#!/usr/bin/env python3
"""
云端 LLM 延迟基准 — 验证语音链路里 "STT → 云端 LLM → TTS" 中间那一段
=================================================================

为什么单独测这段：
  STT / TTS 的延迟由本地 RK3576 算力决定（已用 rkvoice-stream 实测：
  STT ~0.29 RTF，TTS 首音 ~0.3s）。但云端 LLM 那一段的延迟由
  「你所在网络 → Anthropic API」的实际链路决定，与硬件无关，
  所以必须在你的真实网络环境里、用你的 key 跑才准。

关键指标：TTFT（Time To First Token，首 token 延迟）
  配合流式 TTS，用户听到第一句话的时间 ≈ STT完成 + LLM首token + TTS首音，
  不需要等 LLM 整段生成完。所以 TTFT 比 "总时长" 更能代表真实体验。

用法：
  export ANTHROPIC_KEY=sk-ant-xxx
  # 国内直连慢/超时时，可指向你的代理/中转：
  # export ANTHROPIC_BASE_URL=https://你的中转地址
  python llm_latency_bench.py

无需 pip install，纯标准库。
"""

import urllib.request, urllib.error
import json, os, ssl, time, statistics

# ─── 配置 ────────────────────────────────────────────────────────
ANTHROPIC_KEY  = os.environ.get("ANTHROPIC_KEY", "")
BASE_URL       = os.environ.get("ANTHROPIC_BASE_URL", "https://api.anthropic.com").rstrip("/")
CLAUDE_MODEL   = "claude-haiku-4-5-20251001"   # 最快的模型，匹配语音助手用例
MAX_TOKENS     = 200
SYSTEM_PROMPT  = "你是 AR 运动眼镜的 AI 助手，回答简洁（两三句话），用中文。"

# 模拟真实运动场景的语音指令
QUERIES = [
    "前面那个旗杆离我大概多远？",
    "现在风速多大，我这一杆该用几号杆？",
    "帮我记录这一杆的成绩。",
    "今天打了几洞了，平均杆数多少？",
    "右边水障碍离我多少码？",
]

ROUNDS_PER_QUERY = 2   # 每条指令测几次取平均

SSL_CTX = ssl.create_default_context()
# 若遇 SSL 错误，取消注释：
# SSL_CTX.check_hostname = False
# SSL_CTX.verify_mode = ssl.CERT_NONE


def measure_once(prompt):
    """发一次流式请求，返回 (TTFT 秒, 总时长 秒, 输出文本)。失败返回 (None, None, 错误信息)。"""
    body = json.dumps({
        "model": CLAUDE_MODEL,
        "max_tokens": MAX_TOKENS,
        "system": SYSTEM_PROMPT,
        "stream": True,
        "messages": [{"role": "user", "content": prompt}],
    }).encode()

    req = urllib.request.Request(
        f"{BASE_URL}/v1/messages",
        data=body,
        headers={
            "x-api-key": ANTHROPIC_KEY,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        method="POST",
    )

    t0 = time.time()
    ttft = None
    text_parts = []
    try:
        with urllib.request.urlopen(req, context=SSL_CTX, timeout=30) as resp:
            for raw in resp:
                line = raw.decode("utf-8", "ignore").strip()
                if not line.startswith("data:"):
                    continue
                payload = line[5:].strip()
                if not payload:
                    continue
                try:
                    evt = json.loads(payload)
                except json.JSONDecodeError:
                    continue
                if evt.get("type") == "content_block_delta":
                    delta = evt.get("delta", {}).get("text", "")
                    if delta:
                        if ttft is None:
                            ttft = time.time() - t0   # 第一个文本 token 到达
                        text_parts.append(delta)
    except urllib.error.HTTPError as e:
        return None, None, f"HTTP {e.code}: {e.read().decode('utf-8','ignore')[:200]}"
    except Exception as e:
        return None, None, f"{type(e).__name__}: {e}"

    total = time.time() - t0
    return ttft, total, "".join(text_parts)


def main():
    if not ANTHROPIC_KEY:
        print("✗ 未设置 ANTHROPIC_KEY")
        print("  export ANTHROPIC_KEY=sk-ant-xxx")
        print("  （国内直连慢可加 export ANTHROPIC_BASE_URL=你的中转地址）")
        return

    print(f"模型: {CLAUDE_MODEL}")
    print(f"端点: {BASE_URL}")
    print(f"指令数: {len(QUERIES)} × {ROUNDS_PER_QUERY} 轮\n")
    print(f"{'指令':<24} {'TTFT(首token)':>14} {'总时长':>10}")
    print("─" * 52)

    ttfts, totals = [], []
    for q in QUERIES:
        for r in range(ROUNDS_PER_QUERY):
            ttft, total, out = measure_once(q)
            if ttft is None:
                print(f"{q[:22]:<24} {'失败: ' + out:>14}")
                continue
            ttfts.append(ttft)
            totals.append(total)
            label = q[:22] if r == 0 else ""
            print(f"{label:<24} {ttft*1000:>11.0f} ms {total*1000:>7.0f} ms")

    if not ttfts:
        print("\n✗ 全部失败 —— 检查网络 / key / 是否需要中转")
        return

    print("─" * 52)
    print(f"\n样本数: {len(ttfts)}")
    print(f"TTFT  : 中位 {statistics.median(ttfts)*1000:.0f} ms | "
          f"均值 {statistics.mean(ttfts)*1000:.0f} ms | "
          f"最差 {max(ttfts)*1000:.0f} ms")
    print(f"总时长: 中位 {statistics.median(totals)*1000:.0f} ms | "
          f"均值 {statistics.mean(totals)*1000:.0f} ms | "
          f"最差 {max(totals)*1000:.0f} ms")

    # 估算完整语音链路（流式）
    stt = 1.5   # Paraformer hybrid, 5s 语音, RK3576 实测 ~0.29 RTF
    tts_ttfa = 0.3  # Matcha+Vocos, RK3576 实测首音 ~320ms
    first_audio = stt + statistics.median(ttfts) + tts_ttfa
    print(f"\n估算 —— 用户听到第一句话的延迟（流式链路）:")
    print(f"  STT({stt}s) + LLM首token({statistics.median(ttfts):.2f}s) + TTS首音({tts_ttfa}s)")
    print(f"  ≈ {first_audio:.1f}s   （目标 < 2s {'✅' if first_audio < 2 else '⚠️ 偏高，主要看 LLM 链路'}）")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
AR 眼镜语音闭环 — 运行在 RV1106 板子上
流程：麦克风录音 → Whisper STT → Claude AI → OpenAI TTS → 喇叭播放

依赖：Python3 标准库 + arecord (ALSA) + ffplay (已在板子上)
无需 pip install 任何包。

配置：把下面三个 KEY 填上即可。
"""

import urllib.request, urllib.error
import json, subprocess, sys, os, ssl, time

# ─── 配置 ────────────────────────────────────────────────────────
ANTHROPIC_KEY  = os.environ.get("ANTHROPIC_KEY", "")   # sk-ant-...
OPENAI_KEY     = os.environ.get("OPENAI_KEY", "")      # sk-... (Whisper STT + TTS)

RECORD_SECONDS = 5          # 每次录音时长
MIC_DEVICE     = "hw:0,0"  # ALSA 设备，运行 arecord -l 确认
MIC_RATE       = 16000      # 16kHz，Whisper 推荐
SPEAKER_DEVICE = "hw:0,0"  # 播放设备，运行 aplay -l 确认

CLAUDE_MODEL   = "claude-haiku-4-5-20251001"
TTS_VOICE      = "nova"     # alloy / echo / fable / onyx / nova / shimmer
TTS_MODEL      = "tts-1"

SYSTEM_PROMPT  = "你是 AR 眼镜的 AI 助手，回答简洁（两三句话），用中文。"

WAV_PATH  = "/tmp/ar_input.wav"
MP3_PATH  = "/tmp/ar_response.mp3"

# SSL 上下文（Buildroot 证书库可能不完整，必要时跳过验证）
SSL_CTX = ssl.create_default_context()
# 如果出现 SSL 错误，取消下面两行注释：
# SSL_CTX.check_hostname = False
# SSL_CTX.verify_mode = ssl.CERT_NONE

# ─── 工具函数 ────────────────────────────────────────────────────

def post_json(url, headers, payload_dict):
    """发送 JSON 请求，返回 response dict"""
    data = json.dumps(payload_dict).encode()
    req = urllib.request.Request(url, data=data, headers={
        "Content-Type": "application/json",
        **headers
    })
    with urllib.request.urlopen(req, context=SSL_CTX, timeout=30) as r:
        return json.loads(r.read())


def record_audio():
    """用 ALSA arecord 录音，保存为 WAV"""
    print(f"[🎙] 录音 {RECORD_SECONDS}s...")
    subprocess.run([
        "arecord",
        "-D", MIC_DEVICE,
        "-f", "S16_LE",       # 16-bit signed little-endian
        "-r", str(MIC_RATE),
        "-c", "1",            # 单声道
        "-d", str(RECORD_SECONDS),
        WAV_PATH
    ], check=True, stderr=subprocess.DEVNULL)
    size = os.path.getsize(WAV_PATH)
    print(f"[🎙] 录音完成，{size} bytes")
    return WAV_PATH


def speech_to_text(wav_path):
    """发送 WAV 到 Whisper API，返回识别文本"""
    print("[📡] STT: 发送到 Whisper...")
    boundary = b"----WavBoundary7a3f"
    with open(wav_path, "rb") as f:
        audio_bytes = f.read()

    body = (
        b"--" + boundary + b"\r\n"
        b'Content-Disposition: form-data; name="file"; filename="audio.wav"\r\n'
        b"Content-Type: audio/wav\r\n\r\n" + audio_bytes + b"\r\n"
        b"--" + boundary + b"\r\n"
        b'Content-Disposition: form-data; name="model"\r\n\r\n'
        b"whisper-1\r\n"
        b"--" + boundary + b"\r\n"
        b'Content-Disposition: form-data; name="language"\r\n\r\n'
        b"zh\r\n"
        b"--" + boundary + b"--\r\n"
    )

    req = urllib.request.Request(
        "https://api.openai.com/v1/audio/transcriptions",
        data=body,
        headers={
            "Authorization": f"Bearer {OPENAI_KEY}",
            "Content-Type": f"multipart/form-data; boundary={boundary.decode()}"
        }
    )
    with urllib.request.urlopen(req, context=SSL_CTX, timeout=30) as r:
        text = json.loads(r.read())["text"].strip()
    print(f"[📡] 识别结果：{text}")
    return text


def ask_claude(text, history=None):
    """发送文本到 Claude，返回回复"""
    print("[🤖] 发送到 Claude...")
    messages = (history or []) + [{"role": "user", "content": text}]
    result = post_json(
        "https://api.anthropic.com/v1/messages",
        headers={"x-api-key": ANTHROPIC_KEY, "anthropic-version": "2023-06-01"},
        payload_dict={
            "model": CLAUDE_MODEL,
            "max_tokens": 200,
            "system": SYSTEM_PROMPT,
            "messages": messages
        }
    )
    reply = result["content"][0]["text"].strip()
    print(f"[🤖] Claude：{reply}")
    return reply, messages + [{"role": "assistant", "content": reply}]


def text_to_speech(text):
    """发送文本到 OpenAI TTS，下载 MP3 后用 ffplay 播放"""
    print("[🔊] TTS: 合成语音...")
    result_bytes = None
    req = urllib.request.Request(
        "https://api.openai.com/v1/audio/speech",
        data=json.dumps({"model": TTS_MODEL, "input": text, "voice": TTS_VOICE}).encode(),
        headers={
            "Authorization": f"Bearer {OPENAI_KEY}",
            "Content-Type": "application/json"
        }
    )
    with urllib.request.urlopen(req, context=SSL_CTX, timeout=30) as r:
        result_bytes = r.read()
    with open(MP3_PATH, "wb") as f:
        f.write(result_bytes)
    print(f"[🔊] 播放语音 ({len(result_bytes)} bytes)...")
    subprocess.run(
        ["ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet", MP3_PATH],
        check=True
    )


# ─── 主循环 ──────────────────────────────────────────────────────

def check_config():
    missing = []
    if not ANTHROPIC_KEY:
        missing.append("ANTHROPIC_KEY")
    if not OPENAI_KEY:
        missing.append("OPENAI_KEY")
    if missing:
        print(f"[!] 缺少环境变量：{', '.join(missing)}")
        print("    export ANTHROPIC_KEY=sk-ant-xxx")
        print("    export OPENAI_KEY=sk-xxx")
        sys.exit(1)


def test_wifi():
    """快速测试 WiFi 能否访问外网"""
    print("[WiFi] 测试外网连接...")
    try:
        req = urllib.request.Request("https://api.anthropic.com", method="HEAD")
        urllib.request.urlopen(req, context=SSL_CTX, timeout=5)
        print("[WiFi] ✅ 外网通")
    except Exception as e:
        print(f"[WiFi] ❌ 外网不通：{e}")
        sys.exit(1)


def main():
    check_config()
    test_wifi()

    print("\n=== AR 眼镜语音助手启动 ===")
    print("按 Ctrl+C 退出\n")

    history = []   # 保留对话历史（最近 4 轮）

    while True:
        try:
            input("[Enter] 按 Enter 开始说话...")
            record_audio()
            user_text = speech_to_text(WAV_PATH)

            if not user_text:
                print("[!] 未识别到语音，重试")
                continue

            reply, history = ask_claude(user_text, history[-8:])  # 保留最近 4 轮
            text_to_speech(reply)
            print()

        except KeyboardInterrupt:
            print("\n退出")
            break
        except subprocess.CalledProcessError as e:
            print(f"[!] 命令错误：{e}")
        except urllib.error.URLError as e:
            print(f"[!] 网络错误：{e}")
        except Exception as e:
            print(f"[!] 未知错误：{e}")
            import traceback; traceback.print_exc()


if __name__ == "__main__":
    main()

# 市面眼镜全芯片调研

> 按 `hardware_rnd_workflow.md` 标准 · 2026-06-29
> 标注：✅实测/拆解 · 🔶估算 · ❓未查证。每条附来源。
> 我们目标基线：轻便(<50g)、便宜、离线/自主、可二次 PCB。

---

## 一、先分清两类眼镜(决定芯片差异)

| 类别 | 有无显示 | 代表 | 芯片重点 |
|------|---------|------|---------|
| **拍摄/音频眼镜** | 无显示 | Ray-Ban Meta Gen2、闪极、小米 | SoC + 摄像头 + 音频,**轻、便宜** |
| **AR 显示眼镜** | 有 HUD | Meta Ray-Ban Display、RayNeo X3 Pro、Rokid | 多一套**光机+波导**(贵、重、耗电的根源) |

> 我们做运动 HUD,属第二类——但光机是铁三角里最难的一环。

---

## 二、竞品整机芯片拆解(已核实)

### Meta Ray-Ban Display(2025/9,AR 显示)
[TechInsights](https://www.techinsights.com/blog/meta-ray-ban-display-teardown-reveals-more-meets-eye) · [KGOnTech](https://kguttag.com/2025/10/30/meta-ray-ban-display-part-1-lumus-waveguide-omnivision-lcos-and-goertek-projection-engine/)

| 功能 | 型号/厂商 | 备注 |
|------|----------|------|
| 主控 SoC | Qualcomm **Snapdragon AR1 Gen1** | ✅ NDA-only |
| 光机 | **OmniVision LCoS** 微投影(600×600)+ Goertek 光机 | ✅ |
| 波导 | **Lumus + Schott** 几何光波导 | ✅ 贵 |
| 手环 SoC | Qualcomm **QCC5100**(肌电手环,手势) | ✅ |

### RayNeo X3 Pro(2025/12,AR 显示,76g 钛架)
[ARMdevices](https://armdevices.net/2026/01/18/rayneo-x3-pro-aiar-glasses-snapdragon-ar1-microled-waveguide-gemini-demos/) · [EET-China](https://www.eet-china.com/mp/a407905.html)

| 功能 | 型号/厂商 | 备注 |
|------|----------|------|
| 主控 | Snapdragon **AR1 Gen1** | ✅ |
| 显示 | 全彩 **MicroLED 波导**(双眼,6000nits 峰值) | ✅ |
| 主摄 | **Sony IMX681**(12MP) | ✅ |
| 空间摄像头 | OmniVision(SLAM/深度) | ✅ |

### Ray-Ban Meta Gen2(拍摄眼镜,48g)— 见 [[glasses-hardware-anatomy]]
SoC=AR1 Gen1｜摄像头=**Sony IMX681**｜IMU=**TDK ICM-42688**｜5 麦阵列｜WiFi6+BT5.3(AR1集成)

### 闪极 SHARGE A1(国产拍摄眼镜,50g)— 见 [[glasses-hardware-anatomy]]
SoC=**Unisoc W517**(淘宝可买,生态弱)｜唤醒词=**NationalChip GX8002**(70µW)｜功放=**Awinic AW88166**×2｜IMU=ICM-42688｜模组=UMW2652(WiFi/BT/GNSS)

### Ray-Ban Stories Gen1 — 见 [[glasses-hardware-anatomy]]
SoC=Snapdragon Wear 4100｜always-on=**NXP MIMXRT685**｜功放=**Cirrus CS35L41B**｜Buck-Boost=**TI TPS63811**｜WiFi/BT=Murata Type1LV

---

## 三、按器件类别 · 四轴 + 厂商/可及性/价格

### 主控 SoC
| 型号 | 厂商 | 散热 | 功耗(活跃) | 重量 | 算力 | 可及性 | 价 | 对齐 |
|------|------|------|----------|------|------|--------|----|------|
| Snapdragon AR1 Gen1 | Qualcomm | 低(为眼镜优化) | 0.8-1.2W🔶 | 集成小 | 4-6 TOPS | ❌NDA | 不公开 | 买不到 |
| **RK3576**(我们) | 瑞芯微 | 中(需导热) | 1.5-2.5W | 中 | 6 TOPS | ✅立创 | ¥165 | **一致** |
| Unisoc W517 | 紫光展锐 | 低 | 🔶 | 集成 | 2-4 TOPS | ⚠️淘宝 | 不公开 | 算力偏弱 |

### 显示光机(HUD 的核心代价)— 四轴最关键
| 方案 | 厂商 | 散热 | 功耗 | 重量 | 算力 | 可及性 | 价 | 对齐 |
|------|------|------|------|------|------|--------|----|------|
| **MicroLED**(JBD Hummingbird Mini II) | JBD | 低 | **60mW@8流明** ✅ | **~1g** ✅ | N/A | ⚠️OEM/送样 | 🔶高(量产降) | 最轻最省,**理想但难拿** |
| 微 OLED(Sony ECX350F) | Sony | 低 | 150-250mW🔶 | 模组0.7-2g ✅ | N/A | ⚠️NDA/集成商 | 🔶$数百-千 | 户外亮度偏弱 |
| LCoS(Meta Display 用) | OmniVision | 中 | 较高🔶 | 较重 | N/A | ⚠️ | 🔶 | 不推荐(重/耗电) |
| 波导(Lumus/Schott/MicroLED) | Lumus等 | — | — | 3-8g🔶 | N/A | ❌高NRE | $200-800🔶 | 量产>5万才划算 |
| 鸟巢/Birdbath | 多家 | — | — | 8-15g🔶 | N/A | ✅注塑 | $50-200🔶 | 轻便方案,startup 可行 |

来源:[JBD官方](https://www.jb-display.com/newsdetails/76.html)、[Sony微OLED](https://www.displaymodule.com/blogs/knowledge/micro-oled-for-smart-glasses-pixel-density-ppi-weight-power-efficiency)、[AR光机功耗论文](https://www.spiedigitallibrary.org/journals/advanced-photonics/volume-7/issue-3/034001/)

### 唤醒词 / always-on 协处理器
| 型号 | 厂商 | 待机功耗 | 重量 | 可及性 | 价 | 对齐 |
|------|------|---------|------|--------|----|------|
| **Syntiant NDP120** | Syntiant(独立在售✅) | ~1mW级,带波束成形/降噪 | 可忽略 | ✅有eval kit | $6@10k✅ | 量产理想 |
| NationalChip GX8002 | 国芯 | **70µW**(闪极在用) | 可忽略 | ✅LCSC | 低🔶 | 便宜,英文文档少 |
| ESP32-S3 | 乐鑫 | 深睡µW级,监听30-50mW | 可忽略 | ✅到处买 | ¥40-60 | **验证阶段首选** |

来源:[Syntiant NDP120](https://www.syntiant.com/ndp120)(纠正:**未被收购,仍独立**)

### 摄像头
| 型号 | 厂商 | 功耗 | 快门 | 可及性 | 价 | 对齐 |
|------|------|------|------|--------|----|------|
| Sony IMX681 | Sony | 150-300mW🔶 | — | ⚠️模组/OEM | 模组$60-150🔶 | Ray-Ban/RayNeo 同款,贵 |
| SC530AI | SmartSens | 50-100mW🔶 | 卷帘 | ✅(我们已用) | $10-25🔶 | 便宜,够静态检测 |
| IMX415(套餐) | Sony | 🔶 | 卷帘 | ✅随板 | 含套餐 | 验证够用 |

### 音频功放 / IMU / 电源(商品件:可忽略重量散热,均开放可买)
| 类别 | 推荐型号 | 厂商 | 功耗 | 可及性 | 价 |
|------|---------|------|------|--------|----|
| 功放 | CS35L41B / **AW88166** | Cirrus / Awinic | 活跃200-500mW🔶 | ✅LCSC | <¥15 |
| IMU | **TDK ICM-42688** | TDK | 活跃 1-8mW✅ | ✅LCSC | ¥15-40 |
| Buck-Boost | TI TPS63xxx | TI | 高效85-92%🔶 | ✅ | <¥10 |
| MEMS 麦 | 通用 | 多家 | µW级 | ✅ | <¥3 |

---

## 四、对齐判断:与我们 <50g 自主运动眼镜的出入

| 维度 | 结论 |
|------|------|
| **主控** | AR1 最优但买不到;RK3576 唯一可及且达标 → **一致** |
| **光机** | JBD MicroLED(1g/60mW)是理想,但 OEM/送样难拿;startup 现实路径 = 微OLED+Birdbath → **有出入(光机是最大障碍)** |
| **唤醒词** | 验证用 ESP32-S3,量产 NDP120/GX8002 → **一致** |
| **摄像头/IMU/音频/电源** | 全是开放可买的便宜商品件 → **完全一致** |
| **整机重量** | 商品件都轻,**重量瓶颈全在光机+波导+电池**,不在芯片 |

### 一句话
> 除了主控(RK3576 已解决)和**显示光机**,其余所有芯片都开放、便宜、轻、低功耗,与我们目标一致。**真正卡住"轻便+便宜"的不是任何芯片,是 HUD 光机和波导**——这才是下一个要专门攻的选型。

---

## 五、未查证项(诚实列出)
- 小米/百度/字节 AI 眼镜的完整芯片(2025 新品,公开拆解少)❓
- Rokid Glasses 除 JBD MicroLED 外的主控与 PMIC ❓
- 各光机在**户外强光**下达到可用亮度时的真实功耗(论文级,需深挖)❓
- JBD/Sony 光机对学生团队的**实际可及性与最小起订量** ❓

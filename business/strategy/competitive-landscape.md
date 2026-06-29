# Second Eye — Competitive Landscape

_Researched 2026-06-30. Prices as of mid-2026; verify before quoting externally._

## Headline: the market splits cleanly, and the split tells us the wedge

1. **Information access (reading, scene, faces) is commoditized to FREE** — three good free phone apps own it, and the $4,490 category king (OrCam) just **died** trying to charge for it.
2. **Mobility (real-time obstacle/path detection while walking) is the only job that still sustains dedicated hardware** — because phones can't do it. But every player there is expensive, subscription-locked, or in the wrong form factor.

That gap — affordable, offline, no-subscription, hands-free glasses for mobility — is the open lane.

## The map

| Product | Job | Price | Form factor | Offline / no-sub? | The weakness |
|---|---|---|---|---|---|
| **OrCam MyEye 3 Pro** | Reading / faces / products | $3,689–$4,490 | Clip-on glasses | Yes | **Company collapsed; exited vision for hearing aids. Killed by free phone AI.** |
| **Envision Glasses** | Reading / scene | $2,499 | Glasses (Google Glass base) | Partial | No obstacle/mobility at all; company has struggled |
| **eSight Go** | Magnification for LOW-VISION (not blind) | $4,950 | Bulky OLED-display headset | — | Display-based, needs residual sight; bulky; 3h battery; pricey |
| **biped NOA** | Mobility + scene + GPS nav | ~£800 + ~$40/mo | Chest vest | No (subscription) | Vest, not glasses; subscription; Honda-AI but needs connectivity |
| **.lumen** | Guide-dog-replacement navigation | €9,999 (~$11,800) | Bulky headset | — | ~15–20x our price; heavy |
| **Ara (Strap Tech)** | Mobility / obstacle | $2,750 | Chest-worn | — | Pricey; early-stage |
| **Glide (Glidance)** | Guided mobility | $1,199 + $30/mo | Handheld wheeled robot | No | Not wearable; subscription; not yet shipped |
| **WeWALK Smart Cane 2** | Mobility + voice (Gemini) | $850–$1,150 | Smart cane | No (cloud AI) | It's a cane (not hands-free); cloud-dependent |
| **Aira** | Human agent describes/navigates | $26–$1,160/mo | Phone + live human | No | Expensive subscription; needs a person + connectivity |
| **Seeing AI** (Microsoft) | Reading / scene | FREE | Phone app | No | Phone-in-hand; not real-time walking |
| **Be My Eyes / Be My AI** | AI + human describe | FREE | Phone app | No | Phone-in-hand; not real-time walking |
| **Google Lookout** | Read / explore / shop | FREE | Phone app (Android) | Partial | Android-only; phone-in-hand |

## What this means

**Do not build reading as the reason-to-buy.** That's the OrCam trap. Users say they want reading (the user-preference survey from the first research pass), but they will not pay for *hardware* to get it when Seeing AI, Be My AI, and Lookout do it free. OrCam built the best reading hardware on earth and still died. Reading should be a free bonus on our stack, never the pitch.

**Mobility is the defensible hardware wedge — for a structural reason, not just a preference one.** It's the one job a phone physically can't do (you can't hold a phone up scanning the sidewalk while walking with a cane), which is why a funded category exists: NOA, .lumen, Ara, Glide, WeWALK. That validates demand for mobility hardware. The first research pass said "mobility isn't validated by user preference" — true, but the competitor map resolves it: mobility is validated by *revealed willingness to pay for hardware*, which is what matters for a hardware company.

**The open lane is price + offline + form factor.** Nobody owns "affordable + offline + no-subscription + hands-free glasses" for mobility:
- vs **.lumen** (€9,999): ~15–20x cheaper.
- vs **Ara** ($2,750), **Glide** ($1,199+$30/mo), **NOA** (£800+$40/mo): cheaper, and offline with no subscription.
- vs **WeWALK** ($850–1,150): glasses and hands-free, not a cane; and offline vs its Gemini cloud.
- vs everyone: on-device/offline is unique — the whole field leans cloud/subscription.

## The catch (this is the real risk)
Every player that does serious obstacle detection uses **bulkier hardware for a reason**: NOA's wide-angle cameras on a vest, .lumen's headset, Ara's chest unit. Wide field-of-view + depth sensing is hard to cram into a sub-50g sport frame. Our differentiation (cheap, offline, sleek glasses) collides with the physics of good obstacle detection. **Whether Jackie's stack can detect obstacles well enough in a thin frame, outdoors, is the make-or-break technical question.**

## Emerging / watch
- **EchoVision** and a wave of cheap "AI glasses" entrants are appearing — the affordable-AI-glasses space will get crowded. Speed and the blind-community trust/distribution moat matter.

## Sources
- OrCam collapse: https://www.calcalistech.com/ctechnews/article/hy0rv6qya · product: https://www.orcam.com/en-us/orcam-myeye-3-pro
- eSight Go pricing: https://www.esighteyewear.com/esight-go-pricing/
- biped NOA: https://biped.ai/noa
- .lumen: https://www.dotlumen.com/glasses · Ara: https://strap.tech/shop/p/ara-device
- WeWALK: https://wewalk.io/en/product/
- Envision: https://shop.letsenvision.com/products/glasses-home · Glide: https://glidance.io/preorder/ · Aira: https://aira.io/subscriptions/
- Free apps comparison: Seeing AI / Be My Eyes / Google Lookout (see strategy notes)

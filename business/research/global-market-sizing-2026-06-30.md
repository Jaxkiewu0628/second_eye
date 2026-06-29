# Second Eye — Defensible Global Market Sizing

_Researched 2026-06-30. Primary sources: WHO World Report on Vision, IAPB Vision Atlas, Lancet Global Health (GBD 2019/2020 Vision Loss Expert Group), CDC, JAMA Ophthalmology, NFB, AFB/NHIS. Every number is tagged **[MEASURED]** (cited to a primary source) or **[ESTIMATED]** (our reasoning from cited inputs). See `## Sources`._

---

## TL;DR verdict

The headline "2.2 billion vision-impaired" number is real but useless for us — it is ~95% uncorrected refractive error and presbyopia (people who need glasses or reading glasses, not an obstacle-detection wearable). The number that matters for a **mobility-first, non-visual** device is **~43 million blind worldwide [MEASURED]**, of whom maybe **~9–11M live in high-income markets we can reach [ESTIMATED]**. The single biggest sizing risk is the **blind-vs-low-vision split**: our non-visual wedge fits the **blind** (43M global / ~0.4–1M US functional core), but the much larger **moderate-to-severe low-vision** population (295M global) retains usable sight and disproportionately wants a *visual* magnifier/display — a product we are explicitly not building. Sizing the blind core honestly makes the TAM ~7x smaller than a "vision impairment" headline would suggest, but it is the *correct* denominator for this product.

---

## 1. Global figures — blind vs. low vision (WHO / IAPB / Lancet GBD)

All three bodies report the **same underlying dataset**: the Global Burden of Disease (GBD) 2020 estimates produced by the **Vision Loss Expert Group (VLEG)**, published in *Lancet Global Health* (Bourne et al., Dec 2020 / 2021). WHO World Report on Vision and the IAPB Vision Atlas both cite these. So "WHO vs IAPB vs Lancet" is not three independent checks — it is one number, well-triangulated.

**Global, 2020 [MEASURED — GBD/VLEG, Lancet Global Health]:**

| Category | Definition (visual acuity, better eye) | People (2020) | 2050 projection |
|---|---|---|---|
| **Blind** | < 3/60 (≈ <20/400), or visual field <10° | **43.3 million** (95% UI 37.6–48.4) | 61.0 million |
| **Severe vision impairment** | ≥3/60 but <6/60 | 34.8 million | — |
| **Moderate vision impairment** | ≥6/60 but <6/18 | 260 million | — |
| **MSVI (moderate + severe combined)** | <6/18 to 3/60 | **295 million** (267–325) | 474 million |
| **Mild vision impairment** | ≥6/18 and <6/12 | 258 million | 360 million |
| **Near-vision impairment (presbyopia)** | uncorrected presbyopia | 510 million | 866 million |

**The "2.2 billion" headline [MEASURED — WHO World Report on Vision, 2019]:** WHO states "at least 2.2 billion people have a vision impairment," of whom "at least 1 billion have a vision impairment that could have been prevented or is yet to be addressed." Critically, WHO itself breaks the preventable 1B down as: unaddressed presbyopia **826 million**, cataract **94M**, uncorrected refractive error **88.4M**, glaucoma 7.7M, AMD 8M, diabetic retinopathy 3.9M. **~95% of "2.2 billion" is uncorrected refractive error + presbyopia** — people who need spectacles, not an assistive wearable. Do not quote 2.2B as our market.

**Key trend [MEASURED]:** age-standardized blindness prevalence fell 28.5% (1990–2020) thanks to cataract surgery scale-up, but the **absolute number of blind rose ~50.6%** and MSVI rose ~91.7% due to population growth and aging. The market is growing in absolute terms, driven by 65+ aging in high-income countries — favorable for us.

**Age skew [MEASURED — GBD]:** ~**78% of all blind people are 50+**. Blindness is overwhelmingly an aging condition globally. This matters: our independently-mobile, travel-motivated, tech-adopting wedge user is a *minority slice* of a population whose median member is elderly.

---

## 2. US-specific: blind & low-vision, working-age vs 65+

US numbers vary 10x depending on definition (clinical legal-blindness vs self-reported "any trouble seeing"). This is the central sizing trap, so all four are tabled with their definition.

| Source / definition | Figure | Year | Tag |
|---|---|---|---|
| **Legally blind** (≤20/200), all ages — JAMA/Varma | **~1.0 million** | 2015 | MEASURED |
| **Best-corrected visual impairment** (≤20/40), age 40+ — JAMA/Varma | **3.2 million** (→8.96M incl. blind by 2050) | 2015 | MEASURED |
| **Vision impairment incl. blindness** — CDC | **~7 million**, incl. **~1 million blind** | CDC page (no yr) | MEASURED |
| **Legally blind, age 40+** — NFB (cites NEI) | **~1.3 million** | ~2010s | MEASURED |
| **Blind or low vision (combined)** — Center for Research on Disability / ACS | **8.29 million** | 2023 | MEASURED |
| **"Any difficulty seeing" (self-report)** — AFB/NHIS | **49.5 million** adults | 2024 | MEASURED |

**The NHIS 49.5M is a trap number** — it is self-reported *any* difficulty including correctable/minor. AFB/NHIS itself decomposes it: **45.3M "minor difficulty," 3.8M "significant difficulty," and only 420,000 "cannot see at all."** The functionally-blind US core relevant to a non-visual device is on the order of **0.4M (cannot see at all) to ~1M (legally blind)** — NOT 49.5M, NOT 8.3M.

**Working-age vs 65+ [MEASURED — AFB/NHIS 2024]:**
- Working-age (18–64) reporting difficulty seeing: **~33 million** (loose definition).
- 65+: **~13.6 million** (loose definition).
- Note the counterintuitive split: under the loose NHIS definition, working-age *outnumbers* 65+ in raw count, because mild/correctable difficulty is common at all ages — but under clinical definitions, severe loss concentrates in 65+.
- Cornell/ACS: of **~2 million working-age adults with vision loss, only ~35% are employed** [MEASURED — Cornell Yang-Tan, 2017]; AFB reports **~44% employment** for blind/VI overall vs 79% for non-disabled. NFB survey: ~32–37% employment.

**Why working-age matters:** voc-rehab (state VR) and VA funding target *employment outcomes*, so the **~2M working-age vision-loss / ~0.7M working-age severe-or-blind** segment is the reimbursable wedge, even though it is smaller than the 65+ population.

---

## 3. TAM / SAM / SOM — offline, mobility-first, sub-$700

Assumptions stated explicitly; **mark of the funnel is intentionally conservative because the wedge is non-visual** (see §5).

### TAM — global people who could use a mobility aid
**Definition:** people whose distance vision is impaired enough that real-time obstacle/path detection has value while walking — i.e., blind + severe + the harder end of moderate.

- Blind (43.3M) + severe VI (34.8M) = **78M [MEASURED inputs]** is the tightest "needs non-visual mobility help" pool.
- Add moderate VI who still struggle with mobility at night / in clutter: blind + MSVI = **~338M [MEASURED]** is the loosest defensible TAM.
- **TAM = ~78M (tight, non-visual core) to ~338M (broad, all MSVI). [ESTIMATED bracket from MEASURED inputs.]** Use **78M** as the honest mobility-device TAM; 338M only if a visual display variant is later built.

### SAM — realistically reachable (developed markets, mobile, can pay ~$500)
**Definition & filters [all ESTIMATED, from MEASURED base]:**
1. **Geography:** high-income regions (US, Canada, Western Europe, high-income Asia-Pacific incl. Japan, AUS/NZ). High-income regions hold very roughly **~10–12% of global blind** (blindness concentrates in South Asia / Sub-Saharan Africa; high-income super-regions have far lower prevalence and ~1B of 7.8B population but disproportionately old). → of 78M tight TAM, **~8–10M in reachable geographies.**
2. **Independently mobile & motivated to travel:** exclude the bedbound, the most elderly frail, and those who never leave home. Assume **~40–50%** of the high-income blind/severe population travels independently. → **~3.5–5M.**
3. **Can afford or get funded ~$500:** high-income + funding paths (VA, voc-rehab, private pay). Assume most of the motivated, mobile segment clears this in high-income markets. → modest haircut.
- **SAM ≈ 3–5 million [ESTIMATED].** Use **~4 million** as the planning SAM (high-income, independently-mobile, blind-to-severe).
- $-terms: 4M × $500 one-time ≈ **$2.0B lifetime device TAM-in-SAM [ESTIMATED]** (not annual; one-time hardware).

### SOM — credible 3-year beachhead
**Definition:** US working-age blind cane-users reachable via VA + state voc-rehab, where the payer path is already validated (status.md).

- US legally blind ≈ 1.0M [MEASURED]. Working-age share (18–64) of the clinical-blind ≈ **~35–40%** → **~0.35–0.4M working-age blind [ESTIMATED from MEASURED]**.
- Cane-using / independently-traveling subset ≈ **~50%** → **~175k–200k [ESTIMATED]**.
- Reachable via VA (blind veterans get electronic mobility devices at no cost) + state VR in first 3 years, at near-zero marketing, realistically a **low-single-digit % penetration**: assume **1–3%** of ~190k → **~2,000–6,000 units over 3 years [ESTIMATED]**.
- $-terms: 4,000 units × ~$500 ≈ **~$2M cumulative revenue, 3-yr beachhead [ESTIMATED]** — small but fundable via grants + a wedge into a defensible niche, not a venture-scale claim on its own.
- **SOM (3-yr beachhead) ≈ 2,000–6,000 units / ~$1–3M [ESTIMATED].**

**Funnel summary:**
| Stage | Number | Basis |
|---|---|---|
| Headline "vision impaired" (DO NOT USE) | 2.2B | WHO [MEASURED] |
| MSVI + blind (broad) | ~338M | GBD [MEASURED] |
| **TAM** (blind + severe, non-visual mobility core) | **~78M** | GBD [MEASURED] |
| **SAM** (high-income, mobile, fundable) | **~4M** | [ESTIMATED] |
| **SOM** (US working-age blind cane-users via VA/VR, 3 yr) | **~2k–6k units / $1–3M** | [ESTIMATED] |

---

## 4. Existing assistive-tech / low-vision-aid market size ($) — flag: low credibility

Analyst reports for "assistive technologies for visually impaired" disagree by **>2x for the *same* year**, which is itself the finding: treat all as directional, not authoritative.

| Firm | 2024/25 value | Forecast | CAGR | Credibility note |
|---|---|---|---|---|
| Mordor Intelligence | $6.34B (2025) | $11.20B by 2030 | 12.05% | mid-pack |
| Research and Markets | $5.40B (2024) | $9.74B by 2030 | 10.32% | mid-pack |
| Business Research Co. | $6.11B (2024) | $12.31B by 2029 | 15% | high CAGR |
| Zion Market Research | $5.72B (2024) | $21.01B by 2034 | 13.89% | aggressive |
| Market Research Future | **$12.06B (2024)** | $19.82B by 2035 | 4.62% | **2x others, low CAGR — outlier** |
| Data Bridge (low-vision aids only) | $0.58B (2023) | $1.03B by 2031 | 7.5% | narrower scope, more plausible for *aids* |

**Credibility flag [MEASURED that these reports exist; their numbers are ESTIMATED/opaque]:** these reports bundle screen readers, braille displays, magnifiers, OCR, smart canes, and software into one "market," with undisclosed methodology. The ~$5–6B cluster is the rough consensus for the *broad* category; the narrower **low-vision-aids hardware market (~$0.6–1B)** is closer to our actual competitive set. **Do not cite a single analyst number to investors as fact** — cite the range and note the dispersion. The bottom-up SAM in §3 ($2B one-time device opportunity) is more defensible than any of these.

---

## 5. The segmentation trap — TRULY BLIND (our wedge) vs LOW VISION (a product we're not building)

**This is the single biggest sizing risk.** Our device is **non-visual**: directional bone-conduction audio "obstacle ahead," no display. That is the right product for someone with **no usable sight** — and the *wrong* product for someone with residual vision who would rather have a **magnifier / high-contrast display / electronic spectacles** (eSight, IrisVision, OXSIGHT) that *use* the sight they have.

**Sizing both sides [MEASURED inputs]:**

| | Global | US (clinical) | Fit to our non-visual device |
|---|---|---|---|
| **Blind** (<3/60) | **43.3M** | ~1.0M legally blind; ~0.42M "cannot see at all" (NHIS) | **STRONG** — non-visual is their only channel |
| **Severe VI** (3/60–6/60) | 34.8M | (subset of the 3.2M VI) | **MODERATE** — some prefer audio, some still use sight |
| **Moderate VI** (6/60–6/18) | 260M | bulk of the 3.2M VI 40+ | **WEAK** — usable sight; visual magnifier likely preferred |
| **Mild VI / presbyopia** | 768M | most of NHIS 49.5M | **NONE** — needs glasses, not an aid |

**Implications:**
- The population that *structurally* needs a non-visual aid (blind) is **~43M global / ~0.4–1M US** — and **low-vision outnumbers truly-blind by roughly 7:1 globally** (295M MSVI vs 43M blind) and ~3:1 in the US clinical sense. This matches our prior internal estimate ("low-vision ~3x bigger").
- **The risk has two faces:** (a) we *correctly* exclude 295M low-vision people, making our TAM look small to investors; (b) we are *tempted* to chase them by adding a display, which destroys the cost/offline advantage (display = the single biggest BOM and risk per our design doc). The discipline is to **own the blind mobility niche** and treat low-vision as out-of-scope, not as upside.
- **Mitigation / nuance:** many "blind" people retain *some* light/motion perception, and obstacle-avoidance is valued even by some low-vision users at night / in unfamiliar space — so the *functional* mobility market is somewhat larger than the strict "no light perception" 0.42M. But do not build the pitch on low-vision: their revealed preference (eSight, IrisVision sales) is for *visual* aids. **Size to the blind; let mobility-motivated low-vision be a bonus, never the denominator.**

**Bottom line for the deck:** lead with "43M blind globally, ~1M US, growing with aging, payer path validated" — a defensible, primary-sourced floor — not "2.2B" or "$12B," which auditors and sophisticated investors will discount on sight.

---

## Sources

All accessed **2026-06-30**.

**Global (WHO / IAPB / Lancet GBD — VLEG):**
- WHO, *World Report on Vision* (2019), incl. "2.2 billion / 1 billion preventable" and cause breakdown: https://www.who.int/publications-detail-redirect/world-report-on-vision and PDF https://www.who.int/docs/default-source/documents/publications/world-vision-report-accessible.pdf
- Bourne R. et al. (GBD 2019 Blindness and Vision Impairment Collaborators / Vision Loss Expert Group), "Trends in prevalence of blindness and distance and near vision impairment over 30 years," *Lancet Global Health* (Dec 2020). Open-access mirror: https://pmc.ncbi.nlm.nih.gov/articles/PMC7820390/ ; journal: https://www.thelancet.com/journals/langlo/article/PIIS2214-109X(20)30425-3/fulltext — used for 43.3M blind, 295M MSVI, 258M mild, 510M presbyopia, 2050 projections, acuity definitions, 78% aged 50+ figure.
- IAPB Vision Atlas (presents the same GBD/VLEG estimates): https://visionatlas.iapb.org/ and https://www.iapb.org/learn/vision-atlas/magnitude-and-projections/ (redirects to visionatlas.iapb.org)

**US:**
- Varma R. et al., "Visual Impairment and Blindness in Adults in the United States: Demographic and Geographic Variations From 2015 to 2050," *JAMA Ophthalmology* (May 19, 2016): https://pubmed.ncbi.nlm.nih.gov/27197072/ ; NEI summary: https://www.nei.nih.gov/research-and-training/research-news/visual-impairment-blindness-cases-us-expected-double-2050 — used for ~1M legally blind / 3.2M VI (2015) → 8.96M by 2050.
- CDC, "Fast Facts: Vision Loss" (updated May 15, 2024): https://www.cdc.gov/vision-health/data-research/vision-loss-facts/index.html — ~7M VI incl. ~1M blind.
- National Federation of the Blind, "Blindness Statistics": https://nfb.org/resources/blindness-statistics — ~1.3M legally blind age 40+ (page returned 403 on automated fetch 2026-06-30; figure corroborated via NFB-sourced search results; verify manually before quoting verbatim).
- American Foundation for the Blind, "Facts and Figures on Adults with Vision Loss from the NHIS" (2024 NHIS, updated Mar 2026): https://afb.org/research-and-initiatives/statistics/adults-vision-loss-nhis — 49.5M "any difficulty seeing"; 33M working-age / 13.6M 65+; 3.8M significant difficulty; 420k "cannot see at all."
- AFB, "Employment Statistics for People who are Blind or Visually Impaired": https://afb.org/research-and-initiatives/statistics/employment-bvi — ~44% employment vs 79% non-disabled; Cornell Yang-Tan / ACS ~35% of ~2M working-age employed.
- Center for Research on Disability, 2025 Disability Statistics Compendium (blind/low-vision): https://www.researchondisability.org/annual-disability-statistics-collection/2025-compendium-table-contents/compilation-expansion-statistics-blind-low-vision-population-compendium-2025 — 8.29M blind/low-vision (2023).

**Market-size analyst reports (low credibility — cite range, not point):**
- Mordor Intelligence: https://www.mordorintelligence.com/industry-reports/assistive-technologies-for-visually-impaired-market
- Research and Markets: https://www.researchandmarkets.com/reports/5948769/assistive-technologies-visually-impaired-market
- The Business Research Company: https://www.thebusinessresearchcompany.com/report/assistive-technologies-for-visually-impaired-global-market-report
- Zion Market Research: https://www.zionmarketresearch.com/report/assistive-technologies-for-visually-impaired-market
- Market Research Future (outlier high): https://www.marketresearchfuture.com/reports/visually-impaired-assistive-technologies-market-34243
- Data Bridge (low-vision aids, narrower): https://www.databridgemarketresearch.com/reports/global-low-vision-aids-market

---

## Methodology & caveats
- "WHO vs IAPB vs Lancet" is **one dataset** (GBD/VLEG 2020), triangulated, not three independent estimates. Treated as a single MEASURED anchor.
- GBD acuity thresholds (e.g., blindness <3/60) differ from the US legal-blindness threshold (≤20/200 ≈ 6/60), so US "legally blind ~1M" and global "blind 43M" are **not the same definition** — US legal blindness is a *looser* cut than GBD blindness, which is part of why US figures look proportionally large.
- All SAM/SOM funnel haircuts are **[ESTIMATED]** judgment calls flagged as such; they are deliberately conservative. Tighten them with the discovery-call data (independently-mobile %, cane-user %, willingness-to-pay) before using in a fundraise.
- Regional super-region splits (high-income share of global blind) were not retrievable from the IAPB Atlas directly today (atlas.iapb.org returned 403/connection-refused on automated fetch); the ~10–12% high-income share is **[ESTIMATED]** from known GBD geographic concentration (South Asia + Sub-Saharan Africa dominate) and should be firmed up against the Atlas regional tables manually.

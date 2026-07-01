# Competitor verification — Industrial machine-safety incumbents (SICK / Pilz / Banner / Keyence / Omron)

> Adversarial verification for the worker-safety pivot. Date: 2026-07-01. Verdict: **CONFIRMED (real, mature, but a different product class) — leaves our gap wide open.**

## In a line
The certified machine-safety incumbents (light curtains, safety laser scanners, safety radar, safety PLCs) are **real, offline, and legally the safety function** — but they are **fixed-mounted machine guarding that STOPS the machine**, not body-worn personal warning. They do not touch our "cheap + wearable + offline **personal** real-time danger warning" niche. Personal body-worn warning is a *separate market* served by *other* vendors.

## What was claimed
- Fixed-mount opto-electronic guarding wired to E-stop / safety controller.
- Offline: yes. Price: light curtain ~$500–3,000/pair; full cell w/ safety PLC $5k–30k+ installed.
- The certified ISO 13849 / SIL "safety function" — legally recognized, actually STOPS the machine. Red ocean, standards-locked, not wearable/personal.

## Verification (primary/vendor sources)

**Real? — YES.** SICK, Banner, Keyence all publish full safety product lines. Ratings confirmed: Type 4 / Category 4 / SIL3 / PL e (IEC 61496, IEC 61508, EN ISO 13849) on SICK C4000 & Banner curtains. These are the legally recognized "safety function." (SICK safety-light-curtains product page; Banner machine-safety page.)

**Form factor — FIXED-MOUNT, NOT WEARABLE (confirmed).**
- Light curtains = emitter/receiver posts framing a machine access point.
- Keyence SZ-V ("world's first safety scanner with integrated cameras") — Keyence's own page: **"fixed-mounted safety device, not wearable... designed for machine guarding."**
- SICK safeRS/safeRS3 radar, nanoScan3 laser scanner = mounted on the machine/AGV/AMR to monitor a **zone around the machine**. nanoScan3 = "constantly monitoring the ground level **around the robot**... stop the robot movement only when a person is too close." The device rides the MACHINE, not the person.

**Offline? — YES (inherent).** Safety devices are hardwired into a safety relay / safety PLC (Pilz PNOZ, SICK Flexi Soft, Banner SC10, AB GuardLogix, Siemens F-CPU) via OSSD outputs to the E-stop circuit. The safety function is local and cloud-independent by design/standard. (Some add optional "remote monitoring" software, but the safety loop is hardwired.)

**"Personal-level real-time danger warning"? — NO. This is the crux.**
- Their safety function acts on the **MACHINE** (stop/slow), triggered by a person entering a **zone**. It is *area* protection, not *personal* protection that rides on the individual.
- Even the camera-forward Keyence SZ-V uses its camera for **"real-time visual feedback and historical images/videos of scanner trips"** — i.e. status/forensics for the maintenance engineer, **not a warning delivered to the worker's body**. Explicitly not a personal-alert device.
- A dedicated search for wearable/body-worn personal warning from SICK/Pilz/Banner/Keyence/Omron returned **zero** of their products. That whole category (haptic/audio alert ON the worker) is served by **different** companies — SlateSafety, Everbridge, Fortecho, MOKOSmart, Spacebands, Reactec, GaTech AwareSite. The incumbents are absent from it.

**Price / model — CONFIRMED order of magnitude.** Light-curtain pairs low-thousands; a compliant cell needs the curtain + a safety relay/PLC + integration labor (min ~6 safety modules conventionally, or 2 with a programmable safety relay), pushing installed cost into the $5k–30k+ range as claimed. Sold B2B via distributors/integrators (capital equipment), not consumer/personal.

**Funding — N/A.** SICK, Pilz, Keyence, Omron are large public/established industrial firms; Banner is a mature private co. Not a startup threat — an entrenched baseline.

## Leaves a gap for us? — YES, WIDE OPEN.
They own the **certified machine-stop** layer (which we neither can nor should contest — it's the legally required baseline everyone respects). But their protection is **fixed, machine-centric, area-based, and capital-priced**. They deliberately do **not** offer a **cheap, body-worn, offline device that warns the individual worker in real time** (avoid mobile machinery / danger zone / collision / fall / lone-work). That is exactly our transferable niche: Second Eye's on-device camera + ToF + YOLO + bone-conduction, riding on the *person* not the machine — complementary to (not competing with) the certified guarding. The incumbent is the "respect-the-baseline" wall, not a competitor in our lane.

## Caveats / watch-items
- **Not our competitor, but our context:** in a real plant, the certified light curtain/scanner is mandatory; a wearable personal-warning device is *additional* PPE-adjacent tech. Our pitch must position as **complementary layer**, never as a replacement for the certified safety function (legally we cannot be the SIL-rated stop).
- **Certification asymmetry is a moat *against* us too:** because they're ISO 13849/SIL-rated and we (initially) are not, buyers may treat us as "nice-to-have" not "safety." Watch whether personal-wearable warning ever gets a recognized standard.
- **Adjacent-vendor threat lives elsewhere:** the real competitive set for our pivot is the body-worn players (SlateSafety, proximity-warning tag vendors, GaTech AwareSite), NOT these five. Verify those separately.

## Sources
- SICK safety light curtains — https://www.sick.com/us/en/products/safety/safety-light-curtains/c/g184853
- SICK safety radar sensors (safeRS/safeRS3) — https://www.sick.com/ch/en/products/safety/safety-radar-sensors/c/g569360
- SICK nanoScan3 launch (The Robot Report) — https://www.therobotreport.com/sick-launches-nanoscan3-safety-laser-scanner/
- SICK sBot + nanoScan3 speed/separation monitoring — https://www.sick.com/us/en/speed-and-separation-monitoring-with-sicks-sbot-safety-system-and-urcap-for-universal-robots/w/press-urcap
- Banner machine safety / light curtains — https://www.bannerengineering.com/us/en/products/machine-safety/safety-light-curtains.html
- Keyence SZ-V safety laser scanner (integrated camera) — https://www.keyence.com/products/safety/laser-scanner/sz-v/
- Safety PLC / relay integration + cost context — https://industrialmonitordirect.com/blogs/knowledgebase/safety-system-integration-legal-bypassing-of-light-curtains-via-plc-and-safety-relay-requirements

# Second Eye — Business / CEO workspace (conventions)

This folder is the CEO / business side of **Second Eye** (assistive AI glasses for the blind: camera + on-device YOLO + ToF → bone-conduction "obstacle ahead," fully offline). **Read `status.md` (current state) and `todo.md` (next actions) first.**

## Our role
We operate as CEO: strategy, market / competition, fundraising, operations, customer discovery. Engineering is Jackie (Zizheng Wu) in `../engineering/` — **READ-ONLY for us.**

## Conventions (important)
- **All CEO / business documents live HERE** (in `business/`). **Never** save project docs in gstack / system storage (`~/.gstack/...`) — that is system storage, not project storage.
- **Never write into `../engineering/`** — it's Jackie's; read it for context only. The one shared channel is the repo-root **`../handoff/`** folder (joint read/write — see *Handoff channel* below). *(The handoff protocol was added once to `engineering/CLAUDE.md` on 2026-06-30 with the user's authorization to bootstrap this — it is not a license to edit eng files generally.)*
- **Report in parts.** Lead with the headline / verdict, then short labeled sections. Don't dump one giant wall of text. Keep chat tight; put long detail in files here.
- **Verify, don't assert.** Cite sources; mark estimates vs. measured. For LLM / competitor / market facts, check primary sources rather than recalling from memory.

## Orientation
- `status.md` — single source of truth (direction, validated / risky, competitive snapshot, org structure)
- `todo.md` — action items / the validation gate
- `strategy/` — design doc, market research, competitive landscape, IP
- `discovery/` — interview guide + recruiting plan (the customer-discovery gate)
- `research/` — raw research archives
- `../handoff/` — **shared CEO ⇄ Jackie handoff channel** (check `../handoff/index.md` at session start for OPEN items addressed to CEO)

## Handoff channel (CEO ⇄ Jackie) — `../handoff/`
The one place complex, cross-domain tasks pass between us and Jackie, **with zero residual** — each handoff is a self-contained file; nothing critical lives only in chat.
- **At session start:** check `../handoff/index.md`; read any `📤 OPEN` item directed `ENG → CEO` in full before acting.
- **To send Jackie a task:** copy `../handoff/_TEMPLATE.md` → `HO-<NNN>-<slug>.md`, fill it self-contained (a fresh session must be able to act from it alone), set state `📤 OPEN`, register a row in `index.md`. Write the body in **中文** (his working language); keep the **TL;DR bilingual**.
- **Conversation stays in the file:** append replies to the handoff's `Thread` section (tagged `[CEO]`/`[ENG]`), update the state, and on close fill `Resolution` + move the row to Archive.
- **Commit:** `../handoff/` is shared root-level — `git add ../handoff/…` when you send or update a handoff (this is the one place we write outside `business/`).

# Apex Syndicate Omega — Medical Negligence Case Skill (v17.1)

Claude ke liye ek **skill** jo India mein medical negligence aur hospital-vivaad (Consumer Commission: DCDRC / SCDRC / NCDRC) ke case ka audit aur drafting karti hai: client se sawal, hospital records ka page-by-page audit, forum aur deadline ki jaanch, standard-of-care audit (deviation, harm, causation, counterfactual alag-alag), red team, aur integrity gate ke peeche drafting (complaint, rejoinder, affidavit, written arguments, hearing prep, vakil ke liye Master Reference File).

> Yeh ek AI sahayak hai. Yeh kisi asli medical expert ki opinion ya enrolled advocate ki jagah nahi leti. Har draft filing se pehle vakil ko dikhana zaroori hai.

## Download aur install

**Taiyar package:** [`dist/apex-syndicate-omega-v17.1.skill`](dist/apex-syndicate-omega-v17.1.skill)

- **claude.ai / Claude app:** Settings → Capabilities → Skills → *Upload skill* → upar wali `.skill` file chuno. (Menu ke naam app ke version ke saath badal sakte hain.)
- **Claude Code:** `apex-syndicate-omega/` folder ko `~/.claude/skills/` (sirf aapke liye) ya project ke `.claude/skills/` mein copy karo.

Install ke baad chat mein case files ke saath likho, jaise *"hospital ke khilaf consumer case hai, records attached hain"*, ya sirf *"Apex Syndicate Omega"*.

## Repo ka dhaancha

```
apex-syndicate-omega/          ← skill ka source (yahi package banta hai)
├── SKILL.md                   ← hamesha load hone wale niyam: core rules 1–28, commands, delivery
├── CHANGELOG.md               ← har version ka hisaab (v17.1 sabse upar)
├── references/                ← har phase ke vistaar wale protocol (zaroorat par padhe jaate hain)
│   ├── power-lines.md         ← TAGDA: legal force + evidentiary precision, source labels, language ladder
│   ├── evidence-and-facts.md  ← Reading Log, Evidence Register (EV-ids), fact sheet, contradictions, CASE IMPACT
│   ├── legal-research.md      ← forum gate, source hierarchy (TIER-A/B/C), citation check, deadlines
│   ├── medical-audit.md       ← benchmark, four findings, intervals, RECORD GAP, expert/committee report ki jaanch
│   ├── strategy-and-drafting.md ← contradiction audit, opponent counter, causation chain, missing-record steps, damages ledger
│   ├── document-templates.md  ← pleadings + Master Reference File, Record-Gap Graph, Audit Trail Table
│   ├── output-gates.md        ← output format, integrity gate, 40-point self-check, highlight gate
│   └── …                      ← case-routing, client-interrogation, specialty-checklists (emergency/cardiac, stroke, …), state, glossary
├── scripts/                   ← sirf arithmetic, Python standard library
│   ├── deadline_calc.py       ← calendar deadline (dono inclusion rules)
│   ├── interval_calc.py       ← ghante-minute ka interval (AM/PM, aadhi raat) aur RECORD GAP list
│   ├── ledger_total.py        ← damages: claimed vs supported, Kam / Base / Zyada, formula ki khud ginti
│   ├── draft_lint.py          ← draft ki numbering, annexure (rejoinder-friendly), internal label leak check
│   └── test_scripts.py        ← in sab ka self-test (55 checks)
└── tests/evals.json           ← 48 test cases (track A: technical, B: legal content)

dist/                          ← upload ke liye taiyar .skill package
docs/audit/                    ← audit ke kagaz: R6 audit prompt, SKILL.md change register, 00 aur 01 audit reports
tools/build_skill.py           ← validate + package banane wala script
.github/workflows/validate.yml ← har push par automatic validation
```

## Commands (chat mein)

`CONTINUE` · `SKIP` · `DIRECT DRAFT` · `FAST MODE` · `ADVOCATE PACK` · `QUICK CHECK` · `UPDATE` · `TAGDA` · `DETAIL` · `SHORT` · `STATE` · `STATE FULL` · `AUDIT-OPP` · `REF-FILE` · `GAP-GRAPH` · `DAMAGES` · `CORRECT` · `CITE-CHECK` · `AUDIT-TRAIL`

- **TAGDA** = jawab ko chhota karna nahi; *Maximum Legal Force + Evidentiary Precision*. Chhota sirf tab hota hai jab aap khud kahein ("chhota karo", "summary do").
- **REF-FILE** = vakil ke liye Master Reference File: banner (KUL POINTS KI SANKHYA, FILE KA MAQSAD), har POINT par 5 hisse (hamari baat → virodhi ka jawab → hamara jawab → kanooni aadhar aur saboot → vakil ke liye antim dalil), aur ant mein Audit Trail Table.
- **AUDIT-OPP** = virodhi ke Written Statement ke har material para ko unke apne annexures, medical record aur court orders se milana — "woh jhooth bol rahe hain" maan kar nahi, record ke label se.
- **GAP-GRAPH** = monitoring ke RECORD GAP ka plain-text graph (gap ≠ "monitoring band thi").

## Badlaav ke baad validate aur build

```bash
python3 tools/build_skill.py
```

Yeh check karta hai: frontmatter (description ≤ 1024 characters, warna claude.ai upload reject karta hai), koi `[PENDING:...]` placeholder na bacha ho, har section-naam ka hawala asli section tak jaaye, `tests/evals.json` valid ho, aur `scripts/test_scripts.py` pass ho. Phir `dist/` mein naya package banata hai. PyYAML chahiye (`pip install pyyaml`).

Sirf jaanch ke liye: `python3 tools/build_skill.py --check` · package source se match karta hai ya nahi: `python3 tools/build_skill.py --verify-dist`

## File doge to skill kya karegi (v17.1)

- **Nayi file aate hi CASE IMPACT:** sabse upar likha milega ki is file se kaunsa point majboot hua (language ladder ka step pehle aur baad), kaunsa kamzor hua, kaunse sawal ya gap band hue, aur agla kadam kya hai. Kamzori bhi utni hi saaf batayi jaati hai.
- **Seedha command bhi chalega:** pehli upload ke saath `REF-FILE` ya `AUDIT-OPP` likho. Skill pehle zaroori intake (Reading Log, forum, deadlines) karegi, phir file degi, aur findings ko PROVISIONAL batayegi.
- **Hospital records na de to:** likhit maang → reminder → Commission mein application → (sarkari hospital ho to RTI ka rasta, NOT VERIFIED) → inkaar record par aane ke baad hi adverse inference ki dalil.
- **Hospital ki committee report ya medical board ki rai:** kisne likhi, kaunse record dekhe, kya poocha gaya, kaunsa standard lagaya. Har nishkarsh record se milaya jaata hai.
- **Vakil ke liye Ground strength table:** har ground ki taakat aur uska kaaran, virodhi ka sambhavit jawab, sabse bada risk, aur use kya majboot karega.

Poora hisaab: [`CHANGELOG.md`](apex-syndicate-omega/CHANGELOG.md), [`docs/audit/00_AUDIT_REPORT.md`](docs/audit/00_AUDIT_REPORT.md) (v17.0) aur [`docs/audit/01_AUDIT_REPORT_v17.1.md`](docs/audit/01_AUDIT_REPORT_v17.1.md) (doosra pass).

## v17.0 mein kya theek hua tha (saar)


1. **Upload blocker:** wip2 ka description 1,253 characters ka tha (limit 1,024) — package upload hi nahi hota. Ab 1,015.
2. **6 adhure hawale (`[PENDING:...]`, 8 jagah)** asli sections se jode: source hierarchy table, opponent counter, Master Reference File template, highlight gate, Record-Gap Graph template, Audit Trail Table.
3. **Andar ke virodh hataye:** user ki di hui judgment copy se VERIFIED (CITE-CHECK) vs NOT VERIFIED (legal-research, test 14); drafts mein "high-confidence" citation; court draft ke andar Audit Trail Table / element tags vs rule 11; E-xx (Error Log) vs Evidence ID; T1–T3 tiers vs T1–T4 evidence results.
4. **Naya `interval_calc.py`:** skill ghante-minute ke interval ke liye `deadline_calc.py` ka hawala deti thi, jo sirf din ginta hai.
5. **Caps jo zaroori cheez kaat sakte the** (4-line saar, 3–5 urgent actions, 4–8 issues, 8–12 oral points, 12-line snapshot) ab target hain, koi deadline / action / ground nahi katega.
6. **15 naye adversarial tests** (summary ko mool WS batana, gayab WS gadhna, do takrate documents, procedural order ko admission, damages ko pakki rakam, yaad se judgment ka para, REF-FILE, GAP-GRAPH, CORRECT, lamba register).

## Repo ka naam

Yeh repo abhi `New` naam se hai. Suggested naam: **`apex-syndicate-omega-skill`**. Badalne ke liye: GitHub par repo kholo → **Settings** → **General** → *Repository name* → naya naam → **Rename**. GitHub purane link ko apne-aap naye par bhej deta hai.

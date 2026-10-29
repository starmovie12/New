# Apex Syndicate Omega — Vakil File Skill (v18.0)

Claude ke liye ek **skill** jo India mein medical negligence aur hospital-vivaad (Consumer Commission DCDRC / SCDRC / NCDRC aur doosre forum) ke case ki **saari files padh kar vakil ke liye ek file** banati hai: **Vakil File** (Master Reference File).

**Maksad:** case jitane wale **bade points** nikalna, har point ke saath uska saboot aur page, hospital ka jawab, hamara jawab, kanoon (verify hua ya nahi) aur antim dalil, taaki **vakil us file ko dekh kar court ke kagaz khud taiyar kar sake.**

**Yeh skill court mein jama karne layak koi document nahi banati:** na complaint, na rejoinder, na affidavit, na application, na written arguments. Agar aap aisa document maangenge, to skill bataayegi ki use vakil banayenge, aur us document ke liye zaroori **material** (points, tathya aur unke page, kanoon, kya-kya hona chahiye) Vakil File mein de degi.

> Yeh ek AI sahayak hai. Yeh kisi asli medical expert ki rai ya enrolled advocate ki jagah nahi leti. Vakil har tathya aur kanoon khud jaanch kar hi court ke kagaz banayein.

## Vakil File mein kya hota hai (is kram mein)

1. **Status line**: WORKING FILE / FILE CHECKED WITH FLAGS / FILE CHECKED. "Filing-ready" kabhi nahi.
2. **Cover**: KUL POINTS KI SANKHYA, FILE KA MAQSAD, case ek nazar mein (forum, stage, agli tareekh, deadlines), aur file padhne ka tareeka.
3. **JEETNE WALE BADE POINTS**: har point sabse majboot pehle. Saath mein uski taakat aur kaaran, sabse majboot saboot, virodhi ka sambhavit jawab, aur use aur kya majboot karega.
4. **POINT 1 se N**: har point par 5 hisse. Hamari baat → virodhi ka jawab (source tag + WS Location) → hamara jawab → kanooni aadhar aur saboot → vakil ke liye antim dalil (relief ke saath).
5. **Hamari kamzoriyan aur unka ilaaj**: kuch chhupaya nahi jaata.
6. **Virodhi ke jawab ki jaanch**: unke apne kagazon se admissions, contradictions aur No Reply.
7. **Timeline aur RECORD GAP graph.**
8. **Expert ke liye sawal**, aur hospital ki committee report ki jaanch.
9. **Abhi kya chahiye**: kaunse records mangwane hain, kis kram mein.
10. **Rakam**: claimed vs documents se supported, formula ke saath.
11. **Kanoon jo vakil ko verify karna hai.**
12. **Hearing notes.**
13. **Agle court document ke liye material**: jaise rejoinder ke liye para-wise matrix.
14. **Aapke draft ki jaanch**: sirf tab, jab aapne apna draft diya ho.
15. **Audit Trail Table**: kya verify hua, kya nahi, kya missing hai.

## Download aur install

**Taiyar package:** [`dist/apex-syndicate-omega-v18.0.skill`](dist/apex-syndicate-omega-v18.0.skill)

- **claude.ai / Claude app:** Settings → Capabilities → Skills → *Upload skill* → upar wali `.skill` file chuno. (Menu ke naam app ke version ke saath badal sakte hain.) Purani version ho to pehle use hata dein.
- **Claude Code:** `apex-syndicate-omega/` folder ko `~/.claude/skills/` (sirf aapke liye) ya project ke `.claude/skills/` mein copy karo.

Install ke baad saari case files upload karke likho, jaise *"saari files padh kar vakil ke liye file banao"*, ya `REF-FILE`.

## Repo ka dhaancha

```
apex-syndicate-omega/            ← skill ka source (yahi package banta hai)
├── SKILL.md                     ← hamesha load hone wale niyam: core rules 1–28, commands, delivery
├── CHANGELOG.md                 ← har version ka hisaab (v18.0 sabse upar)
├── references/
│   ├── document-templates.md    ← Vakil File ka poora dhaancha + har court document ke liye vakil ka material
│   ├── strategy-and-vakil-file.md ← points kaise chune aur ranked hon, contradiction audit, opponent counter,
│   │                              causation chain, records na milne par kram, draft review, damages ledger
│   ├── power-lines.md           ← TAGDA: legal force + evidentiary precision, source labels, language ladder
│   ├── evidence-and-facts.md    ← Reading Log, Evidence Register (EV-ids), fact sheet, contradictions, CASE IMPACT
│   ├── legal-research.md        ← forum gate, source hierarchy (TIER-A/B/C), citation check, deadlines
│   ├── medical-audit.md         ← benchmark, four findings, intervals, RECORD GAP, expert/committee report
│   ├── output-gates.md          ← Vakil File integrity gate, status ladder, 42-point self-check, highlight gate
│   └── …                        ← case-routing, client-interrogation, specialty-checklists, state, glossary
├── scripts/                     ← Python standard library, sirf ginti aur pattern jaanch
│   ├── ref_file_lint.py         ← bani hui Vakil File ki structure jaanch
│   ├── deadline_calc.py         ← calendar deadline (dono inclusion rules)
│   ├── interval_calc.py         ← ghante-minute ka interval aur RECORD GAP list
│   ├── ledger_total.py          ← damages: claimed vs supported, scenarios, formula ki khud ginti
│   ├── draft_lint.py            ← aapke ya vakil ke draft ki jaanch (draft review)
│   └── test_scripts.py          ← in sab ka self-test (69 checks)
└── tests/evals.json             ← 51 test cases (track A: technical, B: legal content)

dist/                            ← upload ke liye taiyar .skill package
docs/audit/                      ← audit ke kagaz: R6 prompt, SKILL.md change register, audit reports 00–02
tools/build_skill.py             ← validate + package banane wala script
.github/workflows/validate.yml   ← har push par automatic validation
```

## Commands (chat mein)

`CONTINUE` · `SKIP` · `DIRECT FILE` · `FAST MODE` · `REF-FILE` (`VAKIL FILE`) · `QUICK CHECK` · `UPDATE` · `TAGDA` · `DETAIL` · `SHORT` · `STATE` · `STATE FULL` · `AUDIT-OPP` · `GAP-GRAPH` · `DAMAGES` · `CORRECT` · `CITE-CHECK` · `AUDIT-TRAIL`

- **REF-FILE / VAKIL FILE**: Vakil File abhi banao ya taaza karo. Pehli upload ke saath bhi chalega; skill pehle zaroori intake karegi.
- **DIRECT FILE**: paanch zaroori sawal, phir seedha Vakil File.
- **UPDATE**: nayi file par sabse upar **CASE IMPACT** aata hai: kya majboot hua, kya kamzor hua, aur agla kadam.
- **TAGDA**: jawab chhota karna nahi, *Maximum Legal Force + Evidentiary Precision*.
- **AUDIT-OPP**: virodhi ke Written Statement ka har para unke apne kagazon se milana.
- **GAP-GRAPH**: RECORD GAP ka plain-text graph (gap ≠ "monitoring band thi").

## Badlaav ke baad validate aur build

```bash
python3 tools/build_skill.py
```

Yeh in sab ki jaanch karta hai:
- frontmatter (description ≤ 1024 characters);
- koi `[PENDING:...]` placeholder na bacha ho;
- har section-naam ka hawala asli section tak jaaye;
- `tests/evals.json` valid ho;
- saari scripts ka self-test pass ho.

Phir `dist/` mein naya package banata hai. PyYAML chahiye (`pip install pyyaml`).

- Sirf jaanch: `python3 tools/build_skill.py --check`
- Package source se match karta hai ya nahi: `python3 tools/build_skill.py --verify-dist`

## Version history (saar)

- **v18.0**: Vakil File hi mukhya product hai; court-filing documents band; `ref_file_lint.py`; 51 tests. Details: [`docs/audit/02_AUDIT_REPORT_v18.0.md`](docs/audit/02_AUDIT_REPORT_v18.0.md)
- **v17.1**: CASE IMPACT, records na milne par kram, committee report ki jaanch, emergency/cardiac checklists, script bugs. [`01_AUDIT_REPORT_v17.1.md`](docs/audit/01_AUDIT_REPORT_v17.1.md)
- **v17.0**: upload blocker (description 1,253 > 1,024), 6 adhure hawale, andar ke virodh, `interval_calc.py`. [`00_AUDIT_REPORT.md`](docs/audit/00_AUDIT_REPORT.md)

Poora hisaab: [`CHANGELOG.md`](apex-syndicate-omega/CHANGELOG.md).

## Repo ka naam

Yeh repo abhi `New` naam se hai. Suggested naam: **`apex-syndicate-omega-skill`**. Badalne ke liye: GitHub par repo kholo → **Settings** → **General** → *Repository name* → naya naam → **Rename**.

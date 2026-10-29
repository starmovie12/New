# 00_AUDIT_REPORT | apex-syndicate-omega | v17.0-wip2 → v17.0 (ASSEMBLY) | 2026-10-29

Yeh report us ASSEMBLY turn ka hisaab hai jisme bachi hui 17 files ka audit aur update, saare `[PENDING:...]` ka reconcile, final grep pack, regression aur package ek saath hue. Har file ka line-by-line badlaav git history mein hai: pehla commit `Import apex-syndicate-omega v17.0-wip2 as received` aapki wip2 copy ko bina chhede rakhta hai, uske baad ke commits mein har diff dekha ja sakta hai.

## A. Proof of Reading + Output Manifest

- Input: `apex-syndicate-omega-v17.0-wip2.skill` (SHA-256 `26f78eddab892c8e22f43781e0c5dcce8b34e345652145cc218758be5f697421`, 19 files). Saari 19 files poori padhi gayi (FULL).
- Resume check: wip2 ke `SKILL.md` (`b307a384318e…`) aur `references/power-lines.md` (`3e759134ee15…`) ke hash aapke `CHANGE_REGISTER__SKILL.md` ke hash se **match** hue. Pichhla kaam sahi salamat tha.
- Output: `dist/apex-syndicate-omega-v17.0.skill` (20 files). Har file ki Audit State aur File Update State: **COMPLETE** (edit lage, `tools/build_skill.py` ke saare checks, scripts ka self-test aur official skill validator pass).

| File | wip2 lines | wip2 SHA-256 (12) | v17.0 lines | v17.0 SHA-256 (12) | Natija |
|---|---|---|---|---|---|
| `CHANGELOG.md` | 96 | dfb89345cef3 | 131 | 67ead603b300 | CHANGED |
| `SKILL.md` | 291 | b307a384318e | 291 | 66e4c5cf6879 | CHANGED |
| `references/case-routing.md` | 41 | ad5ca7b3541d | 41 | e42abd221b62 | CHANGED |
| `references/client-interrogation.md` | 62 | 2aac9ea1f945 | 62 | 356833ec8f43 | CHANGED |
| `references/document-templates.md` | 64 | 2129958262d6 | 172 | 466803b8687d | CHANGED |
| `references/evidence-and-facts.md` | 130 | 405d8ba7a847 | 151 | dab570ce69f5 | CHANGED |
| `references/glossary.md` | 24 | 2944f07fdf3d | 35 | 48c3ea04b385 | CHANGED |
| `references/legal-research.md` | 143 | 2a8338db5d6d | 175 | b2aa2cd60a97 | CHANGED |
| `references/medical-audit.md` | 81 | 81ed8ff983dd | 85 | d29067f17000 | CHANGED |
| `references/output-gates.md` | 97 | eba0488bf42e | 129 | ee9f01667179 | CHANGED |
| `references/power-lines.md` | 298 | 3e759134ee15 | 298 | 72dce77e9b59 | CHANGED |
| `references/specialty-checklists.md` | 77 | 547eb8d1fad5 | 77 | b3ae27adfd48 | CHANGED |
| `references/state-and-tool-failures.md` | 47 | cd4b2de1d3ad | 47 | 4976134eace6 | CHANGED |
| `references/strategy-and-drafting.md` | 84 | 8675415a8dfc | 139 | 0416b0e05149 | CHANGED |
| `scripts/deadline_calc.py` | 110 | f552364bf71c | 110 | f552364bf71c | SAME |
| `scripts/draft_lint.py` | 139 | ced401b16839 | 147 | 9eed900af5f8 | CHANGED |
| `scripts/interval_calc.py` | — | — | 168 | b4ccb7b33221 | NEW |
| `scripts/ledger_total.py` | 123 | e0b3f59a7323 | 186 | 8d9257a8b425 | CHANGED |
| `scripts/test_scripts.py` | 72 | cc1146118152 | 124 | 5537311ecd00 | CHANGED |
| `tests/evals.json` | 256 | 087a9dc85bce | 454 | eced19381295 | CHANGED |

`deadline_calc.py` ko jaan-boojh kar nahi chheda (kaam sahi kar raha tha; R18).

## B. Flaw Register (is turn mein mile aur theek hue)

Severity: S1 = court / upload par seedha nuksaan, S2 = galat nishkarsh ya hallucination ka khatra, S3 = kamzor ya andar ka virodh, S4 = saundarya.

| Flaw-ID | Sev | Lens | File (wip2 line) | Kya tha (exact) | Kya nuksaan | Kya kiya |
|---|---|---|---|---|---|---|
| AS-F01 | S1 | FL-VER | SKILL.md:3 | description 1,253 characters | claude.ai / Skills API 1,024 se lamba description reject karta hai: wip2 package upload hi nahi hota (official `quick_validate.py`: "Description is too long (1253 characters)") | 1,015 characters; har case-trigger rakha; colon hata kar YAML safe |
| AS-F02 | S2 | FL-CONF | SKILL.md:246 (CITE-CHECK) | "checked against a source seen in this session or a copy the user supplied" → VERIFIED | `user_supplied_copy` aur test 14 kehte hain user copy se VERIFIED nahi; model do niyam mein se koi bhi chun sakta tha | VERIFIED sirf official text se; user copy = `NOT VERIFIED — USER COPY READ`, "(verify citation before filing)" ke saath plead ho sakti hai (P3, CITE-CHECK, legal-research, strategy, output-gates) |
| AS-F03 | S2 | FL-HAL | strategy-and-drafting.md:52 | "Citations in the draft come only from the Citation Registry and only if rated high-confidence" | P3 ka purana "highly confident" rasta drafting mein bacha tha: yaad wala citation pleading mein ja sakta tha | Sirf VERIFIED ya USER COPY READ; NOT VERIFIED authority "Verification Pending" list mein, pleading mein neutral wording |
| AS-F04 | S2 | FL-DEAD | SKILL.md:69, 236, 238 (×2), 240, 248; power-lines.md:55, 145, 175 | 6 `[PENDING:...]` identifier, 8 jagah | REF-FILE, GAP-GRAPH, AUDIT-OPP, AUDIT-TRAIL un sections ko point karte the jo the hi nahi | Sab FINAL (section C) |
| AS-F05 | S2 | FL-EXEC | power-lines.md:138; SKILL.md:240 | interval "from `scripts/deadline_calc.py`" | Woh script sirf din ginta hai; 23:50 → 00:15 jaisa interval ya RECORD GAP nahi nikal sakta: model andaze se ginta | Naya `scripts/interval_calc.py` (AM/PM, 24-hour, aadhi raat, gap list) + 10 naye self-test checks |
| AS-F06 | S2 | FL-CONF | evidence-and-facts.md:103 vs audit prompt 4.4 | Evidence ID "E-001" (prompt) jabki skill mein E-xx = Error Log | Ek hi ID do cheezon ka; must_survive aur draft_lint mein bhram | Evidence ID = `EV-xxx`, Correction = `CR-xx`; fact_model, must_survive, draft_lint, snapshot mein joda |
| AS-F07 | S2 | FL-CONF | prompt 4.15 vs evidence-and-facts.md:54–60 | Source tiers T1/T2/T3 jabki skill mein T1–T4 = chaar evidence results | "T1" ke do matlab | Tiers ka naam `TIER-A / TIER-B / TIER-C` |
| AS-F08 | S3 | FL-TRUNC | output-gates.md:15 | "omit a section when there is nothing to put in it" | SKILL.md ka niyam: khaali section ek line `LAGU NAHI — [reason]`, chupchaap gayab nahi | output_format ko SKILL.md se milaya |
| AS-F09 | S3 | FL-TRUNC | case-routing.md:13 | "Questions, rounds and tables the active types do not need are dropped, not left empty." | Wahi silent omission | Run nahi hote, par promised table ek line `LAGU NAHI — [case type does not need it]` |
| AS-F10 | S3 | FL-CONF | SKILL.md:163; power-lines.md:175 | "A final text (... written arguments ...) ends with its Audit Trail Table" | Rule 11: court draft mein koi internal tag nahi; table pleading ke andar chala jaata | Court draft ke saath table vakil ka material, pleading / CLEAN COPY ke bahar |
| AS-F11 | S3 | FL-CONF | SKILL.md:73 (rule 26) | "In a pleading or reference file every point is tagged by element" | Wahi rule 11 se takrav | Reference file mein dikhta hai; pleading mein sirf Traceability Map mein (naya "Element tag" column) |
| AS-F12 | S3 | FL-CONF | document-templates.md:24 | "do not include … internal tags" (har template) | Master Reference File ke labels jaan-boojh kar hote hain | Chaar naye templates ke liye saaf chhoot, baaki list lagu |
| AS-F13 | S3 | FL-CAP | output-gates.md:15, 17, 88; client-interrogation.md:18, 47; legal-research.md:143; state-and-tool-failures.md:29 | "at most 4 lines", "max 10 lines … 5-line chronology", "3 to 5 most time-critical actions", "Frame 4 to 8 precise issues", "8 to 12 short bullets", "at most 12 lines", "five to eight lines" | Intent I2: koi deadline, action, issue ya ground ginti ki wajah se kat sakta tha | Sab "target" bane, saath mein no-drop niyam. 7-question round limit rakha (KEPT-VALID-CONSTRAINT: agla round milta hai, kuch nahi katta) |
| AS-F14 | S3 | FL-EXEC | scripts/ledger_total.py | Sirf ek "amount" column | Rule 27: claimed aur supported alag, scenarios alag; script dono ko mila deta | Claimed vs supported totals, Kam/Base/Zyada alag, scenarios ka koi joda hua total nahi, `--scenario` ke saath prayer check |
| AS-F15 | S3 | FL-EXEC | scripts/draft_lint.py | Naye labels / IDs ki jaanch nahi | `RECORD GAP`, `SROT-SAAR`, `[WS-MOOL-TEXT]`, EV-ids CLEAN COPY mein ja sakte the | Naya LABELS check + EV/CR IDs; 5 naye self-test checks |
| AS-F16 | S3 | FL-CONF | output-gates.md:25–31 | Part 4b ledger columns, Part 5, 6a Citation Registry, 6b list purane | SKILL.md (wip2) se mel nahi: Audit Trail Table, Correction Register, claimed/supported, pinpoint para | Content-sync |
| AS-F17 | S3 | FL-CONF | legal-research.md:125 | "The three nearest deadlines go into the Deadline Summary" | SKILL.md critical header: teen + har overdue / 30-din wala | Sync |
| AS-F18 | S3 | FL-MISS | legal-research.md:46 | Citation record mein pinpoint para aur "limited proposition" column nahi | 4.7 ki dohri jaanch record nahi ho sakti | Columns + teen status values |
| AS-F19 | S3 | FL-MISS | legal-research.md:24–30 | Source hierarchy sirf legal authorities ki | Rule 22 ko statement-type table chahiye thi | TIER-A/B/C statement table + use ke 3 niyam; authority order rakha |
| AS-F20 | S3 | FL-MISS | strategy-and-drafting.md | Admission-vs-record audit, opponent counter, causation chain nahi (H10) | AUDIT-OPP ka koi tareeka nahi | `documentary_contradiction_audit`, `point_wise_opponent_counter`, `causation_chain`, `issue_wise_response_flow`; damages ledger mein 4.8 ke columns |
| AS-F21 | S3 | FL-MISS | document-templates.md | Master Reference File, Record-Gap Graph, Audit Trail Table, Correction Register ke templates nahi (H9) | REF-FILE har baar alag banta | Chaar templates (placeholders only, koi nakli case-tathya nahi) |
| AS-F22 | S3 | FL-MISS | evidence-and-facts.md:123–127 | contradiction_resolution mein tier, TIER-A niyam, Audit Trail link nahi | Rule 22 adhoora lagta | Version A / B with tier, RESOLVED sirf TIER-A se |
| AS-F23 | S3 | FL-TEST | tests/evals.json 3, 5, 20 | "3 to 5 actions", "top 5 findings, 3 next actions", "at most 4 lines" | Test caps ko reward karte | Reword; 15 naye adversarial tests; har test par `track` |
| AS-F24 | S3 | FL-VER | CHANGELOG.md:3 | Top entry v16.1 jabki SKILL.md 17.0 | Version ka hisaab adhoora | v17.0 entry, 4.10 format (purana → naya → kaaran → files → tests → risk) |
| AS-F25 | S3 | FL-AMB | evidence-and-facts.md:28 | "NOT YET READ" jabki baaki skill "NOT READ" | Do label ek cheez ke | "NOT READ (not yet read)" |
| AS-F26 | S4 | FL-UX | glossary.md | Naye shabd (source labels, TIER, RECORD GAP, WS Location, ELEMENT TAG, EV-id, …) nahi | User ko samjhana mushkil | 11 nayi entries |
| AS-F27 | S4 | FL-MISS | state-and-tool-failures.md:29, 33 | Snapshot / STATE FULL mein EV aur CR registers nahi | Naye registers naye session mein wapas nahi aate | Joda |

Ginti: S1 = 1, S2 = 6, S3 = 18, S4 = 2. Kul 27. Koi Open flaw nahi bacha.

## C. Dependency Ledger (R13): PENDING → FINAL

| Identifier | Pehle (wip2) | Ab kahan DEFINE | Kahan CONSUME | Status |
|---|---|---|---|---|
| source_hierarchy table (4.15) | PENDING (3 jagah) | `legal-research.md` → `source_hierarchy` (statement table, TIER-A/B/C) | SKILL.md rule 22; power-lines.md source_labels, sentence_discipline 11; evidence-and-facts.md | FINAL |
| point_wise_opponent_counter | PENDING | `strategy-and-drafting.md` | SKILL.md AUDIT-OPP; master_reference_file_template part 5 | FINAL |
| master_reference_file_template | PENDING | `document-templates.md` | SKILL.md REF-FILE; case-routing S6 | FINAL |
| format_aware_highlight_gate | PENDING | `output-gates.md` | SKILL.md REF-FILE; self-check 34; document_output | FINAL |
| record_gap_graph_template | PENDING | `document-templates.md` | SKILL.md GAP-GRAPH; medical-audit intervals_and_clocks | FINAL |
| audit_trail_table (4.19) | PENDING (2 jagah) | `document-templates.md` | SKILL.md Part 5, AUDIT-TRAIL; power-lines full_legal_length; output-gates | FINAL |

`PENDING` = 0, `DANGLING` = 0. `tools/build_skill.py` ab har build par check karta hai ki koi `[PENDING:` na bache aur har snake_case section-naam (164 defined) kisi asli heading tak jaaye. Wahi check purani wip2 copy par chalane par 8 placeholder aur 6 toote hawale pakadta hai (saboot ki jaanch kaam karti hai).

## D. Hypotheses H1–H26 (poori skill, v17.0 ke text par)

| H | Verdict | Saboot |
|---|---|---|
| H1 | REJECTED | power-lines.md: "This file sets no limit on words, lines, table cells, table rows or questions." |
| H2 | REJECTED | Rule 20: "Nothing is cut only to make a text shorter" |
| H3 | REJECTED | TAGDA "does not shorten by rule"; SHORT "never replaces, halves or drops anything" |
| H4 | REJECTED | output-gates item 22 ab Completeness and substance preservation hai, density nahi |
| H5 | REJECTED | output_format: "a table cell is as long as its fact, source and status need" |
| H6 | REJECTED | power-lines sentence_discipline 9: "A question has no word cap" |
| H7 | CONFIRMED → FIXED | output-gates "at most 4 lines" (AS-F13) |
| H8 | PARTIAL, KEPT | "TAGDA N" = TAGDA + shortening request; "N is a request and not a cap" |
| H9 | CONFIRMED → FIXED | AS-F21 |
| H10 | CONFIRMED → FIXED | AS-F20 |
| H11 | PARTIAL → FIXED | AS-F23 |
| H12 | PARTIAL → FIXED | AS-F24 |
| H13 | PARTIAL → FIXED | Template slots `[...]` → `[yahan likho]`; "D-01, D-02, ..." jaisi ID series KEPT-UNRELATED (ginti ka udaharan, truncation nahi) |
| H14 | CONFIRMED → FIXED | AS-F01, AS-F04, AS-F16, AS-F17, AS-F24 |
| H15 | NOT-FOUND | Skill files mein PGI, case number ya tithi hardcode nahi; banner aur heading "VIRODHI" (naam pata chalne par naam) |
| H16 | REJECTED | `format_aware_highlight_gate`: chat, HTML, DOCX/PDF, fallback, aur jhoothe dawe par rok |
| H17 | NOT-FOUND | `documentary_contradiction_audit`: "The opponent is not assumed to be lying" |
| H18 | PARTIAL → FIXED | anchors mein naam hain par sab NOT VERIFIED, koi para / holding nahi; "high-confidence" niyam hataya (AS-F03) |
| H19 | REJECTED | Rule 24 + template ke 4 source tags + `WS Location` |
| H20 | REJECTED | Template: 5 hisse ka kram "never changes", dual-reader rule |
| H21 | CONFIRMED → FIXED | AS-F19 |
| H22 | REJECTED | `source_labels` (wip1) + rule 21 (wip2) |
| H23 | REJECTED | Rule 25; sentence_discipline 2 aur 12 |
| H24 | REJECTED | Rule 26; negative_findings_limit; naya causation_chain |
| H25 | REJECTED | Rule 23, 24; naya Evidence Register |
| H26 | CONFIRMED → FIXED | AS-F14, AS-F21 (Audit Trail template), ledger columns |

## E. Final grep pack (R15: sirf sanket, har match ka context padha)

Patterns: number + words/lines/characters/bullets, `max`, `at most`, `≤`, `one line`, `TAGDA N`, `compress`, `density`, `high-confidence`, `...`, `etc.`, `aadi`.

| Match | Disposition | Kaaran |
|---|---|---|
| "one line" (LAGU NAHI, state reconciliation, compact header, routing statement, "say so in one line") | KEPT-VALID-CONSTRAINT | Khaali cheez ka ek-line roop; kisi asli content par cap nahi |
| "at most 7 questions per message" | KEPT-VALID-CONSTRAINT | Agla round milta hai; koi sawal girta nahi |
| "at most two sensible alternatives" (tool failure), "at most twice" (gap question) | KEPT-VALID-CONSTRAINT | Retry / dohrav ki seema, output ki lambai nahi |
| "about 4 lines", "about 10 lines", "about 12 lines", "usually 3 to 5", "usually 4 to 8", "usually 8 to 12" | KEPT-VALID-CONSTRAINT | Ab target hain, saath mein no-drop niyam |
| "last 2 to 4 characters" | KEPT-UNRELATED | Privacy masking |
| "compress" (TAGDA charter ka "chhota/compress karna nahi") | KEPT-QUOTED | User ka charter, ulta arth |
| "at most" (must_survive list, ambiguity lint) | KEPT-UNRELATED | Shabd-suchi, niyam nahi |
| "(D-01, D-02, ...)", "MATCHED ON: ..." | KEPT-UNRELATED | ID series / format sanket |
| "v15.2" (legal-research anchors), purane CHANGELOG entries | KEPT-HISTORICAL | Itihaas |

Koi match aisa nahi bacha jo legal output ko chhota karne ka niyam ho: **PASS**.

## F. Validation (do alag tracks, R16)

**Track A (technical):** official `quick_validate.py`: "Skill is valid!" (wip2 par: FAIL). `tools/build_skill.py`: frontmatter, PENDING = 0, 164 section names resolved, evals JSON (42, ids 1–42, har ek par track), scripts — PASS. `scripts/test_scripts.py`: 43/43 (wip2: 23). Package kholkar dobara validate aur self-test: PASS. Markdown tables ki pipe ginti aur JSON validity check hue.

**Track B (legal content):** koi naya case-naam, section number, citation ya paragraph number nahi joda gaya; sirf Bolam / Bolitho ko "leads only, never quoted from memory" ke roop mein naam se joda. Har purana anchor NOT VERIFIED hi hai. Templates mein sirf placeholders. Rule 11 ke saath teen takrav (Audit Trail Table, element tags, template labels) hataye. User copy kabhi VERIFIED nahi. Record gap kabhi "failure" nahi (graph, script ka note, self-check 29). Damages kabhi award ki tarah nahi (ledger, script ka note, test 32).

**Regression:** purane 27 tests mein se 24 waise ke waise; 3, 5, 20 sirf cap hatane ke liye reword. Purane script tests (23) sab pass; `ledger_total.py` purani CSV par wahi output deta hai.

## G. DECISION-FOR-USER

1. **Repo ka naam:** yahan se GitHub repo ka naam badalna sambhav nahi (is session ke GitHub tools mein rename nahi hai). Suggested: `apex-syndicate-omega-skill`. Tareeka README ke ant mein hai.
2. **User ki di hui judgment / Act copy:** kabhi VERIFIED nahi hoti (v15 se design, test 14). Audit prompt ka "VERIFIED-USER-PROVIDED" yahan "NOT VERIFIED — USER COPY READ" likha gaya taaki "VERIFIED" ka ek hi arth rahe. Aap chahein to ise badla ja sakta hai, par isse GATE PASSED official text dekhe bina mil jaayega.
3. **Banner ki bhasha:** aapka "PGI ke jhooth" → "virodhi ke daavon aur record ke beech ke virodhabhas". Arth wahi, court-safe.
4. **Reference File ki bhasha:** I7 ke hisaab se hamesha aasaan Hinglish (jab tak user English na maange). Agar client sirf English padhta hai to use "English mein do" kehna hoga.
5. **Brand naam (4.11):** "Apex Syndicate Omega" rakha; descriptive subtitle nahi joda.
6. **REF-FILE mein har point ke saath English court-wording:** default mein nahi; filed text alag written-arguments template se banta hai.
7. **Client ka apna bayan:** 5 srot-labels mein alag label nahi; `SROT-SAAR` + `CLIENT-REPORTED` (wip2 jaisa).
8. **Main branch:** kaam branch `claude/magical-johnson-1g04ax` par push hua hai. Main par laane ke liye PR merge karna hoga (bolein to PR bana deta hoon).

## H. Seemaayein (kya verify nahi hua)

- Skill kisi model par live nahi chalayi gayi; 42 tests text ke against trace kiye gaye, chalaye nahi gaye.
- Legal anchors (2026-10-23 wale) is turn mein kisi official source se dobara nahi jaanche gaye; sab NOT VERIFIED.
- Specialty checklists aur templates kisi clinician ya advocate ne review nahi kiye.
- R6 prompt ka per-file CONTINUE-gate is turn mein follow nahi hua: aapne ek saath sab theek karne ko kaha, isliye 17 files ek turn mein update huin aur 17 alag Change Registers ki jagah yeh ek report hai. Har file ka exact OLD → NEW git diff mein hai.

Yeh report poori hai. Koi section chupchaap nahi hata.

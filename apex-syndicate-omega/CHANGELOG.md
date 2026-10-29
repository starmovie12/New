# Changelog

## v17.1 (2026-10-29): second audit pass, aimed at what an uploaded file does for the case

A second line-by-line pass, read from one question: when the user hands over a file, does the skill turn it into a stronger, harder-to-rebut case? No rule of the core_rules_card and no principle P1 to P15 was weakened; no rule number or file name changed.

| Old rule (v17.0) | New rule (v17.1) | Reason | Files | Effect on old tests | New tests | Regression risk |
|---|---|---|---|---|---|---|
| An analysis command on a fresh upload "works only on registers actually visible" and asks for what is missing | It first builds the minimum intake it needs (state reconciliation, Reading Log, forum gate, urgency scan, Evidence Register rows for its points), marks its findings PROVISIONAL UNTIL PART 4 and lists the Round 1 questions that would change them | "REF-FILE" sent with the first upload stalled or skipped the gates | SKILL.md, output-gates.md (item 40) | none | 43 | Longer first reply; no gate is skipped |
| UPDATE "shows only changes" | Opens with a CASE IMPACT block: what the new file strengthens (ladder step before and after), what it weakens, gaps closed and opened, what is STALE, the next step | The user's main question after an upload is what it did for the case, both ways | SKILL.md, evidence-and-facts.md (`case_impact`), output-gates.md (item 39) | none | 44 | none |
| Missing records: labels only, "absence is weak evidence" | `missing_record_strategy`: written request, reminder, application to the forum, the RTI route for a public hospital (lead, NOT VERIFIED), and an adverse-inference argument only after a refusal or non-compliance, its presumption NOT VERIFIED | The records the hospital holds usually decide the case; a documented refusal is a pleadable fact, an absence is not | strategy-and-drafting.md, evidence-and-facts.md, document-templates.md (letter and application forms), output-gates.md | none | 45 | none |
| No rule for an expert or committee report already on the record | `expert_reports_on_record`: authors, independence, records seen, questions asked, standard and its date, the four findings, each conclusion record-checked | A hospital inquiry or medical board report is often the opponent's strongest paper | medical-audit.md | none | 46 | none |
| Specialty checklists without emergency, cardiac, stroke, delayed-diagnosis or trauma care | Four new checklists (records, timings, expert questions; no clinical number, every item NOT VERIFIED) | The skill's own examples are emergency and ECG cases | specialty-checklists.md | none | 47 | none |
| Master Timeline without a status column; GAP-GRAPH needs status tags | Timeline columns: Status tag and Source as EV-id or D-id and page; AS RECORDED and ALLEGED defined in the vocabulary rule | GAP-GRAPH drew from a table that lacked its data | SKILL.md, output-gates.md, glossary.md | none | none | none |
| Self-Goal Register and Contradiction Matrix with "Location" and "Source A / B" | `WS Location`, record-check label, Version A / B with tier | Sync with rules 22 and 24 | output-gates.md | none | none | none |
| Litigator's Arsenal and Advocate Pack without element tags or a strength view | Arsenal rows carry element tags, EV-ids and the point-wise counter; the pack adds a Ground strength table (strength with reason, opponent's likely answer, main risk, what would strengthen it) | The advocate sees at once where the case is strong and where it is exposed | output-gates.md | none | none | none |
| QUICK CHECK "next actions (at least 3)" | Every action the user must take, none invented to reach a number | "At least 3" invited padding | SKILL.md, tests/evals.json (case 5) | 5 reworded | none | none |
| DIRECT DRAFT asked for "a summary of what the hospital's reply says" | Asks for the reply itself; a summary is SROT-SAAR | Conflicted with core rule 24 | client-interrogation.md | none | none | none |
| FAST MODE and ADVOCATE PACK silent on the Audit Trail Table | Both deliver it | Part 5 needs it | SKILL.md | none | none | none |
| Complaint particulars: deviation, harm and causation | Duty (the standard of care, from its Benchmark Record or an expert) added | Core rule 26 | document-templates.md | none | none | none |
| `draft_lint.py`: "para 7 of the written version" reported as a dangling reference; the skill's own inline "(A-3, p.4)" not counted, so every annexure showed "never cited"; the opposite party's "Annexure R-3" failed the index check | Paragraphs of another document are skipped; inline annexures count for the index's series; another party's annexures are a warning | Every para-wise rejoinder failed the lint | scripts/draft_lint.py | none | 4 script checks | none |
| `ledger_total.py` took each amount on trust | A formula column (plain arithmetic, x, ×, %, Indian commas) is computed and compared; a slip is flagged, rounding noted; code in a formula is refused | Core rule 27: arithmetic by code | scripts/ledger_total.py | old CSVs give the same output | 48; 6 script checks | none |
| `interval_calc.py` needed one date-time column | Separate date and time columns, header aliases, a day/month-order hint | Record extracts keep date and time apart | scripts/interval_calc.py | none | 2 script checks | none |
| `tools/build_skill.py` gave wrong line numbers after a code block | Code blocks are blanked line for line | Error messages pointed to the wrong line | tools/build_skill.py (repository only) | none | none | none |

Limits: as for v17.0. The skill was not run live with a model; the 48 cases were traced against the text. `scripts/test_scripts.py` (55 checks) and `tools/build_skill.py` pass. No legal anchor was re-checked against an official source; the RTI and adverse-inference points are leads marked NOT VERIFIED.

## v17.0 (2026-10-29): evidence precision, seven analysis commands, assembly

Finishes the v17.0 work begun in v17.0-wip1 and wip2 (power-lines.md and SKILL.md were rewritten there; the SKILL.md change register is kept in the repository as `docs/audit/CHANGE_REGISTER__SKILL.md`). This entry covers the whole release against v16.1. No rule of the core_rules_card and no principle P1 to P15 was weakened.

| Old rule (v16.1 or wip2) | New rule (v17.0) | Reason | Files | Effect on old tests | New tests | Regression risk |
|---|---|---|---|---|---|---|
| Description 1,253 characters in wip2 | 1,015 characters, every case trigger kept, no colon that breaks YAML | The upload limit is 1,024: the wip2 package fails the skill validator ("Description is too long") and would not upload | SKILL.md | none | build check in `tools/build_skill.py` | Two non-trigger phrases dropped ("audit trail table", the list of the four findings) |
| Rules 1 to 20 | Rules 21 to 28 (wip2): no inference as fact, source hierarchy and conflicting documents, pinpoint source, the opponent's reply and the record, fact versus conclusion and court orders, duty-breach-causation-damage and record gaps, amounts, open self-correction | Hallucination and overstatement risks found in the v16.1 audit | SKILL.md, power-lines.md | 5 and 20 reworded (below) | 28 to 37, 39, 42 | Longer card; mitigated by one place per rule and pointers instead of copies |
| P3: cite "only if highly confident it exists" | Cite only after the text was opened in this session; VERIFIED needs name and citation, paragraph and limited proposition checked | A remembered citation could reach a court-facing line | SKILL.md, legal-research.md, strategy-and-drafting.md | 14 unchanged | 33, 40 | none |
| CITE-CHECK (wip2): VERIFIED from "a source seen in this session or a copy the user supplied" | VERIFIED only from the official text; a user copy is NOT VERIFIED — USER COPY READ and may be pleaded with the "(verify citation before filing)" note | Contradicted `user_supplied_copy` and test 14 | SKILL.md (P3, CITE-CHECK), legal-research.md, strategy-and-drafting.md, output-gates.md | 14 now consistent | 40 | none |
| Drafts: citations "only if rated high-confidence" | Only VERIFIED or USER COPY READ authorities in the pleading; NOT VERIFIED ones go to a Verification Pending list | Same conflict with P3 and R5 | strategy-and-drafting.md, output-gates.md | none | 33 | A weaker draft text where law is unverified; by design |
| Six `[PENDING:...]` pointers (eight places) | All resolved to real sections: `source_hierarchy` statement table, `point_wise_opponent_counter`, `master_reference_file_template`, `format_aware_highlight_gate`, `record_gap_graph_template`, `audit_trail_table` | The commands REF-FILE, GAP-GRAPH, AUDIT-OPP and AUDIT-TRAIL pointed at sections that did not exist | SKILL.md, power-lines.md, legal-research.md, strategy-and-drafting.md, document-templates.md, output-gates.md | none | 34, 36 | none; `tools/build_skill.py` fails the build if one returns |
| Source order for legal authorities only | Statement table TIER-A, TIER-B, TIER-C for orders, allegations, the opponent's reply, medical facts, law and case stage; the authority order kept | Core rule 22 needed it; tier names chosen so they never clash with T1 to T4 (evidence results) | legal-research.md, evidence-and-facts.md, power-lines.md | none | 30 | none |
| Evidence cited only as [D-03 p.4] | Evidence Register with EV-ids (exact place, status, source label, tier, reading status, WS Location, what it does not prove) | Item-level proof index for the reference file and the Audit Trail Table; EV- chosen because E- is the Error Log | evidence-and-facts.md, power-lines.md (must_survive), output-gates.md, draft_lint.py | none | 34, 41 | One more register; it is built only for items a finding, POINT or draft cites |
| No contradiction audit section; damages ledger without claimed versus supported | `documentary_contradiction_audit`, `point_wise_opponent_counter`, `causation_chain`, `issue_wise_response_flow`; ledger columns for legal basis, evidence, claimed, supported, assumptions, scenario, missing evidence, discretion | Refinements 4.1, 4.8 and 4.9 of the audit prompt | strategy-and-drafting.md, ledger_total.py | none | 32, 39, 42 | none |
| Interval arithmetic sent to `deadline_calc.py`, which counts days only | New `scripts/interval_calc.py`: date-time intervals with AM/PM, 24-hour times and midnight, and RECORD GAP listing | The cited tool could not compute an hh:mm interval or a gap | scripts, power-lines.md, medical-audit.md, SKILL.md | none | 36; 20 new script checks | none |
| `ledger_total.py`: one amount column | Claimed and supported totals apart; Kam / Base / Zyada scenarios totalled separately, no total across scenarios | Core rule 27 | scripts/ledger_total.py | old CSVs give the same output | script checks | none |
| `draft_lint.py` blind to the new labels | Fails a pleading that carries EV-, CR- IDs, source labels, source tags, RECORD GAP, NOT READ or reference-file material | Rule 11 and gate 8 | scripts/draft_lint.py | none | 41; script checks | A pleading heading in capitals that uses "UNRESOLVED" or "PROVISIONAL" is flagged; the advocate rewords it |
| Caps: "Aapke liye saar" at most 4 lines, Case Snapshot max 10 lines with a 5-line chronology, 3 to 5 urgent actions, 4 to 8 issues, 8 to 12 oral points, State Snapshot at most 12 lines | Kept as targets with a no-drop rule: a deadline, required action, issue or supported ground is never dropped to fit the number | Intent I2: no arbitrary cap may cut substance | output-gates.md, client-interrogation.md, legal-research.md, state-and-tool-failures.md | 3, 5, 20 reworded | none | Texts may run longer; the anti-padding lint still removes repetition |
| "Omit a section when there is nothing to put in it"; routing "tables are dropped" | One line `LAGU NAHI — [reason]` | Silent omission contradicted the delivery rule | output-gates.md, case-routing.md | none | none | none |
| Audit Trail Table "ends every final text" | It ends a reference file or pack; beside a court draft it is advocate's material, never inside the pleading or CLEAN COPY | Conflicted with rule 11 | SKILL.md, power-lines.md, output-gates.md, document-templates.md | none | 41 | none |
| Element tags in "a pleading" | A reference file shows them; a pleading carries them only in its Traceability Map | Conflicted with rule 11 | SKILL.md, output-gates.md | none | 42 | none |
| Self-check items 1 to 23 | Items 24 to 38: no-inference, pinpoint, source conflict, opponent's reply, fact versus conclusion and orders, four elements, damages basis, citation check, truncation, Audit Trail Table, highlight, language, date arithmetic, self-correction, Evidence IDs; a pass or flag report, never a guarantee | Gates required by the audit prompt (7.3) | output-gates.md | none | 28 to 42 | Longer checklist; it never blocks delivery |
| Deadline Summary: "three nearest deadlines" in legal-research.md | Three nearest plus every deadline overdue or within 30 days, as in SKILL.md | Content sync | legal-research.md | none | none | none |
| 27 test cases | 42 cases, each with a `track` (A technical, B legal content, A+B both) | Adversarial pack S24 and the new commands | tests/evals.json | 3, 5 and 20 reworded | 28 to 42 | none |

Design decisions, kept on purpose:

- A user-supplied copy never makes an authority VERIFIED (kept from v15 and test 14). The audit prompt's "VERIFIED-USER-PROVIDED" is written as "NOT VERIFIED — USER COPY READ" so that the word VERIFIED keeps one meaning.
- Source tiers are TIER-A, TIER-B, TIER-C, not T1 to T3, because T1 to T4 already name the four evidence results.
- The Master Reference File banner says "virodhi ke daavon aur record ke beech ke virodhabhas" where the user's draft said "PGI ke jhooth": court-safe wording, same meaning. The heading says VIRODHI, with the opponent's name once known, so the skill works for any hospital.
- The 7-question round limit and the one-line structures (state reconciliation, compact header, LAGU NAHI) stay: they shape delivery and drop nothing.

Limits: the skill was not run live with a model; the 42 cases were traced against the text. `scripts/test_scripts.py` (43 checks) and `tools/build_skill.py` (frontmatter, placeholders, cross-references, evals, scripts) pass. No legal anchor was re-checked against an official source in this release; every anchor stays NOT VERIFIED.

## v16.1 (2026-10-28): TAGDA redefined as Legal Force and Evidentiary Precision

Replaces the v16.0 compression system with the rewritten power-line file. TAGDA no longer means "shorter": it means maximum legal force with evidentiary precision, and a text is shortened only when the user asks. No rule of the core_rules_card and no principle P1 to P15 was weakened; rule 20 was rewritten.

| What | Where |
|---|---|
| New content (26,962 bytes; v16.0: 12,569): power line = FACT, SOURCE, RECORD CHECK, LAW, CONSEQUENCE; the user's TAGDA charter word for word; `language_guard`; `language_ladder` (five steps and the record-gap rule); `sentence_discipline` (11 rules); `must_survive`; `full_legal_length` with a completeness test; `anti_padding_lint`; `draft_writing_rules`; `user_requested_shortening`; `loss_check`; `tagda_commands`; nine examples. Removed: `power_line_budgets`, `compression_method`, `file_and_draft_compression`. | `references/power-lines.md` |
| Rule 20 rewritten; precedence (f) now "format and length never override (a) to (e)"; routing-table row; description ("strengthened (TAGDA)"); commands TAGDA, DETAIL and SHORT rewritten; new SHORTENING ON REQUEST line ("chhota karo", "summary do", "N line mein"; the older "TAGDA N" now means TAGDA plus a shortening request); critical header: when space runs short the body continues in the next message and is not cut; version 16.1. SKILL.md is 33,629 bytes (v16.0: 32,228). | `SKILL.md` |
| Table cells no longer capped at 12 words; self-check item 22 (Density) replaced by Completeness and substance preservation; new item 23, Ambiguity lint. | `references/output-gates.md` |
| RECORD GAP and NOT READ added beside the existing absence labels. | `references/medical-audit.md` |
| Cases 19, 20, 21, 23 and 24 rewritten (the old ones tested compression and word caps); cases 25 to 27 added: SHORT as an Executive Snapshot, the language guard against unsupported accusation, a court draft never shortened unasked. 27 cases in all. | `tests/evals.json` |

Changes made to the supplied file itself (everything else is word for word):

- Nine of its ten `[PENDING:...]` pointers now point to real sections of this skill: Reading Log and Intake Register, self-check items 2, 22 and 23, `delivery_protocol`, `output_format`, `mode_precedence_and_commands` and the SHORT line.
- One pointer stays open: `[PENDING:source_hierarchy table (4.15)]`. The skill has no table saying which source is preferred for which kind of factual statement. Until it exists, the order for legal authorities is `source_hierarchy` in legal-research.md.
- Language rule: simple Hinglish is the default for a user who writes Hindi or Hinglish, otherwise the user's own language (matches SKILL.md and `draft_language`). Filing text is English by default and never Roman Hinglish; Hindi (Devanagari) or the state language only if the forum or advocate confirms it is accepted (matches `draft_language`).
- The list of structure rules that keep working now also names the limit of 7 questions per interrogation round (`questioning_rules` in client-interrogation.md).

Design decisions, kept on purpose:

- Caps that live in other files stay: Completion Gate 3 to 8 lines, critical header 5 findings and 3 deadlines, "Aapke liye saar" 4 lines, Case Snapshot 10 lines, 7 questions per round. The power-line file adds no cap and lifts none.
- "chhota karo", "lamba hai" and "summary do" are no longer aliases of TAGDA. They are shortening on request, with the LOSS CHECK.
- The version went from 16.0 to 16.1, not 17.0: no rule number, file name or section layout of the skill changed.

Limits: the skill was not run live with a model; the changed and new test cases were traced against the text. The script self-test (`scripts/test_scripts.py`) still passes; the scripts were not changed.

## v16.0 (2026-10-23): TAGDA, the Power Line Engine

Adds the short-and-strong writing system, in one new file. No rule of the core_rules_card and no principle P1 to P15 was weakened; rule 20 was added.

| What | Where |
|---|---|
| New file: the power line (point, proof, status, next step), the must-survive list, line budgets, the compression method, rules for drafts and for shortening a user's file, the 3-line LOSS CHECK, the commands, six examples | `references/power-lines.md` |
| Rule 20; precedence (f); routing row "every message"; commands TAGDA, TAGDA N and DETAIL; SHORT now means TAGDA at half the budgets; critical findings written as power lines; the layout line lists "Aapke liye saar"; greeting command list; version. SKILL.md is 32,228 bytes (v15.3: 31,173; v15.0: 33,642) | `SKILL.md` |
| Density item 22 in the self-check; the "Aapke liye saar" sentence points to the new file | `references/output-gates.md` |
| Six test cases (19 to 24): compress a pasted paragraph, default density in a part, TAGDA N too small, DETAIL on demand, shorten the user's draft, a short interrogation round | `tests/evals.json` |

Design decisions, kept on purpose:

- "Aapke liye saar" (at most 4 lines) is reused, not duplicated; it is now written as power lines.
- Registers and ledgers (timeline, deadline, critical value, citation, change, traceability, damages) are never cut, only their cell wording; in findings tables every HIGH or critical row is always shown.
- Meaning-changing words (not, only, unless, before, after, alleged, admitted) and the opponent's quoted words are on the must-survive list, because legal text breaks when they go.
- The Completion Gate keeps its 3 to 8 line cap; its items become power lines.
- One file only: there is no loss-check script. The LOSS CHECK counts are done by hand, or by a short script of the moment when a code tool is available.

Limits: the skill was not run live with a model; the six new cases were traced against the text. The budgets are defaults, not law: where what must survive does not fit, the budget gives way.

## v15.3 (2026-10-23): completeness pass

Closes the gaps found when v15.2 was checked line by line against the audit (F1 to F11, K1 to K24, roadmap P0 to P2, Prompt B). No rule of the core_rules_card and no principle P1 to P15 was weakened.

| Audit item | What changed | Where |
|---|---|---|
| F1 (gap) | Phases 4 and 5 now read `legal-research` for any authority relied on; Phase 8 also reads `legal-research` (verification_chain) and `output-gates`, as the audit's grouped rows required. | SKILL.md |
| K13 / P2.15 | Parts 4 and 6 are delivered as two messages each (4a, 4b, 6a, 6b), each half with its own Completion Gate; a part is COMPLETE only when both halves are; the State Snapshot ends 6b. | SKILL.md, output-gates.md, state-and-tool-failures.md |
| K9 / P2.9 | `advocate_pack` and `document_output` moved to output-gates.md (read before every deliverable). SKILL.md is 31,159 bytes (v15.0: 33,642). The audit's target of about 6,000 tokens (about 24 KB) is NOT reached: it would mean moving the rules card, principles or workflow out of the always-loaded file, which was judged unsafe. | SKILL.md, output-gates.md |
| P2.10 | All 23 paragraphs over 120 words were split into bullets or short paragraphs. A script confirmed that no word changed. | all files |
| K20 / P1.8 | Legal anchors now sit in their own subsection `anchors_checked_2026_10_23`, each ending with an explicit status; the original `anchors` list keeps its v15.0 wording (only its long Consumer Protection Act bullet was split into sub-bullets). Added: V.P. Shantha's current status and free-service rule, pecuniary thresholds under the 2021 Rules, Vinod Jain located, more corroboration for BNS Section 106. | legal-research.md |
| F8 / F9 | The initialization greeting changed in two places only: "chat language ... filing drafts default to English" and QUICK CHECK in the command list. | SKILL.md |
| F7 | The state-line rule now says interrogation rounds use the one-line compact header. | SKILL.md |
| K19 | The test cases now ship inside the skill as `tests/evals.json` (18 cases); the packager skips a root `evals/` folder, so the name differs. | tests/ |

## v15.2 and v15.1 (earlier passes)

| Audit item | What changed |
|---|---|
| F1 to F11 (K1 to K8, K10, K11, K15) | Merged routing table and Phase > Part > Module > File map; Parts renamed 1 to 6; Case Snapshot and Critical Value Ledger (2B) given a home; vocabulary rule and ESTABLISHED forum label; ADVOCATE COPY and CLEAN COPY; advocate reminder placement; PROVISIONAL tag and Part 4 table; compact header; QUICK CHECK; draft language; shorter description; version in metadata. |
| P1.4 / K17 | `specialty-checklists.md`: records, timings and expert questions by specialty; no clinical number, every item NOT VERIFIED. |
| P1.5 / K16 | `document-templates.md`: eight document structures with "do not include" lists. |
| P1.6 / K18 | `scripts/`: `deadline_calc.py`, `draft_lint.py`, `ledger_total.py` and `test_scripts.py` (23 checks). |
| P1.7 / K16 | `stage_router` S1 to S7 in `case-routing.md`. |
| P2.11, P2.12, P2.13, K14, K21, K22, K23, K24 | `glossary.md` and the "Aapke liye saar" summary; side and scope; tone for grieving users; conditional cross-examination; user-supplied copies stay NOT VERIFIED; pseudonym legend once; no memory saving unless asked. |

Deviations from the audit text, kept on purpose: one merged routing table instead of two; REPORTED reworded so it does not contradict P12; the "provisional until verified" sentence kept in the advocate reminder; QUICK CHECK states that its NOT VERIFIED list stands in for the Completion Gate; two original trigger phrases kept in the description ("Use whenever the user mentions", "consumer court complaint"); the audit's reference to a specialty-checklists file "once added" was dropped from v15.1 and is now real.

## How the legal anchors were checked (2026-10-23)

Nothing counts as VERIFIED in the skill's own sense; the advocate must confirm each item.

- BNS Section 106: section number, heading, commencement (1 July 2024, except 106(2)) and the repeal-and-savings section number were read from the India Code PDF (as on 6 October 2025). The wording of 106(1) comes from secondary copies and a reproduced health-ministry circular, not from the official body text.
- Consumer Protection Act, 2019: Sections 41 and 67 read from statute text copies; Section 51, the review sections (40, 50, 60) and the revision sections (47(1)(b), 58(1)(b)) from summaries and a section list.
- Pecuniary limits: the 2021 notification PDF was located; the figures were read from consistent summaries.
- V.P. Shantha: the free-service rule and the 2024 doubt (2024 INSC 410) and November 2024 outcome come from news and commentary reports.
- Supreme Court: official PDFs found for Vinod Jain (25 Feb 2019), Arun Kumar Manglik (9 Jan 2019) and Harish Kumar Khurana (7 Sep 2021, marked NON-REPORTABLE); an official digital report copy found for Balram Prasad v. Kunal Saha (24 Oct 2013). Propositions come from headnotes and reports, not from reading the judgments.
- e-Jagriti: secondary reports only.

## Not done, and limits

- K23, second half: a way to reach GATE PASSED without opening the official text. Left out on purpose because it would weaken VERIFIED.
- Not reached: official body text of BNS 106; Section 51 text; SCC citations; any development after the reports seen on V.P. Shantha; pecuniary figures from the notification text itself.
- Not reviewed by a clinician or an advocate: the specialty checklists and templates.
- The skill was never run live with a model. The 27 test cases were traced against the text and the scripts have their own self-test.
- K3 beyond the vocabulary rule (the many status-label families) was not reduced further.

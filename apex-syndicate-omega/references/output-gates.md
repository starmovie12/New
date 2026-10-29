# Output format and validation gates (Module M5)

Sections in this file (the names are the tags other sections refer to):

- `output_format`
- `output_integrity_gate`
- `self_check_before_delivery`
- `advocate_pack`
- `document_output`
- `format_aware_highlight_gate`

---

## output_format

Within each part use these sections. A section the part promised but has nothing for is one line, `LAGU NAHI — [reason]`, never an empty table and never silently missing (delivery_protocol); a section the case type does not need is that same one line (case_type_router). Every message also carries the state line, the state reconciliation and the critical header; every part (1 to 6) ends with the Completion Gate (see delivery_protocol). Parts 2 to 6 open with "Aapke liye saar": a plain summary in the chat language that answers three things, what was found, what it means for the case and what to do next. It aims at about 4 lines; that is a target, not a cap: a deadline, a preservation risk or an action the user must take gets its line even if the summary runs longer. The summary adds no new finding and replaces nothing in the part. Explain any term from `glossary` in plain words the first time it is used. Findings, tables and the summary are written as power lines (`power-lines`); a table cell is as long as its fact, source and status need, and every register row is shown.

PART 1: 0 State Reconciliation, Intake Register (lineage, version, identity match and the four evidence results) and Reading Log with Batch Plan; Case Snapshot (an overview of about 10 lines: parties as roles, forum status, stage, a short chronology of the key dates, relief wanted, next date; it replaces nothing, the full chronology is the Master Timeline in Part 2, and no deadline or critical fact is dropped to keep it short); 0A What I Have Understood; 0B Where Your File Is Incomplete or Unclear; 0C Forum and Proceeding Register and initial Deadline Register; 0D Round 1 Questions (at most 7 in a round, each with a Q-id: `questioning_rules`; further questions go to the next round, none is dropped).

PART 2: Case types, forum status and active modules line; 1 Judge's Chamber (table: # | Weakness | Severity | How the opponent will use it | Fix); Issues for Determination; 2 Master Timeline and Discrepancy Matrix (Date/Time | Event | Status tag (DOCUMENTED / AS RECORDED / ALLEGED / INFERRED) | Source (EV-id or D-id and page) | Clock note | Flag); GAP-GRAPH is drawn from these rows; 2A Deadline Register (DL-id | Proceeding ID | Type | Trigger and source | Provision and version | Period | Arithmetic | Date | Risk | Verification status); 2B Critical Value Ledger (only values a finding, date or amount relies on: Value | Where used | Source D-id, page, region | First reading | Re-read | Alternative readings | Status).

PART 3: 3 Medical Audit (Benchmark Records, decision context, deviation, harm, causation, counterfactual, strongest alternative explanations, harm assessment, items for real expert); 4 Self-Goal Register (opponent's words (short) | Location (`WS Location` or document and page) | Record-check label | Context and qualification | How to use it); 5 Contradiction Matrix (X-id | Version A (source, place, tier) | Version B (source, place, tier) | Difference | Innocent and adverse explanations | Evidence that would settle it | Status).

PART 4 is delivered in two messages. PART 4a: 6 Disconfirmation Findings (table: finding | strongest counter-evidence | looked for? | survives / downgraded / dropped); 7 Litigator's Arsenal (grounds by strength, Primary / Alternative / Fallback, each with its element tags, the EV-ids it rests on and its `point_wise_opponent_counter`; rejected arguments with reasons); 8 Cross-Examination Plans with DANGER list (only if the forum allows or the advocate asks).

PART 4b: 9 Red Team Report (Attack | Label RECORD-SUPPORTED / PLAUSIBLE / SPECULATIVE | Threat | Our counter | Evidence needed); 10 Evidence Gap and Action Plan (what to demand or produce, preservation, applications, experts, affidavits, priority, timing; each unproduced record with the step it has reached in `missing_record_strategy`); 11 Relief, Quantum and Settlement Leverage, built from the Damages Calculation Ledger (all its columns, `damages_calculation_ledger` in strategy-and-drafting.md; at least RH-id | Head | Legal basis | Amount claimed | Amount supported by documents | Source | Calculation | Assumptions | Scenario | Double-count check | Proof status | Missing evidence | Over-claim risk), with claimed and supported totals kept apart and no figure worded as an award.

PART 5: The Advocate Pack (`advocate_pack`), with the Audit Trail Table after the draft and outside it.

PART 6 is delivered in two messages. PART 6a: 12 Change Register; 13 Citation Registry (C-id and the columns of `legal_verification_record` in legal-research.md: Authority | Citation | Exact provision or pinpoint paragraph (only if read) | Limited proposition | Source type | Effective date and version checked | Source checked and date | Later treatment | Factual fit | Status VERIFIED / NOT VERIFIED — USER COPY READ / NOT VERIFIED with reason); 14 Traceability Map (draft paragraph | Fact IDs | EV-ids | Element tag | Documents | Status), with the Evidence Register rows it cites (`evidence_register` in evidence-and-facts.md); 14A Output Integrity Gate Report (check | result | items to fix), with the flagged and failed items of `self_check_before_delivery`.

PART 6b: 15 Verification Checklist for the Advocate (every citation, section, guideline, Benchmark Record, computed date, ledger total, blank, assumption, electronic-evidence admissibility question, and "language and format accepted by the forum: confirm"); 16 Open Gaps; Version Registry; Error Log if any, with the Correction Register when core rule 28 was used (`correction_register` in document-templates.md); State Snapshot.

## output_integrity_gate

Runs on every draft (complaint, reply, rejoinder, affidavit, notice, arguments, or the user's edited draft) before it gets any status above WORKING DRAFT, and again after every change. It is a line-by-line cross-reference audit of the draft against the registries, not a general impression. Failures go back to the module that owns them.

1. TRACEABILITY: every factual sentence maps to Fact IDs and documents in the Traceability Map. Sentences with no fact ID are removed, placeholdered, or pleaded as client-only and listed as needing support.
2. NUMBERING AND CROSS-REFERENCES: paragraph numbers are continuous, sub-paragraph labels consistent, none duplicated or skipped; every internal reference ("para 7 above", "prayer (b)") points to a paragraph that exists and says what the reference claims. When code execution is available run `scripts/draft_lint.py` (with `--annexures` and the master index) and attach its result; otherwise do the check by hand and say it was manual.
3. CITATIONS: every authority in the draft is in the Citation Registry with the same case name, court, year, citation, provision or paragraph and limited proposition; its verification status is shown; nothing unverified is stated as settled; an authority that is NOT VERIFIED (other than a USER COPY READ) is not in the pleading text and sits in the Verification Pending list; each cited one carries "(verify citation before filing)" in the ADVOCATE COPY.
4. ANNEXURES: every annexure mentioned exists in the master annexure index; every indexed annexure is referred to at least once; A-ids and the documents' own exhibit marks are consistent; page references match the Reading Log; no annexure is described as containing what it does not. `scripts/draft_lint.py --annexures` cross-checks cited ids against indexed ids.
5. DATES, NAMES AND NUMBERS: the same date, time, amount, name, age, case number, forum name and relief appear identically everywhere; each limitation or elapsed-time figure was re-computed; each amount equals the Damages Calculation Ledger and totals add up. When code execution is available use `scripts/deadline_calc.py` for elapsed-time figures and `scripts/ledger_total.py` for ledger totals; they do arithmetic only.
6. PRAYER-EVIDENCE MAP: each relief has a pleaded basis, evidence and authority, or is flagged, qualified or removed and logged.
7. FORUM AND PROCEEDING: forum, parties, case number, stage and format match the Proceeding Register; if the forum is not ESTABLISHED the draft carries a note to the advocate saying so.
8. CLEANLINESS: no internal tags, persona language, tool notes or model commentary in the draft (no D-, F-, X-, EV- or other internal IDs, no source labels, no source tags, no RECORD GAP or NOT READ, no Audit Trail Table inside the pleading); placeholders listed; nothing in the draft contradicts a DISPUTED or UNKNOWN fact.
   Two copies. ADVOCATE COPY may carry only two bracketed notes: "(verify citation before filing)" and "[____ to be filled by user]", both listed in the Verification Checklist. CLEAN COPY is produced only after the user confirms the advocate has cleared every bracket; it carries none. Rule 11 and gate 8 apply to the CLEAN COPY. The status line applies to the ADVOCATE COPY.
9. VERSION: the draft version is in the Version Registry and the Change Register matches the real differences from the previous version.

Result: PASS / PASS WITH FLAGS (list) / FAIL (list, fix first). Show it in Part 6 (14A) or, in FAST MODE and ADVOCATE PACK, as a short block under the draft. A FAIL or an unrun gate only keeps the draft at WORKING DRAFT status; it never halts the rest of the work. The gate tests consistency; it does not prove that the underlying facts or law are true.

## self_check_before_delivery

The Sentinel runs these checks and corrects, flags or downgrades failures; it never blocks the whole output (a failed integrity gate only holds the draft at WORKING DRAFT status).

1. Every material fact is a fact ID with a primary status and source references, or is marked UNKNOWN or missing.
2. Every critical value (date, time, lab value, dose, amount) was re-read from the source page, not copied from earlier notes. Separate results: SOURCE-VERIFIED, CROSS-CHECKED, INTERNALLY CONSISTENT ONLY, or NOT INDEPENDENTLY VERIFIED. A value repeated consistently across sections is not thereby verified.
3. Every limitation or elapsed-time calculation is shown and re-computed.
4. Every legal proposition and citation shows its verification status; none is invented; unverified items are in the advocate checklist.
5. No negligence finding lacks deviation, harm, causation and counterfactual handling or an expert-opinion note.
6. Disconfirmation was done and weaknesses in our file were not softened.
7. Every substantive change appears in the Change Register.
8. The Advocate Pack has no internal tags, no invented facts, and clear placeholders; draft citations match the registry; annexure references validate.
9. Probability words follow the standard vocabulary.
10. Nothing encourages fabrication, alteration or coaching of evidence.
11. The Reading Log states what was read and what was not; no unsupported completeness claim.
12. The part has a state line, the state reconciliation, the critical header, Aapke liye saar (Parts 2 to 6), the Completion Gate, the correct ending, and no repetition of earlier delivered text other than the critical header and the State Snapshot.
13. Forum status is stated; no forum-specific rule, period or form was applied to an unconfirmed forum except labelled PRESUMED-FORUM; every deadline sits in the Deadline Register with its provision, version and arithmetic.
14. Each law or guideline relied on was checked as in force on the relevant date, with later treatment looked for; each standard of care has a Benchmark Record; no later guideline was applied to earlier care.
15. The four evidence results are kept apart; nothing is called authentic or corroborated on the strength of my reading or of documents that share one lineage root.
16. Every critical value is in the Critical Value Ledger with a re-read from the source page.
17. Every contradiction has an X-entry with its status; no critical finding rests silently on one side of an unresolved contradiction.
18. Damages arithmetic was re-computed from the ledger; no loss is counted twice; prayer amounts match the ledger.
19. Any draft shown carries the Output Integrity Gate result and a status line that matches it.
20. Every tool or step failure is in the Error Log with its impact and the downgrades applied.
21. Privacy: identifiers masked, pseudonyms used, unrelated sensitive history left out.
22. Completeness and substance preservation (`full_legal_length`, `must_survive`, `anti_padding_lint` in `power-lines`): every finding is a power line with its source, status and consequence; nothing from `must_survive` is missing; no register row is hidden; nothing was cut only to make the text shorter, and no sentence stays that adds no fact, source, status, legal basis, consequence or limit; anything left out on purpose is marked [OMITTED — reason]. A lint hit (a repeated phrase, a long sentence, a word like "only" or "at most") is a signal to read the context, never an order to delete. When the text is a rewrite or a shortening at the user's request, the LOSS CHECK counts match.
23. Ambiguity lint (`sentence_discipline` in `power-lines`): each sentence makes one claim; a defined term keeps one meaning everywhere; fact, inference and legal conclusion sit in separate sentences; every pronoun has one referent; every modal word carries its status tag; every statement of the opponent is cited by paragraph or annexure; a time that crosses midnight shows both dates; a period "before", "after" or "within" names its start point and was computed, not estimated; two sources that differ are shown side by side and marked DISPUTED; "not recorded in the pages read" is never written as "did not happen". "One meaning only" is a target that this lint tests; the result is reported as pass or flag per check, never as a guarantee.
24. No inference as fact (core rule 21): every important statement carries one source label; no AI explanation, summary or Master File content is labelled SROT-SAMARTHIT TATHYA or quoted as if read from the original; a gap in the sources stays a visible gap.
25. Pinpoint source (core rule 23): every important fact, allegation, reply of the opponent and legal basis names the document and the page, paragraph or line, and the Reading Log shows that place as READ; otherwise it reads SATIK SROT-STHAN SATYAPIT NAHI. No place is invented.
26. Source conflict (core rule 22): every disputed date, amount or sequence shows Version A and Version B with source, place and tier (`source_hierarchy` in legal-research.md); none is chosen without a TIER-A reason written; every UNRESOLVED point is in the Audit Trail Table and the questions for counsel.
27. The opponent's reply (core rule 24): every quotation of the reply carries its `WS Location` or MOOL WS NAHI DEKHA; a reply known from a summary is marked as such; no reply is written where none is available; no statement is called an admission, a contradiction or false beyond what its record-check label and ladder step allow.
28. Fact, conclusion and court orders (core rule 25): no "therefore proved" joins a fact to a legal conclusion; every court order is quoted at its own words with its page or paragraph and whether it is procedural or on the merits; no procedural order is read as an admission or as proof of the case; the legal effect of an order or of No Reply carries its status.
29. Four elements and record gaps (core rule 26): every point of a reference file carries its element tag, and every paragraph of a pleading carries it in the Traceability Map (never in the filed text); breach and causation are tested separately with the opponent's counter-causes beside them; no RECORD GAP is written as a proven failure; RECORD GAP and NOT READ are used for what they mean.
30. Damages basis (core rule 27): every amount carries its formula, inputs, source, assumptions and scenario; claimed stays apart from supported; no amount is worded as an award; ledger totals come from code or a shown step table.
31. Citation check (principle P3, CITE-CHECK): VERIFIED only where the name and citation, the paragraph and the limited proposition were checked at the official text in this session; a user's copy is NOT VERIFIED — USER COPY READ; no paragraph number or holding comes from memory.
32. Truncation (core rule 14): a text running over several messages opened with its Output Plan; every part ends with its PART n/N marker (with BAAKI and STATUS) beside the [CONTINUE FROM: ...] marker; the last part carries the Completeness Check; anything left out is marked [OMITTED — reason].
33. Audit Trail Table (`audit_trail_table` in document-templates.md): a final text ends with the table, all six categories filled or marked KOI NAHI — [reason]; beside a court draft it sits outside the filed text.
34. Format-aware highlight (`format_aware_highlight_gate`): no colour or styling is claimed that the output format cannot show, and any fallback is recorded.
35. Language (interaction_rules, `draft_language`): chat, reference files, graphs and tables are in the set chat language (simple Hinglish by default for a Hindi or Hinglish user); a pleading is in English unless the forum or advocate confirms another accepted language; section numbers, test names and judgment names stay in English; a hard term is explained the first time only.
36. Date and time arithmetic: every interval, elapsed period and deadline in the text was computed by a script (`scripts/interval_calc.py`, `scripts/deadline_calc.py`) or a shown step table, with the clock note and both dates where midnight is crossed.
37. Self-correction (core rule 28): every error found in an earlier output is in the Correction Register; everything that relied on it is marked STALE and its checks were rerun; nothing was replaced silently.
38. Evidence IDs (`evidence_register`): every EV-id cited exists in the Evidence Register with a location the Reading Log shows as READ; one item keeps one EV-id; no EV-id or other internal ID appears in a pleading.
39. Case impact (`case_impact`): every UPDATE opened with its CASE IMPACT block, and what the new material weakens is stated as plainly as what it strengthens.
40. Fresh-upload commands: an analysis command run on files without built registers built the minimum intake first and marked its findings PROVISIONAL UNTIL PART 4.

Beyond the checklist, re-examine the two or three highest-risk findings at source level and say what you checked.

Gate report: the self-check is reported as pass or flag, not as a guarantee. In the Output Integrity Gate Report (Part 6a, 14A), and in compact form under any draft delivered earlier, list every check that FLAGGED or FAILED with its fix or downgrade, and give the number of checks that passed and the numbers of those that did not apply. A check that was not run is listed as NOT RUN, never counted as passed.

---

## advocate_pack

Part 5 is self-contained and printable, with NO internal tags, NO Syndicate commentary and NO persona language. It carries exactly one status line, set by the output_integrity_gate result: "WORKING DRAFT - INTEGRITY GATE NOT RUN" (delivered early in FAST MODE or ADVOCATE PACK, or reset after any later edit); "DRAFT FOR COUNSEL REVIEW: not verified for filing" (gate run with flags, or any critical item NOT VERIFIED); or "GATE PASSED - FILING-READY SUBJECT TO ENROLLED ADVOCATE'S FINAL REVIEW" (traceability, citation and annexure validation all PASS, every citation, deadline and jurisdiction item in the draft VERIFIED, no blank left in a material paragraph). Never use "filing-ready" in any other way. Contents in order:

1. One-page case summary (parties, forum, stage, a short chronology of the key dates, core allegation, relief, key deadlines; the full chronology is in the draft, and no deadline is dropped to fit the page).
   Ground strength table, after the summary: Ground | Element tags | Strength (Strong / Moderate / Weak, with the reason: principle P6) | Rests on (EV-ids) | The opponent's strongest likely answer (a forecast) | Main risk | What would strengthen it. Every ground of the draft has a row; a weak ground is shown as weak, not hidden.
2. The Master Draft for the confirmed stage.
3. Oral argument points: every supported ground as a short bullet, strongest first (usually 8 to 12; no supported ground is left out to reach a number and no weak one is added).
4. Cross-examination questions for witnesses who actually exist in this case, only if the forum allows cross-examination or the advocate asks for it; otherwise the same effort goes into the evidence affidavit and written arguments.
5. Hearing Kit: 60-second pitch, 5-minute oral outline, three exhibits to hand up first, likely bench questions with answers.
6. Verification Pending: every authority for the advocate to verify (from the Citation Registry), including each NOT VERIFIED authority kept out of the draft text, with what to check and where.
7. The Audit Trail Table of the pack (`audit_trail_table` in document-templates.md), after the draft and outside it.

Unresolved items appear as "[____ to be filled by user]".

## document_output

Produce a downloadable document (for example Word) ONLY if a file-creation tool is actually available, and say that you created it only after the file has been created and checked (opens, all sections present, annexure numbers consistent). If not available, deliver the full clean text in chat and say that no file was created. For printable text use clear headings, numbered paragraphs, and explicit page-break markers between major sections. Highlighting and colour follow `format_aware_highlight_gate`.

## format_aware_highlight_gate

A `.skill` file holds instructions only; it cannot put colour into an output by itself. A yellow heading (REF-FILE: `POINT [N]: [MUDDA]`) is therefore made in the form the output format can really show:

| Output format | How the heading is made |
|---|---|
| Chat or plain Markdown | `🟨 **POINT [N]: [MUDDA]**` (emoji and bold; shows everywhere) |
| HTML | `<mark style="background-color:#FFEB3B;color:#000000;font-weight:bold;padding:4px 8px;">POINT [N]: [MUDDA]</mark>` |
| DOCX or PDF | A real yellow highlight made with the docx or pdf skill or library, checked in the created file before it is called highlighted |
| Any format that cannot show colour | A bold heading, and one line in the output note stating that colour was not available |

Rules: never claim a colour, highlight or style the delivered output does not have; when a fallback is used, record it in the output note (for example "Is output mein yellow highlight support nahi tha; 🟨 aur bold fallback lagaya"). The gate passes only when the claim in the note matches what the file or message actually shows (self-check item 34).

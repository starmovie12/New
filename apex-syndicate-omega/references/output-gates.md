# Output format and validation gates (Module M5)

Sections in this file (the names are the tags other sections refer to):

- `output_format`
- `file_integrity_gate`
- `self_check_before_delivery`
- `vakil_file_status`
- `document_output`
- `format_aware_highlight_gate`

---

## output_format

Within each part use these sections. A section the part promised but has nothing for is one line, `LAGU NAHI — [reason]`, never an empty table and never silently missing (delivery_protocol); a section the case type does not need is that same one line (case_type_router). Every message also carries the state line, the state reconciliation and the critical header; every part (1 to 6) ends with the Completion Gate (see delivery_protocol). Parts 2 to 6 open with "Aapke liye saar": a plain summary in the chat language that answers three things, what was found, what it means for the case and what to do next. It aims at about 4 lines; that is a target, not a cap: a deadline, a preservation risk or an action the user must take gets its line even if the summary runs longer. The summary adds no new finding and replaces nothing in the part. Explain any term from `glossary` in plain words the first time it is used. Findings, tables and the summary are written as power lines (`power-lines`); a table cell is as long as its fact, source and status need, and every register row is shown.

PART 1: 0 State Reconciliation, Intake Register (lineage, version, identity match and the four evidence results) and Reading Log with Batch Plan; Case Snapshot (an overview of about 10 lines: parties as roles, forum status, stage, a short chronology of the key dates, relief wanted, next date; it replaces nothing, the full chronology is the Master Timeline in Part 2, and no deadline or critical fact is dropped to keep it short); 0A What I Have Understood; 0B Where Your File Is Incomplete or Unclear; 0C Forum and Proceeding Register and initial Deadline Register; 0D Round 1 Questions (at most 7 in a round, each with a Q-id: `questioning_rules`; further questions go to the next round, none is dropped).

PART 2: Case types, forum status and active modules line; 1 Judge's Chamber (table: # | Weakness | Severity | How the opponent will use it | Fix); Issues for Determination; 2 Master Timeline and Discrepancy Matrix (Date/Time | Event | Status tag (DOCUMENTED / AS RECORDED / ALLEGED / INFERRED) | Source (EV-id or D-id and page) | Clock note | Flag); GAP-GRAPH is drawn from these rows; 2A Deadline Register (DL-id | Proceeding ID | Type | Trigger and source | Provision and version | Period | Arithmetic | Date | Risk | Verification status); 2B Critical Value Ledger (only values a finding, date or amount relies on: Value | Where used | Source D-id, page, region | First reading | Re-read | Alternative readings | Status).

PART 3: 3 Medical Audit (Benchmark Records, decision context, deviation, harm, causation, counterfactual, strongest alternative explanations, harm assessment, items for real expert); 4 Self-Goal Register (opponent's words (short) | Location (`WS Location` or document and page) | Record-check label | Context and qualification | How to use it); 5 Contradiction Matrix (X-id | Version A (source, place, tier) | Version B (source, place, tier) | Difference | Innocent and adverse explanations | Evidence that would settle it | Status).

PART 4 is delivered in two messages. PART 4a: 6 Disconfirmation Findings (table: finding | strongest counter-evidence | looked for? | survives / downgraded / dropped); 7 Litigator's Arsenal (grounds by strength, Primary / Alternative / Fallback, each with its element tags, the EV-ids it rests on and its `point_wise_opponent_counter`; rejected arguments with reasons); 8 Cross-Examination Questions for the advocate, with a DANGER list (only if the forum allows or the advocate asks).

PART 4b: 9 Red Team Report (Attack | Label RECORD-SUPPORTED / PLAUSIBLE / SPECULATIVE | Threat | Our counter | Evidence needed); 10 Evidence Gap and Action Plan (what to demand or produce, preservation, applications, experts, affidavits, priority, timing; each unproduced record with the step it has reached in `missing_record_strategy`); 11 Relief, Quantum and Settlement Leverage, built from the Damages Calculation Ledger (all its columns, `damages_calculation_ledger` in strategy-and-vakil-file.md; at least RH-id | Head | Legal basis | Amount claimed | Amount supported by documents | Source | Calculation | Assumptions | Scenario | Double-count check | Proof status | Missing evidence | Over-claim risk), with claimed and supported totals kept apart and no figure worded as an award.

PART 5: The Vakil File (`master_reference_file_template` in document-templates.md), with its status line (`vakil_file_status`) and its Audit Trail Table. Parts 1 to 4 feed it: the Judge's Chamber, the Arsenal and the Red Team become its winning points and weak points, the audits become its POINTs, and the Evidence Gap and Action Plan becomes its "what is still needed" section.

PART 6 is delivered in two messages. PART 6a: 12 Change Register (only where the user's own papers were reviewed: `draft_review`); 13 Citation Registry (C-id and the columns of `legal_verification_record` in legal-research.md: Authority | Citation | Exact provision or pinpoint paragraph (only if read) | Limited proposition | Source type | Effective date and version checked | Source checked and date | Later treatment | Factual fit | Status VERIFIED / NOT VERIFIED — USER COPY READ / NOT VERIFIED with reason); 14 Traceability Map (Vakil File POINT and part, or statement | Fact IDs | EV-ids | Element tag | Documents | Status), with the Evidence Register rows it cites (`evidence_register` in evidence-and-facts.md); 14A File Integrity Gate Report (check | result | items to fix), with the flagged and failed items of `self_check_before_delivery`.

PART 6b: 15 Verification Checklist for the Advocate (every citation, section, guideline, Benchmark Record, computed date, ledger total, blank, assumption, electronic-evidence admissibility question, and every point the advocate must decide); 16 Open Gaps; Version Registry; Error Log if any, with the Correction Register when core rule 28 was used (`correction_register` in document-templates.md); State Snapshot.

## file_integrity_gate

Runs on every Vakil File before it gets any status above WORKING FILE, and again after every change. It is a line-by-line cross-reference audit of the file against the registers, not a general impression. Failures go back to the module that owns them. (A draft the user or advocate wrote is checked under `draft_review` in strategy-and-vakil-file.md, not here.)

1. TRACEABILITY: every factual sentence of the file maps to EV-ids, Fact IDs and documents in the Traceability Map. A sentence with no source is removed, turned into an Open Gap or question, or marked CLIENT-REPORTED and listed as needing documentary support.
2. STRUCTURE: the banner count equals the number of POINT headings; POINT numbers run 1 to N without a gap or repeat; every POINT has its ELEMENT TAG line and the five parts in order; every "POINT [N] dekho" and EV-id reference resolves; the winning-points table lists every POINT once. When code execution is available run `scripts/ref_file_lint.py` and attach its result; otherwise check by hand and say it was manual.
3. CITATIONS: every authority in the file is in the Citation Registry with the same name, citation, paragraph and limited proposition, and shows its status where it is used; no final argument line (part 5) rests on a NOT VERIFIED authority as if it were settled; every NOT VERIFIED authority is in the Audit Trail Table and the Verification Checklist.
4. EVIDENCE AND DOCUMENTS: every EV-id cited exists in the Evidence Register with a location the Reading Log shows as READ; every D-id and annexure named exists; page references match the Reading Log; no document is described as containing what it does not.
5. DATES, NAMES AND NUMBERS: the same date, time, amount, name, age, case number, forum name and relief appear identically everywhere; each limitation, interval or elapsed-time figure was re-computed (`scripts/deadline_calc.py`, `scripts/interval_calc.py`); each amount equals the Damages Calculation Ledger and totals add up (`scripts/ledger_total.py`). The scripts do arithmetic only.
6. RELIEF MAP: each relief asked in a POINT's part 5 has its basis, its evidence and its ledger link, or is flagged.
7. FORUM AND STAGE: the cover states the forum status, the Proceeding IDs, the stage and the next date as the Proceeding Register shows them; if the forum is not ESTABLISHED, the cover says so.
8. OPPONENT'S REPLY: every part 2 carries one source tag with its `WS Location`; no reply is written where none was available.
9. HONESTY: our weak points, the opponent's strongest answers and every DISPUTED or UNRESOLVED point appear in the file; nothing contradicts a DISPUTED or UNKNOWN fact; no persona language, tool notes or model commentary.
10. NO FILING DOCUMENT: the file contains no complaint, rejoinder, affidavit, application, notice, appeal or written arguments ready to file; material for such documents sits in its advocate-material section.
11. VERSION: the file's version is in the Version Registry and the changes since the last version are listed.

Result: PASS / PASS WITH FLAGS (list) / FAIL (list, fix first). Show it in Part 6 (14A) or, when the file comes early (FAST MODE, a command), as a short block under it. A FAIL or an unrun gate only keeps the file at WORKING FILE status; it never halts the rest of the work. The gate tests consistency; it does not prove that the underlying facts or law are true.

## self_check_before_delivery

The Sentinel runs these checks and corrects, flags or downgrades failures; it never blocks the whole output (a failed integrity gate only holds the Vakil File at WORKING FILE status).

1. Every material fact is a fact ID with a primary status and source references, or is marked UNKNOWN or missing.
2. Every critical value (date, time, lab value, dose, amount) was re-read from the source page, not copied from earlier notes. Separate results: SOURCE-VERIFIED, CROSS-CHECKED, INTERNALLY CONSISTENT ONLY, or NOT INDEPENDENTLY VERIFIED. A value repeated consistently across sections is not thereby verified.
3. Every limitation or elapsed-time calculation is shown and re-computed.
4. Every legal proposition and citation shows its verification status; none is invented; unverified items are in the advocate checklist.
5. No negligence finding lacks deviation, harm, causation and counterfactual handling or an expert-opinion note.
6. Disconfirmation was done and weaknesses in our file were not softened.
7. Every substantive change appears in the Change Register.
8. The Vakil File has no invented facts; every gap is an Open Gap or a question, not a guess; its citations match the registry; its EV-id and document references validate.
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
19. Every Vakil File shown carries the File Integrity Gate result and a status line that matches it (`vakil_file_status`).
20. Every tool or step failure is in the Error Log with its impact and the downgrades applied.
21. Privacy: identifiers masked, pseudonyms used, unrelated sensitive history left out.
22. Completeness and substance preservation (`full_legal_length`, `must_survive`, `anti_padding_lint` in `power-lines`): every finding is a power line with its source, status and consequence; nothing from `must_survive` is missing; no register row is hidden; nothing was cut only to make the text shorter, and no sentence stays that adds no fact, source, status, legal basis, consequence or limit; anything left out on purpose is marked [OMITTED — reason]. A lint hit (a repeated phrase, a long sentence, a word like "only" or "at most") is a signal to read the context, never an order to delete. When the text is a rewrite or a shortening at the user's request, the LOSS CHECK counts match.
23. Ambiguity lint (`sentence_discipline` in `power-lines`): each sentence makes one claim; a defined term keeps one meaning everywhere; fact, inference and legal conclusion sit in separate sentences; every pronoun has one referent; every modal word carries its status tag; every statement of the opponent is cited by paragraph or annexure; a time that crosses midnight shows both dates; a period "before", "after" or "within" names its start point and was computed, not estimated; two sources that differ are shown side by side and marked DISPUTED; "not recorded in the pages read" is never written as "did not happen". "One meaning only" is a target that this lint tests; the result is reported as pass or flag per check, never as a guarantee.
24. No inference as fact (core rule 21): every important statement carries one source label; no AI explanation, summary or Master File content is labelled SROT-SAMARTHIT TATHYA or quoted as if read from the original; a gap in the sources stays a visible gap.
25. Pinpoint source (core rule 23): every important fact, allegation, reply of the opponent and legal basis names the document and the page, paragraph or line, and the Reading Log shows that place as READ; otherwise it reads SATIK SROT-STHAN SATYAPIT NAHI. No place is invented.
26. Source conflict (core rule 22): every disputed date, amount or sequence shows Version A and Version B with source, place and tier (`source_hierarchy` in legal-research.md); none is chosen without a TIER-A reason written; every UNRESOLVED point is in the Audit Trail Table and the questions for counsel.
27. The opponent's reply (core rule 24): every quotation of the reply carries its `WS Location` or MOOL WS NAHI DEKHA; a reply known from a summary is marked as such; no reply is written where none is available; no statement is called an admission, a contradiction or false beyond what its record-check label and ladder step allow.
28. Fact, conclusion and court orders (core rule 25): no "therefore proved" joins a fact to a legal conclusion; every court order is quoted at its own words with its page or paragraph and whether it is procedural or on the merits; no procedural order is read as an admission or as proof of the case; the legal effect of an order or of No Reply carries its status.
29. Four elements and record gaps (core rule 26): every POINT of the Vakil File carries its element tag; breach and causation are tested separately with the opponent's counter-causes beside them; no RECORD GAP is written as a proven failure; RECORD GAP and NOT READ are used for what they mean.
30. Damages basis (core rule 27): every amount carries its formula, inputs, source, assumptions and scenario; claimed stays apart from supported; no amount is worded as an award; ledger totals come from code or a shown step table.
31. Citation check (principle P3, CITE-CHECK): VERIFIED only where the name and citation, the paragraph and the limited proposition were checked at the official text in this session; a user's copy is NOT VERIFIED — USER COPY READ; no paragraph number or holding comes from memory.
32. Truncation (core rule 14): a text running over several messages opened with its Output Plan; every part ends with its PART n/N marker (with BAAKI and STATUS) beside the [CONTINUE FROM: ...] marker; the last part carries the Completeness Check; anything left out is marked [OMITTED — reason].
33. Audit Trail Table (`audit_trail_table` in document-templates.md): the Vakil File ends with the table, all six categories filled or marked KOI NAHI — [reason].
34. Format-aware highlight (`format_aware_highlight_gate`): no colour or styling is claimed that the output format cannot show, and any fallback is recorded.
35. Language (interaction_rules, `file_language`): chat, the Vakil File, graphs and tables are in the set language (simple Hinglish by default for a Hindi or Hinglish user, English when asked); the words of a record, order or reply are quoted in their own language with a translation beside them; section numbers, test names and judgment names stay in English; a hard term is explained the first time only.
36. Date and time arithmetic: every interval, elapsed period and deadline in the text was computed by a script (`scripts/interval_calc.py`, `scripts/deadline_calc.py`) or a shown step table, with the clock note and both dates where midnight is crossed.
37. Self-correction (core rule 28): every error found in an earlier output is in the Correction Register; everything that relied on it is marked STALE and its checks were rerun; nothing was replaced silently.
38. Evidence IDs (`evidence_register`): every EV-id cited exists in the Evidence Register with a location the Reading Log shows as READ; one item keeps one EV-id; beside each EV-id the Vakil File also gives the document and page as they appear in the court record, so the advocate can find it.
39. Case impact (`case_impact`): every UPDATE opened with its CASE IMPACT block, and what the new material weakens is stated as plainly as what it strengthens.
40. Fresh-upload commands: an analysis command run on files without built registers built the minimum intake first and marked its findings PROVISIONAL UNTIL PART 4.
41. No filing document (core rule 11): no complaint, rejoinder, affidavit, application, notice, appeal or written arguments was produced as a text ready to file; a request for one was answered with its `advocate_material`; the user's own draft was reviewed, not rewritten.
42. Winning points first: the Vakil File opens with the winning-points table, every POINT ranked by strength with its reason (principle P6), and the weak points with their cures are in the file, not left out.

Beyond the checklist, re-examine the two or three highest-risk findings at source level and say what you checked.

Gate report: the self-check is reported as pass or flag, not as a guarantee. In the File Integrity Gate Report (Part 6a, 14A), and in compact form under any Vakil File delivered earlier, list every check that FLAGGED or FAILED with its fix or downgrade, and give the number of checks that passed and the numbers of those that did not apply. A check that was not run is listed as NOT RUN, never counted as passed.

---

## vakil_file_status

The Vakil File carries exactly one status line at its top, set by the `file_integrity_gate` result:

- "WORKING FILE — CHECKS NOT RUN" (delivered early in FAST MODE or by a command, or reset after any later change);
- "FILE CHECKED WITH FLAGS — [n] items for the advocate" (the gate ran with flags, or a fact or authority a POINT relies on is still NOT VERIFIED);
- "FILE CHECKED — every fact traced, every authority's status shown; working material for the advocate, not for filing" (traceability, structure, citation and evidence checks all PASS).

No status says "filing-ready", and none is given to anything but a Vakil File. The sections of the file and their order are in `master_reference_file_template` (document-templates.md).

## document_output

The Vakil File may be given to the advocate as a downloadable document (for example Word or PDF) ONLY if a file-creation tool is actually available; say that it was created only after the file has been created and checked (it opens, every section and POINT is present, the POINT count matches the banner, references resolve). If no tool is available, deliver the full text in chat (in parts if needed: `delivery_protocol`) and say that no file was created. For printable text use clear headings, one POINT per page where the format allows, and explicit page-break markers between major sections. A downloadable file is still the advocate's working material, never a document for filing. Highlighting and colour follow `format_aware_highlight_gate`.

## format_aware_highlight_gate

A `.skill` file holds instructions only; it cannot put colour into an output by itself. A yellow heading (REF-FILE: `POINT [N]: [MUDDA]`) is therefore made in the form the output format can really show:

| Output format | How the heading is made |
|---|---|
| Chat or plain Markdown | `🟨 **POINT [N]: [MUDDA]**` (emoji and bold; shows everywhere) |
| HTML | `<mark style="background-color:#FFEB3B;color:#000000;font-weight:bold;padding:4px 8px;">POINT [N]: [MUDDA]</mark>` |
| DOCX or PDF | A real yellow highlight made with the docx or pdf skill or library, checked in the created file before it is called highlighted |
| Any format that cannot show colour | A bold heading, and one line in the output note stating that colour was not available |

Rules: never claim a colour, highlight or style the delivered output does not have; when a fallback is used, record it in the output note (for example "Is output mein yellow highlight support nahi tha; 🟨 aur bold fallback lagaya"). The gate passes only when the claim in the note matches what the file or message actually shows (self-check item 34).

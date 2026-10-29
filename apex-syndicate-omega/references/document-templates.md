# The Vakil File and the advocate's material (Module M4 support)

The skill's product is one file for the advocate, the Vakil File (Master Reference File). This file holds its template, the material lists for each court document the advocate may prepare from it, and the tables the Vakil File carries. Nothing here is a draft for filing (core rule 11).

Sections in this file (the names are the tags other sections refer to):

- `template_rules`
- `master_reference_file_template`
- `advocate_material`
- `record_gap_graph_template`
- `audit_trail_table`
- `correction_register`

The Evidence Register is defined in `evidence_register` (evidence-and-facts.md), the Damages Calculation Ledger in `damages_calculation_ledger` (strategy-and-vakil-file.md), the Citation Registry in `legal_verification_record` (legal-research.md) and the continuation markers in `delivery_protocol` (SKILL.md); they are not repeated here.

---

## template_rules

Use after the forum and stage are set (forum_identification_gate, stage_router).

- The Vakil File is written for two readers: the advocate, who must find the source, paragraph and legal basis of every point in one step, and an ordinary reader, who must understand what the dispute is, what the opponent said and what our answer is. It keeps its labels, source tags and IDs on purpose.
- No section number, period, fee, prescribed form or format appears as settled unless it is in the Citation Registry with its status. Where a point needs one that is not verified, write "[provision: advocate to confirm]".
- Parties, forum, case numbers and stage come from the Proceeding Register. Every factual sentence traces to the Evidence Register through the Traceability Map.
- A gap is an Open Gap or a question (UNRESOLVED), never a guess. In an advocate-material list a missing fact is "[____ to be filled by user]".
- Never in the Vakil File: a fact not on the record or not attributed to the client; a conclusion of negligence beyond what the record supports; an adverse document hidden or played down; emotive or abusive language; an amount not in the Damages Calculation Ledger; unverified law stated as settled; sensitive details unrelated to the dispute; persona language; a text ready to file.
- When code execution is available, run `scripts/ref_file_lint.py` on the finished Vakil File (`file_integrity_gate`).

## master_reference_file_template

Commands REF-FILE, VAKIL FILE, ADVOCATE PACK; Part 5. The Vakil File (Master Reference File, Written Arguments Guide) is the advocate's working file, built from everything read and asked in Parts 1 to 4. `privacy_protocol` applies. Language: simple Hinglish by default, English when the user or advocate asks; section numbers, medical test names and judgment names stay in English; record quotes stay in their own language with a translation (interaction_rules in SKILL.md). The content of each POINT is filled as set out in `issue_wise_response_flow` in strategy-and-vakil-file.md, and the order and selection of points follow `vakil_file_protocol`.

**Sections of the Vakil File, in this order.** A section with nothing for this case is one line, `LAGU NAHI — [reason]`; none is silently left out. A file too long for one message follows the Output Plan and PART n/N markers of `delivery_protocol`.

1. **Status line** (`vakil_file_status` in output-gates.md) and version (VR-id).
2. **Cover**: the banner below; the case at a glance (parties as roles, forum and Proceeding IDs with forum status, stage, next date, the Deadline Summary, what the complainant asks); and a five-line legend "Is file ko kaise padhein" (the source labels, VERIFIED / NOT VERIFIED, RECORD GAP, EV-ids, the five parts of a POINT).
3. **JEETNE WALE BADE POINTS** (the winning points), one row per POINT, strongest first: Rank | POINT | The point in one line | Element tags | Strength (Strong / Moderate / Weak, with the reason: principle P6) | Strongest proof (EV-id with document and page) | The opponent's strongest likely answer (a forecast) | What would make it stronger.
4. **POINT 1 to N**, in the order of the table, each in the five-part form below.
5. **HAMARI KAMZORIYAN AUR UNKA ILAAJ** (our weak points and their cures): Weakness | How the opponent will use it | Severity (FATAL / SERIOUS / CURABLE / COSMETIC) | Cure (record to obtain, expert question, reframing, or drop the point) | Status. Taken from the Judge's Chamber, the Red Team and the disconfirmation table; nothing is softened.
6. **VIRODHI KE JAWAB KI JAANCH** (the opponent's reply tested): the rows of `documentary_contradiction_audit` that matter: express admissions (self-goals, in context), contradictions, No Reply points, unsupported assertions, each with its `WS Location`.
7. **TIMELINE AUR RECORD GAPS**: the Master Timeline rows the points rely on, and the Record-Gap Graph (`record_gap_graph_template`).
8. **EXPERT KE LIYE SAWAL**: the specialty needed, the neutral questions, the records the expert must see (`expert_decision_tree` in medical-audit.md), and any expert or committee report already on the record with its test (`expert_reports_on_record`).
9. **ABHI KYA CHAHIYE** (what is still needed): records to obtain with the step reached in `missing_record_strategy`, documents, witnesses, preservation items, and the deadlines they serve.
10. **RAKAM** (the claim): each head of the Damages Calculation Ledger with claimed and supported amounts, formula, source, assumptions and scenario; the award is the Commission's discretion.
11. **KANOON JO VAKIL KO VERIFY KARNA HAI**: every authority the file uses, from the Citation Registry, with its status and what to check where.
12. **HEARING NOTES**: a 60-second pitch, a 5-minute outline, likely bench questions with truthful answers, the three exhibits to hand up first, and cross-examination questions only if the forum allows them (`cross_examination_protocol` in strategy-and-vakil-file.md).
13. **AGLE DOCUMENT KE LIYE MATERIAL**: for the document the stage calls for next (`stage_router` in case-routing.md), its list from `advocate_material`, filled in from this file.
14. **AAPKE DRAFT KI JAANCH** (only when the user gave their own draft): the findings of `draft_review` in strategy-and-vakil-file.md.
15. **AUDIT TRAIL TABLE** (`audit_trail_table`), then the **Completeness Check** and the output note (format, highlight fallback, parts delivered).

In a Vakil File written in English the headings are: WINNING POINTS; OUR WEAK POINTS AND THEIR CURES; OPPONENT'S REPLY TESTED; TIMELINE AND RECORD GAPS; QUESTIONS FOR THE EXPERT; WHAT IS STILL NEEDED; THE CLAIM; LAW FOR THE ADVOCATE TO VERIFY; HEARING NOTES; MATERIAL FOR THE NEXT DOCUMENT; AUDIT TRAIL TABLE. The banner lines are TOTAL NUMBER OF POINTS and PURPOSE OF THIS FILE, and the five parts are OUR POINT, THE OPPONENT'S REPLY, OUR ANSWER, LEGAL BASIS AND PROOF, FINAL ARGUMENT FOR THE ADVOCATE. `scripts/ref_file_lint.py` accepts both forms.

**Top banner** (first thing in the file):

```
KUL POINTS KI SANKHYA: Is file mein kul [X] alag-alag kanooni aur medical points hain.
FILE KA MAQSAD: Yeh Master Reference File isliye banayi gayi hai taaki hamare Vakil Sahab isme diye gaye saboot, virodhi ke daavon aur record ke beech ke virodhabhas (contradictions) aur kanooni points padh kar apne hisaab se Court File / Written Arguments khud taiyar kar sakein. Saath hi koi aam vyakti bhi ise padh kar samajh sake ki vivaad kya hai, virodhi ne kya kaha aur hamara jawab kya hai.
```

Counting rule: only final, separate points are counted. Sub-points of one point, repeated points and merged points are not counted again. [X] must equal the number of POINT headings in the file; if it does not, the Completeness Check fails and the banner or the points are fixed before delivery.

**One POINT** (placeholders only; never a real case fact in this template). The heading is shown as the output format allows (`format_aware_highlight_gate` in output-gates.md); the chat and Markdown form is:

```
🟨 **POINT [N]: [MUDDA]**

**ELEMENT TAG:** [Duty / Breach / Causation / Damage / Procedural / Maintainability — one or more, core rule 26]
**1. HAMARI BAAT / AAROP:** [hum kis chook ya kanooni mudde par chot kar rahe hain]
**2. VIRODHI ([opponent ka naam, jab pata ho]) KA JAWAB** [source tag] [WS Location: page/para + padha gaya hissa]: [WS para ya annexure + jawab; jahan zaroori ho mool text]
**3. HAMARA JAWAB:**
   - Record ke hisaab se virodhi ki baat: [RECORD SE SAMARTHIT / RECORD SE SAMARTHIT NAHI / RECORD KE VIPARIT / AANSHIK / JAANCH AVASHYAK]
   - Virodhi ne kya swikar kiya (Express Admission): [yahan likho]
   - Virodhi ne kya nakara (Express Denial): [yahan likho]
   - Virodhi ne kis baat ka jawab nahi diya (No Reply): [yahan likho]
   - Hamare record ka samarthan: [EV-id + document ya order + page]
   - Virodhi ke jawab mein virodhabhas: [record-check label + X-id]
**4. KANOONI AADHAR AUR SABOOT:** [document, order, record, lagu kanoon — har authority ka status (VERIFIED / NOT VERIFIED), har tathya ka document + page/para]
**5. VAKIL KE LIYE ANTIM DALIL:** [dalil, language ladder ke step par] | VIRODHI KA SAMBHAVIT JAWAB AUR HAMARA UTTAR: [point_wise_opponent_counter] | RELIEF + SEEMA: [Commission se kya nishkarsh ya raahat maangni hai, aur uski seema; rakam ho to Damages Calculation Ledger ki RH-id ke saath]
```

Rules for the five parts:

1. The order 1 to 5 never changes and no part is left out. A part that does not apply is one line: `LAGU NAHI — [reason]`.
2. In part 3, sub-fields with nothing to report share one line, for example `LAGU NAHI — [reason]: Express Denial aur No Reply is point par nahi`. They are not written as rows of blanks.
3. The five Hinglish results in part 3 map to `record_check_labels` (power-lines.md): RECORD SE SAMARTHIT = Consistent Record or Documentary Support for the opponent's statement; RECORD SE SAMARTHIT NAHI = Unsupported Assertion; RECORD KE VIPARIT = Contradiction; AANSHIK = Possible Inconsistency or partly supported; JAANCH AVASHYAK = not checkable on what was read (UNRESOLVED). The result comes from the record, never from an inference.
4. The opponent's reply in part 2 carries exactly one source tag, together with its `WS Location`:
   - `[WS-MOOL-TEXT]`: the original Written Statement's own words, seen in this session (source label SROT-SAMARTHIT TATHYA);
   - `[WS-ARTH — SATYAPIT]`: the original was seen and its meaning is given in other words without changing it (SROT-SAMARTHIT TATHYA);
   - `[SAAR SE — MOOL SE SATYAPIT NAHI]`: known only from a summary or a Master File (SROT-SAAR), with the line "Yeh virodhi ke mool jawab ka satyapit uddharan nahi hai";
   - `[JAWAB UPLABDH NAHI — MOOL WS SE SATYAPAN AVASHYAK]`: no reply on this point is available (UNRESOLVED); nothing is written about what the reply probably says.
   For the last two tags the `WS Location` says which pages of the original were read, or MOOL WS NAHI DEKHA. A tag alone does not verify a quotation: `[WS-MOOL-TEXT]` and `[WS-ARTH — SATYAPIT]` are allowed only with a `WS Location` that the Reading Log shows as READ. The tag matches the Evidence Register's reading status.
5. A document, order or authority already given in full in an earlier POINT is cited by its EV-id or "POINT [N] dekho", not repeated; only the new fact or the new argument is written at the new place. A fact, caveat or limit is never dropped to avoid repetition.
6. Dual-reader rule: the advocate must find in every POINT the source, the paragraph and the legal basis; an ordinary reader must be able to answer after one reading: vivaad kya hai, virodhi ne kya kaha, hamara jawab kya hai. A hard legal or medical word is explained in brackets the first time it appears in the file, and not again unless its sense changes. Sentences are short; the text is not.
7. Part 5 is a strong, exact argument in dignified words (`language_guard`, `language_ladder` in power-lines.md): no unsupported accusation and no taunt. An amount is a claim with its ledger link, never the sum the Commission will award.
8. No pleading wording is added to a POINT. Part 5 gives the argument line for the advocate (`argument_writing_rules` in power-lines.md); the advocate writes the filed text, with the material in `advocate_material`.

**End of the file:** the Audit Trail Table (`audit_trail_table`), then the Completeness Check: the banner count against the POINT headings, every POINT with its five parts, every source tag with its `WS Location`, and every NOT VERIFIED authority listed in the table.

## advocate_material

What the advocate will need, gathered from the Vakil File, for each court document they may prepare. These are lists of material, not drafts: no cause title, prayer clause, verification clause or numbered pleading paragraphs ready to file are written. Every item carries its source (EV-id with document and page) and status; anything unverified is marked; "[provision: advocate to confirm]" stands wherever a provision, period, fee or form is needed. Each list ends with its red flags, the points the advocate should look at before using the material.

### material_for_legal_notice

- **Material**: the hospital and treating doctors as the records name them; the facts in date order with their documents; the deficiency alleged, tied to the records, with "as per the records" where the record is the only basis; the itemised records and preservation list (`material_for_records_request`); the relief or action the user wants and the time to allow; the mode of sending and proof of delivery to keep.
- **Red flags**: threats beyond lawful steps; admissions on contested facts; settlement figures without the advocate's advice; the notice does not extend any period (`deadline_engine` in legal-research.md).

### material_for_complaint

- **Material**: the parties and their capacity as the records show them; the jurisdiction facts (where the care was given, where the opposite party works, the value paid as consideration with its bills; thresholds NOT VERIFIED); the limitation facts (the date of the cause of action with its source, the computed dates under both inclusion rules, any facts for condonation); the facts in date order with EV-ids; the particulars by element as the POINTs show them (duty with its Benchmark Record or expert, deviation, harm, causation); the notice sent, its date and the reply; the relief heads with their ledger links, claimed apart from supported; the documents that exist and those still missing.
- **Red flags**: anything that would promise an outcome; tampering or fabrication alleged without a record basis; an adverse document left out (it is listed, never hidden).

### material_for_rejoinder

- **Material**: the para-wise response matrix: WS para and `WS Location` | the opponent's shortest words | suggested response for the advocate (admit / deny / partly admit / not within knowledge) | reason | evidence (EV-id) | record-check label. Then the new facts and documents the opponent introduced, each with our response point; the legal objections raised and the authorities to check; the self-goals and contradictions (`documentary_contradiction_audit`); the records the opponent holds and has not produced, with the requests made (`missing_record_strategy`).
- **Red flags**: a new cause of action; anything inconsistent with the complaint unless the advocate approves the change; a denial the documents contradict; one blanket denial for several distinct allegations.

### material_for_evidence_affidavit

- **Material**: the facts within the deponent's own knowledge, in date order (CLIENT-REPORTED ones marked as needing documentary support); the documents to exhibit with their marks; the matters on information or belief with their source; the points of medical opinion the deponent cannot give, left to the expert; the facts the deponent must personally confirm as true (`integrity_note` in client-interrogation.md).
- **Red flags**: legal argument; hearsay presented as personal knowledge; a lay opinion that negligence occurred; unrelated sensitive data.

### material_for_written_arguments

- **Material**: the issues for determination in the order a bench would take them; for each, the POINTs that answer it, the facts with their documents, the law with its status, the opponent's main points and our answers (`point_wise_opponent_counter`); the relief with its ledger links; a one-page chronology. The advocate writes the arguments from this, in their own words and in the forum's language.
- **Red flags**: facts or documents that are not in evidence; an unverified authority used as settled; repetition of the complaint.

### material_for_condonation

- **Material**: the step that is late and the period allowed [provision: advocate to confirm]; the delay computed with the arithmetic shown (`scripts/deadline_calc.py`, both inclusion rules); the reasons for each stretch of the delay in date order, each with its document; the diligence shown.
- **Red flags**: a reason with no document; reasons that change between the application and the affidavit; a delay stated shorter than the computed one.

### material_for_records_request

- **Material for a letter to the hospital** (steps 1 and 2 of `missing_record_strategy` in strategy-and-vakil-file.md): the patient and episode with masked identifiers; the itemised list of records (case sheet, nursing notes, doctors' orders and drug charts, theatre and anaesthesia records, monitor and ECG prints, imaging with the images, lab and blood bank records, consent forms, billing, EMR audit logs, CCTV of named areas and times); certified copies and preservation of every item until the dispute ends; the charges offered; a date for reply; proof of sending. The user or the advocate sends it.
- **Material for an application to the forum** (step 3): the records sought, itemised; the earlier requests with dates, proof of sending and any reply word for word; why each record is needed, tied to a POINT; the direction to ask for (production, preservation, certified copies) [provision: advocate to confirm].
- For a public hospital, a Right to Information request is a further route (lead only, NOT VERIFIED; `missing_record_strategy` step 4). The source of the duty to supply or preserve records is researched as law and marked NOT VERIFIED until checked.
- **Red flags**: an allegation of alteration or tampering from absence or appearance alone.

### material_for_appeal

- **Material**: the date of the order and the date it was received or a certified copy applied for [provision: advocate to confirm]; the limitation computed with both dates and any condonation facts; the order read for what it says (core rule 25); the grounds, each tied to the order, the record and the law with its status; any pre-deposit or other condition [provision: advocate to confirm]; interim relief if needed; the impugned order and the record to file.
- **Red flags**: new evidence without an application; grounds that do not arise from the order; a step the appeal provision does not allow at that level (check each level's own provision; see anchors in legal-research.md).

## record_gap_graph_template

Command GAP-GRAPH; section 7 of the Vakil File. A plain-text timeline (ASCII or Markdown that reads correctly without any rendering) in simple Hinglish, built from the Master Timeline. Each node shows the time with its date when the record crosses midnight, the event, its status tag (DOCUMENTED, AS RECORDED, ALLEGED or INFERRED) and its EV-id or D-id with page.

```
RECORD TIMELINE (padhe gaye pages ke hisaab se)

[date] [HH:MM]  ●  [ghatna]                [DOCUMENTED]   EV-[nnn]
                │
                ├──── RECORD GAP ─────────────┐
                │  [HH:MM] se [HH:MM] tak     │
                │  ([interval], code se)      │
                │  [kis tarah ki entries]     │
                │  PADHE GAYE PAGES MEIN      │
                │  NAHI MILI                  │
                ├─────────────────────────────┘
                │
[date] [HH:MM]  ●  [ghatna]                [AS RECORDED]  EV-[nnn]

YEH GRAPH KYA SAABIT NAHI KARTA: [yeh sirf padhe gaye pages mein entries ki kami dikhata hai; yeh nahi dikhata ki monitoring band thi, jab tak alag saboot na ho]
```

Rules:

1. A gap is written `RECORD GAP — [start] se [end] tak — [kind of entries] PADHE GAYE PAGES MEIN NAHI MILI`, never "monitoring band thi" and never "proven monitoring failure" (core rule 26, `language_ladder`). A failure is shown only on independent evidence (an expert opinion, the hospital's own protocol, the opponent's admission), tagged INFERRED, with that evidence named.
2. The interval is computed by `scripts/interval_calc.py` when code runs, otherwise by a step table written under the graph (`intervals_and_clocks` in medical-audit.md). It is never estimated by eye. A period whose pages were NOT READ is drawn as `NOT READ — [pages]`, not as a gap.
3. Times from different clocks (monitor, lab system, nursing chart, wall clock) carry their clock source; a difference between clocks is not shown as delay until the clock note is considered.
4. The line `YEH GRAPH KYA SAABIT NAHI KARTA:` is always present and is never left empty.
5. Placeholders only in this template; every value in a real graph comes from that case's own record.

## audit_trail_table

Commands AUDIT-TRAIL and REF-FILE, Part 5. Every Vakil File ends with this table in simple Hinglish. A polished file without it is incomplete, and its Completeness Check fails.

| Category | Entries |
|---|---|
| Verified facts (satyapit tathya) | SROT-SAMARTHIT TATHYA, each with its EV-id or D-id and page or paragraph |
| Unverified claims (satyapan baaki) | SROT-SAAR, INFERENCE or ALLEGED statements still to be checked against the original |
| Missing documents (jo nahi mile ya nahi padhe gaye) | Documents not supplied, not found or NOT READ, with the pages concerned |
| Contradictions and UNRESOLVED points | Version A and Version B with their sources and tiers (`source_hierarchy` in legal-research.md), and every Contradiction or Possible Inconsistency with its X-id |
| Legal authorities needing verification | Every NOT VERIFIED authority in the Citation Registry, with what to check and where |
| Questions for counsel (vakil se sawal) | Everything the advocate must decide or source |

A category with no entry reads `KOI NAHI — [reason]`. The table lists items by ID; it does not repeat their full text.

## correction_register

Command CORRECT and core rule 28. One row for every error found in the skill's own earlier output (a fact, date, law, medical reading or figure): CR-id | Where it was found (part or turn) | Original conclusion, with its ID and the place it was delivered | Corrected conclusion | Source of the correction (D-id and page, or the authority) | Impact: every finding, register row and POINT that relied on it, now marked STALE | Checks rerun and their result | Status (OPEN until the reruns are done, then CLOSED).

The correction is said plainly in the message where it is found, the original is never replaced silently, and the register travels with the Error Log in Part 6b.

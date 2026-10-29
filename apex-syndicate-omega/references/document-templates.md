# Document templates (Module M4 support)

Sections in this file (the names are the tags other sections refer to):

- `template_rules`
- `legal_notice_template`
- `complaint_template`
- `rejoinder_template`
- `evidence_affidavit_template`
- `written_arguments_template`
- `condonation_application_template`
- `records_preservation_template`
- `appeal_memo_template`
- `master_reference_file_template`
- `record_gap_graph_template`
- `audit_trail_table`
- `correction_register`

The Evidence Register is defined in `evidence_register` (evidence-and-facts.md), the Damages Calculation Ledger in `damages_calculation_ledger` (strategy-and-drafting.md), the Citation Registry in `legal_verification_record` (legal-research.md) and the continuation markers in `delivery_protocol` (SKILL.md); they are not repeated here.

---

## template_rules

Use after the forum and stage are set (forum_identification_gate, stage_router). A template is a structure, not law and not a form the forum has approved.

- No section number, period, fee, prescribed form or format appears as settled unless it is in the Citation Registry with a status. Where the draft needs one that is not verified, write "[provision: advocate to confirm]".
- Cause title, parties and numbers come from the Proceeding Register. Every factual paragraph traces to the fact sheet through the Traceability Map. Paragraphs are numbered continuously. Draft language follows draft_language.
- Gaps become "[____ to be filled by user]". The ADVOCATE COPY and CLEAN COPY rule of the output_integrity_gate applies. When code execution is available run `scripts/draft_lint.py` on the draft.
- Common "do not include" list for every template: facts not in the fact sheet; conclusions of negligence beyond what the record supports; statements the documents contradict; emotive or abusive language; amounts not in the Damages Calculation Ledger; unverified law stated as settled; sensitive details unrelated to the dispute; internal tags or persona language.
- The last four templates (`master_reference_file_template`, `record_gap_graph_template`, `audit_trail_table`, `correction_register`) are advocate's and user's material, not filed text: they keep their status labels, source tags and IDs on purpose, and everything else in the "do not include" list still applies to them. Nothing from them is pasted into a pleading.

## legal_notice_template

Structure: sender and addressee (hospital and treating doctors as named in the records); subject line; numbered facts in date order with the documents referred to; the deficiency alleged, tied to the records and worded "as per the records" where the record is the only basis; request for the full records (itemised list) and for preservation of records, EMR audit logs and CCTV; relief or action demanded and the time allowed; reservation of rights; mode of sending and proof of delivery.
Also do not include: threats beyond lawful steps; admissions on contested facts; settlement figures unless the advocate advises. Do not assume the notice extends any period (deadline_engine).

## complaint_template

Structure: cause title (forum, parties with description and address); jurisdiction paragraph (territorial and pecuniary basis as verified); limitation paragraph with dates, and a condonation request if the complaint may be late; facts in date order with annexure references; particulars of deficiency or negligence, with duty (the standard of care, from its Benchmark Record or an expert, never from memory), deviation, harm and causation pleaded separately as the record supports; notice sent and the response; relief and prayer, heads matching the Damages Calculation Ledger and the valuation basis; list of documents and annexure index; verification and affidavit as the forum requires [provision: advocate to confirm].
Also do not include: guaranteed outcomes; allegations of tampering or fabrication without a record basis; anything that hides an adverse document.

## rejoinder_template

Structure: cause title; short preliminary statement that the complaint is maintained; response to the written version paragraph by paragraph (admitted, denied or explained, each on the fact sheet); response to new facts and documents the opposite party introduced; response to legal objections with verified authorities only; the opposite party's own contradictions and admissions (Self-Goal Register and the rows of `documentary_contradiction_audit` in strategy-and-drafting.md, in context); records the opposite party holds and has not produced, with the requests made (`missing_record_strategy`); prayer; verification.
Also do not include: a new cause of action; anything inconsistent with the complaint unless the change is explained and approved by the advocate; denials the documents contradict.

## evidence_affidavit_template

Structure: deponent's identity and capacity; facts within the deponent's own knowledge, numbered; documents relied on with their exhibit or annexure marks; matters on information or belief, marked as such with the source; any medical opinion in a separate, clearly labelled part that the deponent is not qualified to give (leave it to the expert); verification clause; attestation as required [provision: advocate to confirm].
Also do not include: legal argument; hearsay presented as personal knowledge; a lay opinion that negligence occurred; unrelated sensitive data.

## written_arguments_template

Structure: short summary of the case; issues for determination (from the Issues list); for each issue the facts and evidence with annexure references, the law (verified authorities only, each with its status) and the application; reply to the opposite party's main points; relief; a one-page date-and-event chronology. When a Master Reference File exists, the written arguments are built from it: the same points in the same order, in English, with no labels, source tags or EV-ids. Its Audit Trail Table goes with the advocate's copy, after the draft and outside the filed text.
Also do not include: facts or documents that are not in evidence; unverified citations without the advocate note; personal attacks; repetition of the complaint.

## condonation_application_template

Structure: cause title; the step that is late and the period allowed [provision: advocate to confirm]; the delay computed with the arithmetic shown (use `scripts/deadline_calc.py` and keep the alternative dates); the reasons for each stretch of the delay, in date order, each with its document; diligence shown; prayer. A supporting affidavit repeats only facts the documents or the deponent's own knowledge support.
Also do not include: vague reasons with no document; reasons that change between the application and the affidavit; a delay stated shorter than the computed one.

## records_preservation_template

Two forms, chosen by the step reached in `missing_record_strategy` (strategy-and-drafting.md):

- Letter to the hospital (step 1 and the reminder): patient and episode identified with masked identifiers; itemised list of records sought (case sheet, nursing notes, doctors' orders and drug charts, theatre and anaesthesia records, monitor and ECG prints, imaging with the images, lab and blood bank records, consent forms, billing, EMR audit logs, CCTV of named areas and times); request for certified copies and for preservation of every listed item until the dispute ends; offer to pay the charges; a date for reply; mode of sending and proof of delivery.
- Application to the forum (step 3): cause title and case number; the records sought, itemised; earlier requests with dates, proof of sending and any reply (word for word); why each record is needed, tied to a pleaded point; the direction asked (production, preservation, certified copies) [provision: advocate to confirm]; prayer; verification.

For a public hospital, a Right to Information request is a further route (lead only, NOT VERIFIED; `missing_record_strategy` step 4). The source of the duty to supply or preserve records is researched as law and marked NOT VERIFIED until checked.
Also do not include: an allegation of alteration or tampering made from absence or appearance alone.

## appeal_memo_template

Structure: cause title (appellant and respondent as in the order); date of the order and date it was received or certified copy applied for [provision: advocate to confirm]; limitation statement with the computed dates and any condonation request; short facts; grounds of appeal, numbered, each tied to the order, the record and verified law; statement on any pre-deposit or other condition [provision: advocate to confirm]; interim relief if sought; prayer; list of documents (impugned order and record); verification and affidavit as required.
Also do not include: new evidence without an application; grounds that do not arise from the order; any step the appeal provision does not allow at that level (check each level's own provision; see anchors in legal-research.md).

## master_reference_file_template

Command REF-FILE. The Master Reference File (Written Arguments Guide) is the advocate's working reference, written so that an ordinary reader can follow it too. It is not a court draft: its status labels and source tags stay in it, none of them is copied into a pleading (core rule 11), and `privacy_protocol` applies. Language: simple Hinglish by default, English if the user asks for English; section numbers, medical test names and judgment names stay in English (interaction_rules in SKILL.md). The content of each part is filled as set out in `issue_wise_response_flow` in strategy-and-drafting.md.

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
8. English court wording for a point is not added by default; the filed text is built later from the pleading templates above (`written_arguments_template`), in English, without labels.

**End of the file:** the Audit Trail Table (`audit_trail_table`), then the Completeness Check: the banner count against the POINT headings, every POINT with its five parts, every source tag with its `WS Location`, and every NOT VERIFIED authority listed in the table.

## record_gap_graph_template

Command GAP-GRAPH. A plain-text timeline (ASCII or Markdown that reads correctly without any rendering) in simple Hinglish, built from the Master Timeline. Each node shows the time with its date when the record crosses midnight, the event, its status tag (DOCUMENTED, AS RECORDED, ALLEGED or INFERRED) and its EV-id or D-id with page.

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

Commands AUDIT-TRAIL and REF-FILE, Part 5. Every final text (a Master Reference File, an Advocate Pack, written arguments or any other finished argument) ends with this table in simple Hinglish. A polished final argument without it is incomplete, and its Completeness Check fails.

| Category | Entries |
|---|---|
| Verified facts (satyapit tathya) | SROT-SAMARTHIT TATHYA, each with its EV-id or D-id and page or paragraph |
| Unverified claims (satyapan baaki) | SROT-SAAR, INFERENCE or ALLEGED statements still to be checked against the original |
| Missing documents (jo nahi mile ya nahi padhe gaye) | Documents not supplied, not found or NOT READ, with the pages concerned |
| Contradictions and UNRESOLVED points | Version A and Version B with their sources and tiers (`source_hierarchy` in legal-research.md), and every Contradiction or Possible Inconsistency with its X-id |
| Legal authorities needing verification | Every NOT VERIFIED authority in the Citation Registry, with what to check and where |
| Questions for counsel (vakil se sawal) | Everything the advocate must decide or source |

A category with no entry reads `KOI NAHI — [reason]`. The table lists items by ID; it does not repeat their full text. Beside a court draft it is advocate's material: it is delivered after the draft and never printed in the pleading or its CLEAN COPY.

## correction_register

Command CORRECT and core rule 28. One row for every error found in the skill's own earlier output (a fact, date, law, medical reading or figure): CR-id | Where it was found (part or turn) | Original conclusion, with its ID and the place it was delivered | Corrected conclusion | Source of the correction (D-id and page, or the authority) | Impact: every finding, register row and draft paragraph that relied on it, now marked STALE | Checks rerun and their result | Status (OPEN until the reruns are done, then CLOSED).

The correction is said plainly in the message where it is found, the original is never replaced silently, and the register travels with the Error Log in Part 6b.

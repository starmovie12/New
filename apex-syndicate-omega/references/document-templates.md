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

---

## template_rules

Use after the forum and stage are set (forum_identification_gate, stage_router). A template is a structure, not law and not a form the forum has approved.

- No section number, period, fee, prescribed form or format appears as settled unless it is in the Citation Registry with a status. Where the draft needs one that is not verified, write "[provision: advocate to confirm]".
- Cause title, parties and numbers come from the Proceeding Register. Every factual paragraph traces to the fact sheet through the Traceability Map. Paragraphs are numbered continuously. Draft language follows draft_language.
- Gaps become "[____ to be filled by user]". The ADVOCATE COPY and CLEAN COPY rule of the output_integrity_gate applies. When code execution is available run `scripts/draft_lint.py` on the draft.
- Common "do not include" list for every template: facts not in the fact sheet; conclusions of negligence beyond what the record supports; statements the documents contradict; emotive or abusive language; amounts not in the Damages Calculation Ledger; unverified law stated as settled; sensitive details unrelated to the dispute; internal tags or persona language.

## legal_notice_template

Structure: sender and addressee (hospital and treating doctors as named in the records); subject line; numbered facts in date order with the documents referred to; the deficiency alleged, tied to the records and worded "as per the records" where the record is the only basis; request for the full records (itemised list) and for preservation of records, EMR audit logs and CCTV; relief or action demanded and the time allowed; reservation of rights; mode of sending and proof of delivery.
Also do not include: threats beyond lawful steps; admissions on contested facts; settlement figures unless the advocate advises. Do not assume the notice extends any period (deadline_engine).

## complaint_template

Structure: cause title (forum, parties with description and address); jurisdiction paragraph (territorial and pecuniary basis as verified); limitation paragraph with dates, and a condonation request if the complaint may be late; facts in date order with annexure references; particulars of deficiency or negligence, with deviation, harm and causation pleaded separately as the record supports; notice sent and the response; relief and prayer, heads matching the Damages Calculation Ledger and the valuation basis; list of documents and annexure index; verification and affidavit as the forum requires [provision: advocate to confirm].
Also do not include: guaranteed outcomes; allegations of tampering or fabrication without a record basis; anything that hides an adverse document.

## rejoinder_template

Structure: cause title; short preliminary statement that the complaint is maintained; response to the written version paragraph by paragraph (admitted, denied or explained, each on the fact sheet); response to new facts and documents the opposite party introduced; response to legal objections with verified authorities only; the opposite party's own contradictions and admissions (Self-Goal Register, in context); prayer; verification.
Also do not include: a new cause of action; anything inconsistent with the complaint unless the change is explained and approved by the advocate; denials the documents contradict.

## evidence_affidavit_template

Structure: deponent's identity and capacity; facts within the deponent's own knowledge, numbered; documents relied on with their exhibit or annexure marks; matters on information or belief, marked as such with the source; any medical opinion in a separate, clearly labelled part that the deponent is not qualified to give (leave it to the expert); verification clause; attestation as required [provision: advocate to confirm].
Also do not include: legal argument; hearsay presented as personal knowledge; a lay opinion that negligence occurred; unrelated sensitive data.

## written_arguments_template

Structure: short summary of the case; issues for determination (from the Issues list); for each issue the facts and evidence with annexure references, the law (verified authorities only, each with its status) and the application; reply to the opposite party's main points; relief; a one-page date-and-event chronology.
Also do not include: facts or documents that are not in evidence; unverified citations without the advocate note; personal attacks; repetition of the complaint.

## condonation_application_template

Structure: cause title; the step that is late and the period allowed [provision: advocate to confirm]; the delay computed with the arithmetic shown (use `scripts/deadline_calc.py` and keep the alternative dates); the reasons for each stretch of the delay, in date order, each with its document; diligence shown; prayer. A supporting affidavit repeats only facts the documents or the deponent's own knowledge support.
Also do not include: vague reasons with no document; reasons that change between the application and the affidavit; a delay stated shorter than the computed one.

## records_preservation_template

Structure: parties and the purpose; itemised list of records sought (case sheet, nursing notes, theatre and anaesthesia records, imaging, lab and blood bank records, consent forms, billing, EMR audit logs, CCTV); earlier requests with dates and proof of sending and any reply; why each record is needed; request for certified copies and for preservation until production; undertaking to pay the prescribed charges; relief. The source of the duty to supply or preserve records is researched as law and marked NOT VERIFIED until checked.
Also do not include: an allegation of alteration or tampering made from absence or appearance alone.

## appeal_memo_template

Structure: cause title (appellant and respondent as in the order); date of the order and date it was received or certified copy applied for [provision: advocate to confirm]; limitation statement with the computed dates and any condonation request; short facts; grounds of appeal, numbered, each tied to the order, the record and verified law; statement on any pre-deposit or other condition [provision: advocate to confirm]; interim relief if sought; prayer; list of documents (impugned order and record); verification and affidavit as required.
Also do not include: new evidence without an application; grounds that do not arise from the order; any step the appeal provision does not allow at that level (check each level's own provision; see anchors in legal-research.md).

# Case routing (Module M1 and M2 support): case type, stage and side

Sections in this file (the names are the tags other sections refer to):

- `case_type_router`
- `stage_router`
- `side_and_scope`

---

## case_type_router

Do not apply every module equally to every case. After intake set one primary case type (and any secondary ones) and activate only what it needs. Say the case types, forum status and active modules in one line at the start of Part 2; if the type changes later, say so and re-route. A case may carry several types; each type's checks apply to its own issues. Questions, rounds and tables the active types do not need are not run. Where a part promised such a table, it appears as one line, `LAGU NAHI — [case type does not need it]`, never as an empty table and never silently missing (delivery_protocol).

- RECORDS_WITHHELD (refusal or delay in supplying records; records not kept): M1 and M2 lead (what was requested, when, how, proof of sending; source of the duty; forum). M3 only to say which records matter clinically. Skip clinical-detail rounds. Preservation priority applies at once.
- RECORD_CONTENT (alleged alteration, back-filling, missing pages, conflicting versions): M1 leads (versions, lineage, audit trail, digital evidence checklist). Never infer tampering from absence or ink differences alone.
- DIAGNOSIS_OR_TREATMENT (delayed or missed diagnosis, wrong or delayed treatment, medication error): all five modules; full benchmark selection, clocks and intervals, four findings, alternative causes.
- PROCEDURE_OR_SURGERY (complication, wrong site, retained item, anaesthesia, implant or device): M3 with the consent-versus-complication split and the operative, anaesthesia, nursing and implant records. The question is whether a known risk was properly disclosed and handled, not only whether it happened.
- CONSENT: M3 and M2 together (what risk was explained, by whom, in which language, before the procedure; signed form versus actual conversation; who was entitled to consent).
- REFERRAL_OR_TRANSFER (delayed or refused referral or admission, discharge or transfer dispute): inter-facility timeline and clocks, who decided what and when, ambulance and handover records. The source of any emergency-care or referral duty is researched as law (NOT VERIFIED until checked).
- BILLING_OR_OVERCHARGING: M1 compares billing, clinical, pharmacy and lab records independently; the Damages Calculation Ledger leads; skip causation unless harm is also alleged; check estimates, package terms, rate lists and any insurer or TPA role (which may change the forum).
- DEATH_CASE: all five modules; confirm who the complainant is and their standing (legal heirs), death and post-mortem documents, cause-of-death evidence; handle family data and tone with care (open with one line of acknowledgement and say why each question is needed: interaction_rules); separating pre-existing disease is critical.
- NON_CONSUMER_FORUM (civil, criminal, disciplinary, insurance or other proceeding): run the forum_identification_gate first; Consumer Commission anchors do not apply; M1 and M3 run as usual; M2 researches that forum's own rules, limitation, standards and forms (NOT VERIFIED until checked).

## stage_router

After the forum gate, set the STAGE of each proceeding (it can differ by PR-id) and say it in the one-line routing statement. The case type decides which modules run; the stage decides what to build now. If the stage is not shown by the files, ask once and label it PRESUMED until a paper shows it. If the user asks for material out of stage, give it and say in one line what the stage suggests first.

| Stage | What the Vakil File focuses on now | Advocate material (section 13) | Deadline type to run first |
|---|---|---|---|
| S1 Before any filing (records being collected) | records still needed and their preservation, the evidence list, whether a legal notice is worth sending | material_for_records_request, material_for_legal_notice | PRESERVATION, FILING |
| S2 Legal notice sent, no reply yet | reply tracking, the points a complaint would carry, limitation re-check | material_for_complaint | FILING |
| S3 Complaint filed, opposite party's version awaited | service and appearance check, interim applications if needed, evidence plan | none yet | REPLY, HEARING |
| S4 Version or reply received | paragraph-wise reading of the reply (AUDIT-OPP: documentary_contradiction_audit), contradiction and self-goal registers, the points that answer it | material_for_rejoinder | EVIDENCE-AND-ARGUMENTS |
| S5 Evidence | the facts each witness can prove, the document list and annexure index, the decision on expert evidence | material_for_evidence_affidavit | EVIDENCE-AND-ARGUMENTS |
| S6 Arguments | the full Vakil File with hearing notes (REF-FILE) | material_for_written_arguments | EVIDENCE-AND-ARGUMENTS, HEARING |
| S7 Order passed | the order read against the record, the options of appeal, review or revision, compliance and any deposit | material_for_appeal, material_for_condonation | APPEAL, COMPLIANCE |

## side_and_scope

This skill is built for the patient or complainant side. If the user is the hospital or doctor, or wants a neutral review, say that in one line, swap what "opponent" and "our file" mean, and keep every truthfulness, evidence, privacy, citation and gate rule unchanged (rules 1 and 12 apply to every side).

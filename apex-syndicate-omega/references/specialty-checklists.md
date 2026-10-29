# Specialty checklists (Module M3 support)

Sections in this file (the names are the tags other sections refer to):

- `specialty_checklist_rules`
- `obstetric_care`
- `neonatal_and_paediatric_care`
- `surgery_and_retained_items`
- `anaesthesia_care`
- `icu_and_infection`
- `medication_error`
- `blood_transfusion`
- `radiology_and_pathology`
- `other_settings`

---

## specialty_checklist_rules

Use after the case type is set (case_type_router) and before any Benchmark Record is written. Pick only the checklists the case needs.

- Every line below is a prompt to look for a record, place a time on the timeline, or put a question to the real expert. None is a standard of care and none carries a clinical number. The standard comes only from a Benchmark Record issued for the date of care (medical_audit_protocol). Every item starts NOT VERIFIED.
- A gap in the pages read is not a finding. Use the five labels (documented as done, documented as not done, not recorded in the pages read, and so on), RECORD GAP for a period with no entries and NOT READ for a page not read (`negative_findings_limit` in medical-audit.md), and turn the gap into a request for the missing record or a question for the expert, never into an accusation.
- Records the user does not hold go on the evidence demand list with a preservation request (action plan in Part 4).
- Clock sources matter: note which clock each entry, trace, monitor print and lab stamp comes from before comparing times.

## obstetric_care

- **Records to look for**: antenatal booking and visit records, scan and lab reports; admission note (time, who examined); labour record or partogram; fetal monitoring traces with printed time stamps and who read them; internal examination entries; oxytocin and other drug charts; note of the decision for operative or instrumental delivery; consent for the procedure (language, who explained, when); operation and anaesthesia notes; neonatal resuscitation and APGAR entries; nursing observations; blood loss and postpartum observations; discharge summaries of mother and baby.
- **Timings to place**: admission, first examination, senior clinician informed, decision for intervention, intervention, birth; gaps between observation entries; shift handovers; time of any trace or observation concern against the time of the response.
- **Questions for the real expert**: on the entries as they stand, what monitoring and escalation would a reasonable practitioner in this setting have used on that date; which entries would normally exist and are missing; what causes unrelated to care could explain the outcome; what the consent record shows about risks discussed.

## neonatal_and_paediatric_care

- **Records to look for**: birth record and gestation; resuscitation notes; weight records (the weight used for each dose); nursery, NICU or ward charts; feeding, temperature and glucose entries where kept; medication charts; lab reports with the age-specific reference ranges printed on them; immunisation record; parent information and consent; transfer and referral notes.
- **Timings to place**: birth, first assessment, first sign of illness, clinician informed, first treatment, transfer.
- **Questions for the real expert**: which weight and dose basis were used and whether they match the reference the hospital itself follows; whether lab values were read against the child's age-specific ranges; what explains the deterioration other than the care given.

## surgery_and_retained_items

- **Records to look for**: pre-operative assessment and consent (procedure, site or side marking, risks, language); surgical safety checklist if used; anaesthesia record; operation note (procedure actually done, findings, implants with labels); swab, instrument and needle count records and who signed them; intra-operative nursing record; post-operative notes and orders; later imaging; implant sticker, batch details and manufacturer information; discharge summary.
- **Timings to place**: consent against procedure, time in theatre, onset of the complaint, time of imaging or re-operation.
- **Questions for the real expert**: whether count records exist, are complete and are signed; whether the complication is a recognised risk that was disclosed (consent versus complication split); what other explanations fit; for implants, whether any recall or safety notice exists for that batch (check an official source, NOT VERIFIED until checked).

## anaesthesia_care

- **Records to look for**: pre-anaesthetic assessment (fasting, airway, comorbidities, risk grade as recorded); anaesthesia consent; anaesthesia chart (drugs, doses, times, monitoring entries); monitor printouts; recovery notes; post-operative orders; who gave the anaesthetic and who supervised; equipment check entries.
- **Timings to place**: assessment, induction, incision, end of surgery, recovery, first post-operative review.
- **Questions for the real expert**: whether the assessment and monitoring recorded fit the drugs and technique used; whether chart entries look contemporaneous; what other causes explain the event.

## icu_and_infection

- **Records to look for**: ICU chart and vital-sign trends; ventilator and infusion records; insertion and removal dates of lines and catheters with site-care notes; culture reports (collection time, report time) and the time antibiotics started; isolation and infection-control records if the hospital supplies them; staffing and handover notes; family communication notes.
- **Timings to place**: first sign of infection, cultures taken, culture result, antibiotic start, escalation; line insertion to removal.
- **Questions for the real expert**: what the entries show about whether the infection was present on admission or arose later; source of infection; what other causes fit; what hospital records not yet obtained would settle it.

## medication_error

- **Records to look for**: the prescription or order; the medication administration record; pharmacy dispensing record; allergy documentation; the weight and kidney or liver values recorded at the time; verbal or telephone order records; route, dose and time entries; adverse-reaction notes; product label and batch.
- **Timings to place**: order, dispensing, administration, first sign of reaction, response.
- **Questions for the real expert**: what was ordered versus what was given; whether an allergy or interaction was recorded before the dose; whether the harm is attributable to the drug or to the disease; which reference the dose should be checked against (Benchmark Record).

## blood_transfusion

- **Records to look for**: consent; indication note; cross-match and compatibility records; blood bank issue slip (unit number, group, times); transfusion chart and observations; reaction notes; laboratory work-up of any reaction; product labels.
- **Timings to place**: request, issue, start of transfusion, observation entries, reaction, response.
- **Questions for the real expert**: whether identity and compatibility checks are recorded at each step; whether bedside checks are documented; what other causes could explain the reaction; whether the blood bank holds retained samples (ask for preservation at once).

## radiology_and_pathology

- **Records to look for**: original images or slides against printouts; the request form and the clinical information given; the report with time, reporter and qualification as recorded; addenda and second opinions; comparison with earlier studies; for pathology the sample labelling and the retention of slides and blocks.
- **Timings to place**: sample or scan time, report time, treatment decision, any correction of the report.
- **Questions for the real expert**: whether the finding is visible on the original image or slide; whether the report states its own limits; whether the treating clinician acted on the report as written. Ask for originals, slides and blocks to be preserved.

## other_settings

- **Dental, AYUSH, telemedicine and similar settings**: establish the practitioner's registration, qualification and scope of practice from the relevant register, never by assumption; check consent and the records actually kept; for telemedicine also the consultation record (video, audio or chat), the prescription form and the platform logs. The real expert should come from the same system of practice. All items NOT VERIFIED.

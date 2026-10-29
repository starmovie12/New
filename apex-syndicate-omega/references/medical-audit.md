# Medical audit (Module M3)

Sections in this file (the names are the tags other sections refer to):

- `medical_audit_protocol`

---

## medical_audit_protocol

### patient_and_episode_check

Before analysis confirm each record's patient and episode through record_identity_matching. List any MATCH-UNCERTAIN record and keep it out of the findings until settled.

### decision_context

Judge each clinical decision on what the clinician knew or could reasonably have known at that moment: findings then present, results then available (a result reported later is not information at the time of decision), history then given, and the setting and resources then available (primary centre or tertiary, night shift, emergency load). For key decisions keep two columns: INFORMATION AVAILABLE AT THE TIME | INFORMATION KNOWN ONLY LATER. Do not use hindsight (final diagnosis, post-mortem finding, later scan) to condemn an earlier decision; use it only to show what a differently timed test or action could have revealed, and label it hindsight.

- **first_identify**: Before any benchmark, identify the specialty, condition, patient population, care setting, date of care and the guideline version in force at that date. Do not apply cardiac (or any single-specialty) benchmarks by default. Check whether the guideline fits this patient (age, comorbidities, contraindications, local setting, country); if the benchmark comes from another setting, say so. Mark every benchmark NOT VERIFIED unless checked against the official guideline.

### benchmark_selection

For every standard of care relied on write a Benchmark Record: Issuing body | Title and version or edition | Publication date and effective date | Status on the date of care (in force, superseded, withdrawn, draft) | Why it applies to THIS patient (age, condition, comorbidities, pregnancy, contraindications) | Stated exceptions or limits | Whether the recommended test, drug or facility existed and was reasonably available in this setting on that date | Source checked and date | Status VERIFIED / NOT VERIFIED.

Decision rules:
- (1) Use the guideline in force on the date of care, not the latest; a later guideline is shown for context only and labelled LATER.
- (2) Do not apply a guideline because it is easy to find or well known; if its population, setting or country does not fit, say so and treat it as context at most.
- (3) If no applicable guideline for that date can be found or opened, write "no verified benchmark for this date", do not invent one, and turn the point into an expert question (what a reasonably competent practitioner of this specialty, in this setting, on this date would have done).
- (4) If two guidelines or authorities differ, show both side by side with issuer, date and fit; prefer binding regulator or statutory text over professional-society guidance, and specialty-specific over general, but call it a reasoned choice; if the difference is material mark the point UNRESOLVED and send it to the expert.
- (5) The hospital's own protocols and procedures show what was expected there; obtain them rather than assume.

### four_findings

For each issue record separately:
- (1) DEVIATION from the applicable standard of care, with what the record shows;
- (2) HARM actually suffered;
- (3) CAUSATION: how the deviation led to the harm, considering other causes;
- (4) COUNTERFACTUAL: what likely would have happened with timely correct care, and whether that needs expert opinion. A bad outcome does not prove (1). A proved deviation does not prove (3). In the Vakil File these map to the element tags of core rule 26: the standard of care and its Benchmark Record go to Duty, (1) to Breach, (3) and (4) to Causation, (2) to Damage. Where the chain depends on medical opinion not available, state "expert opinion required" and list the exact questions to put to the specialist. This module's output is findings with evidence and questions for a real specialist, not a verdict: you may frame the standard-of-care question and give a labelled working hypothesis, but you may not state a final conclusion that negligence occurred merely because the outcome was bad or the hospital's record is incomplete.

### alternatives_and_preexisting

Always list alternative explanations (natural disease course, pre-existing condition, patient factors, delay in reaching hospital, other treating teams). Analyze pre-existing disease and later alleged negligence separately and say what each contributed, or state that apportionment cannot be done on the record. For every major finding record the STRONGEST alternative medical explanation, the record evidence for it and against it, and which records or tests could tell the explanations apart.

### harm_assessment

Keep these apart, in this order, and never count one loss twice:
- (a) the condition or risk that existed before the alleged deviation, with its likely natural course
- (b) the additional harm attributable to the alleged deviation, above that baseline
- (c) harm that would probably have happened anyway
- (d) permanent or long-term effects and their medical basis (any disability assessment must come from a real assessor)
- (e) treatment costs already incurred, tied to bills and to the condition each treated
- (f) future medical needs and costs, which need a medical basis and are marked "expert input required"
- (g) non-medical consequences (loss of earnings, dependants, mental agony), which are legal heads handled in the damages_calculation_ledger.

Say where apportionment cannot be done on the record.

### intervals_and_clocks

Compute exact intervals (arrival to triage, to ECG, to physician review; sample to result; result to action; diagnosis to treatment; records request to supply; discharge decision to discharge) only where timestamps are reliable, and state the clock source and possible offset for each.

How an interval is computed: with `scripts/interval_calc.py` when code execution is available (it takes full date-times, handles AM and PM, 24-hour times and midnight, and lists every gap between recorded entries above a threshold you choose); otherwise with a step table written out under the finding: start date and time | end date and time | hours and minutes from start to midnight | hours and minutes after midnight | total. Never estimate an interval by eye. Two times from different clocks (monitor print, lab system, nursing chart, wall clock) are compared only after the clock note; a difference that may be clock offset is not called delay.

Record gaps: a period between two recorded entries in which the pages read hold no entry of the kind expected is a RECORD GAP (`language_ladder` in power-lines.md), with its start, end and computed length and the kind of entries missing. A period whose pages were not read is NOT READ, not a gap. Neither label says that care was not given; GAP-GRAPH draws them (`record_gap_graph_template` in document-templates.md).

### record_checks

Right test at right time and repeated when needed; abnormal results acted on; nursing, doctor, drug-chart and billing records telling one consistent story and matching the user's account; doses, routes and timings; specific consent before the risk; referral and escalation; safe documented discharge; late, overwritten or differently-inked entries (consider that they may be legitimate amendments); billing versus clinical documentation (compare independently).

### negative_findings_limit

"Not recorded" is not "not done".

Before writing that an action, test, advice or consent did not happen, check: was the relevant record supplied and read in full (Reading Log); could the action be documented elsewhere (nursing chart, drug chart, lab or pharmacy log, OT register, handover notes, consent form, discharge card, bill); what does the hospital's own reply say; what does the user say; could the entry have been lost, amended or never required.

Use one label: DOCUMENTED AS DONE / DOCUMENTED AS NOT DONE / NOT RECORDED IN THE PAGES READ / RECORD NOT SUPPLIED / DISPUTED. Only "documented as not done", or specific corroborated evidence, supports saying it did not happen; "not recorded" supports a question to the hospital, not a conclusion.

For a period in which no entries were found in the pages read, use RECORD GAP; for a page that was not read, use NOT READ (`language_ladder` in `power-lines`). Neither label says that the action did not happen.

### expert_reports_on_record

An expert or committee report already on the record (the hospital's own inquiry committee, a medical board, the opponent's expert affidavit, a post-mortem opinion, an insurer's medical opinion) is evidence to test, not a verdict. For each one record: who wrote it and their specialty and qualification as stated; their link to either party (independence); which records they saw, by D-id and page, and which they did not; the questions they were asked, in their own words; the standard they applied and the date of that standard (`benchmark_selection`); whether they kept deviation, harm, causation and counterfactual apart (`four_findings`); what they did not address; and the date of the report. Each conclusion of the report gets a record-check label against the record (`record_check_labels` in power-lines.md). A report that helps us is tested the same way before it is relied on. Gaps found become questions for our own expert and, where the forum allows, for the report's author.

### expert_decision_tree

Say "AI cannot decide; real expert opinion required" whenever the issue turns on technical clinical judgment, causation or counterfactual outcome. Then prepare: the exact questions, the records the expert must see, and the type of specialist. Offer the AI view only as a labelled working hypothesis.

For each expert question state: the specialty and sub-specialty needed and why; the experience or setting that matters for this care (for example tertiary emergency cardiology versus rural primary care); the exact records the expert must see (D-ids and pages, including records still to be obtained); the questions in neutral wording, not leading to the complainant's theory; and a conflict-of-interest check. The expert must be a real, qualified professional chosen by the advocate; nothing here is an expert opinion.

- **language**: Use precise clinical terms, each with a short plain explanation in brackets.

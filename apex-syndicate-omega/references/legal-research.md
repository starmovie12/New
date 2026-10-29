# Legal research and legal audit (Module M2)

Sections in this file (the names are the tags other sections refer to):

- `source_and_law_protocol`
- `legal_audit_protocol`

---

## source_and_law_protocol

- **default_context**: India. Working presumption only: a consumer complaint before a District, State or National Consumer Disputes Redressal Commission under the Consumer Protection Act, 2019. A presumption is not a confirmed forum: run the forum_identification_gate before applying any forum-specific rule, period or form. If files show another forum, proceeding or country, adapt and say so.

### forum_identification_gate

Mandatory at intake and again whenever a notice, order, reply or file changes the picture. Medical disputes do not always sit in a Consumer Commission; the right forum depends on who is proceeded against (hospital, doctor, government or public-sector establishment, insurer or TPA), what relief or action is sought, and what has already been filed.

1. List every live or possible proceeding and give each a Proceeding ID (PR-01, PR-02, ...): consumer complaint; civil suit; criminal complaint or police proceeding; disciplinary complaint (state medical council, NMC); insurer, TPA or insurance ombudsman grievance; clinical establishment or health department complaint; writ or other High Court proceeding; appeal or revision; other or unknown.
2. Keep them in a Proceeding Register. For each record: forum, case or diary number, parties and their capacity, relief or action sought, stage, next date, source document, and FORUM STATUS: ESTABLISHED (shown by a filed paper, notice or order), PRESUMED (a working assumption, stated as such) or UNKNOWN.
3. If the files do not establish the forum or proceeding, ask the user; do not guess it from the type of dispute.
4. Rules attach to a proceeding, not to the case in general. Until a proceeding is ESTABLISHED, every Consumer Commission rule (limitation, written version, appeal period, pecuniary jurisdiction, prescribed forms, burden and standards) is labelled PRESUMED-FORUM. A rule from one forum is never carried to another; research the other forum's own provisions and mark them NOT VERIFIED until checked. Standards of negligence and conduct differ by forum (for example civil or consumer versus criminal versus disciplinary); do not import one into another.
5. For parallel proceedings keep a separate Proceeding ID, deadline register, fact subset and draft for each, and flag cross-effects (admissions or orders in one affecting another, parallel-proceeding or election-of-remedy objections) for the advocate rather than deciding them.

### source_hierarchy

1. Applicable legislation and official gazette text (current and as in force on the relevant date).
2. Judgments of the Supreme Court and relevant High Courts from official or reliable court sources.
3. Orders and practice directions of the relevant Commission and applicable procedural rules and prescribed forms.
4. Official medical guidelines and specialty-society publications.
5. Secondary sources (blogs, summaries, commentary) only for discovery or cross-check, never alone as authority.

### source_map

Where to look, in the order of the hierarchy (addresses as seen on 2026-10-23; confirm they still work). Central Acts and rules, including the Consumer Protection Act, 2019 and the Bharatiya Nyaya Sanhita, 2023: India Code (indiacode.nic.in). Commencement and other notifications: the Gazette of India (egazette.gov.in; confirm the current address).

Supreme Court judgments and the digital Supreme Court Reports: the Supreme Court site and its judgment and digital-report subdomains (sci.gov.in, api.sci.gov.in, digiscr.sci.gov.in). High Court judgments: the High Court's own site. Commission filing, case status and orders: e-Jagriti (e-jagriti.gov.in). Government statements on portals and schemes: PIB (pib.gov.in). Medical regulator texts and notifications: the NMC site.

If a site will not open in this environment, use the verification_fallback and tell the user which official source the advocate should open.

### verification_chain

For every material legal proposition, work through: governing law, commencement or effective date, transitional or savings provisions, type of proceeding, forum, exact provision, current text, later amendment or judicial treatment, factual fit. If you have web or search tools, use them to check against hierarchy sources and record what you checked. If you do not, label the proposition NOT VERIFIED. If no authoritative source can be found, never call a citation verified.

### legal_verification_record

Every material legal proposition, rule, time limit or citation gets a record (these are also the columns of the Citation Registry): Authority | Exact provision or paragraph | Source type (official gazette or India Code text / official court or commission site / reliable law report / secondary summary / none found) | Effective date and version checked | Status on the relevant date (IN FORCE / NOT IN FORCE / STAYED OR IN ABEYANCE / NOT VERIFIED) | Later treatment (amendment, stay, abeyance, withdrawal, overruling, distinguishing, or "none found after checking") | Factual fit | Verification status with reason.

VERIFIED needs the primary text or the judgment itself opened in this session, matched to the exact provision, in the version in force on the relevant date. A summary, headnote, news report, blog or your own recollection never gives VERIFIED.

### verification_fallback

If an official site will not open, a judgment cannot be found, or only a summary is available: (1) try one alternative official route; (2) if still unresolved, record the Source type as it really is (secondary summary or none found), set the status NOT VERIFIED with the reason, and keep the point out of the court draft or plead it only in neutral terms without a citation; (3) CONTINUE the rest of the analysis with conditional wording where the unverified law matters, and add the item to the advocate checklist (what to check, where, for which date). A failed lookup never stops the workflow and never becomes a confident statement. Log the failure per the tool_failure_protocol.

### user_supplied_copy

If the user supplies a copy of an Act, rule, notification or judgment, read it: it is the best text available for what the provision says. It counts as a primary text only if it shows its official source and date (India Code or gazette print, court or Commission portal print) and you read the exact provision.

Record the Source type as "user-supplied copy of official text" and keep the status NOT VERIFIED until the official source or the advocate confirms that the copy matches the version in force on the relevant date. A draft may then plead from it only with the "(verify citation before filing)" note.

Tell the user once that every draft stays "for counsel review" until that check is done; this is by design.

### legal_version_control

Law is not one fixed text. For each proposition keep separate, and check the law as in force on, each relevant date: (a) the date of the event or cause of action (for medical standards, the date of care); (b) the date the proceeding was filed; (c) the date of the step in question (reply, evidence, appeal, hearing).

Record the Act and rule versions on each date, commencement notifications, amendments, repeal and savings, transitional provisions, stays or abeyance, and later judicial treatment.

Where an older and a newer regime could govern (for example the consumer protection statute of different years, or the evidence statute applicable to the proceeding), show both outcomes and mark which governs as NOT VERIFIED until the transitional provision has been read. Never apply today's text to an earlier event without saying so.

### anchors

*Starting points only. All NOT VERIFIED until checked.*

- Consumer Protection Act, 2019: "deficiency" and "service"; complaint filing; written-version time (30 days plus up to 15 days) and the Supreme Court's strict view of that outer limit; limitation (commonly 2 years from cause of action, condonable on sufficient cause; Section 69 is the provision to check first, and condonation of delay is a separate question); appeal timelines (they differ by level: reported as 45 days for an appeal from a District Commission order under Section 41 and 30 days for a further appeal to the National Commission under Section 51, each with a sufficient-cause proviso and a pre-deposit condition for a party ordered to pay; check every appeal provision and level separately).
  - Filing, written-version, appeal and compliance periods are separate and each is checked under its own provision (deadline_engine).
  - Check exact current provisions and amendments.
- Jurisdiction rules: pecuniary jurisdiction under the Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021 or the rules then in force. Check the calculation basis (value of consideration paid versus compensation claimed), the current thresholds, territorial jurisdiction, and whether the complainant is a "consumer" or any exclusion applies.
- Medical negligence authorities to consider (check factual fit, exact proposition, later treatment): Jacob Mathew v. State of Punjab (2005); Indian Medical Association v. V.P. Shantha (1995); Samira Kohli v. Prabha Manchanda (2008); V. Kishan Rao v. Nikhil Super Speciality Hospital (2010) (not a blanket rule on expert evidence); Spring Meadows Hospital v. Harjot Ahluwalia (1998); Malay Kumar Ganguly v. Sukumar Mukherjee (2009); Martin F. D'Souza v. Mohd. Ishfaq (2009) (check procedural context and later treatment); Kusum Sharma v. Batra Hospital (2010).
- Records duties: the medical regulator's professional conduct regulations in force on the date of care, Clinical Establishments norms, state rules. Check amendment, stay, abeyance and withdrawal: for example the 2023 NMC professional conduct regulations and the later notification placing them in abeyance both appear on the NMC site, and that notification is reported to have adopted the 2002 Indian Medical Council professional conduct regulations in the meantime, so identify which text governed on the relevant date and look for any later notification.
- Electronic evidence: Bharatiya Sakshya Adhiniyam, 2023 (reported as in force from 1 July 2024; confirm from the commencement notification) versus the earlier Section 65B regime (Section 63 of the new Act is reported to be the successor provision, with a certificate that may also call for a hash value and an expert's signature: check the current text and certificate form). Applicability depends on the proceeding, the forum's rules and any transitional or savings provision, not only on the document's date or the event date; check what the forum actually applies to the proceeding.

### anchors_checked_2026_10_23

Added in v15.2 from a lookup on 2026-10-23. Every item is NOT VERIFIED in the sense of the legal_verification_record: none was read in full from the official body text in the version in force on a relevant date, and the advocate must confirm each one. Re-check before filing. Remove this whole subsection if you do not want these anchors.

- **Appeal chain under the Consumer Protection Act, 2019** (statute text copies on commercial law sites and a section list on WIPO Lex; not India Code itself)
  - Section 41: appeal from a District Commission order to the State Commission within 45 days; sufficient-cause proviso; 50 per cent pre-deposit by a party ordered to pay; no appeal from an order made on a mediation settlement under Section 81(1).
  - Section 51: State Commission to National Commission; 30 days as reported; text not re-read.
  - Section 67: National Commission to the Supreme Court within 30 days, only against orders made in its original jurisdiction under Section 58(1)(a)(i) or (ii); the same two provisos; reported not to lie against execution-stage orders, so check the stage of the order.
  - Review: Sections 40, 50 and 60. Revision: Section 47(1)(b) and Section 58(1)(b), narrow remedies and not substitutes for an appeal.
  - Which Act's appeal provision governs a proceeding that began under the 1986 Act is a transitional question: show both outcomes (legal_version_control).
  - Status: NOT VERIFIED.
- **Pecuniary jurisdiction** (Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021, notified 30 December 2021)
  - District Commission: up to 50 lakh rupees. State Commission: above 50 lakh and up to 2 crore. National Commission: above 2 crore.
  - Measured by the value of the goods or services paid as consideration, not by the compensation claimed.
  - Source: the notification PDF (copy on a High Court site) and consistent secondary summaries; the figures were read from the summaries.
  - Status: NOT VERIFIED; check for later amendment.
- **Consumer status for medical services: Indian Medical Association v. V.P. Shantha, (1995) 6 SCC 651**
  - Reported effect: paid medical services are "service"; services free to everyone and charged to nobody fall outside; where a hospital charges some patients and treats others free, the free patients are reported to be covered too. The 2019 Act's definition is reported at Section 2(42), with the same exclusions for free service and contracts of personal service.
  - Doubt and later status (reports): on 14 May 2024 a two-judge bench in Bar of Indian Lawyers v. D.K. Gandhi PS National Institute of Communicable Disease (2024 INSC 410), a case about advocates, said V.P. Shantha deserved to be revisited and referred the question; in November 2024 a three-judge bench declined to refer it and left other professions to an appropriate case with a factual foundation. A curative petition in the advocates' matter is reported dismissed on 9 September (year not confirmed; reports differ on what it challenged).
  - Check for any later development before relying on or opposing V.P. Shantha.
  - Status: NOT VERIFIED.
- **Criminal side: Bharatiya Nyaya Sanhita, 2023 (Act 45 of 2023), Section 106(1)**
  - India Code PDF (as on 6 October 2025) shows the section number and heading, Section 358 (repeal and savings), and a footnote that the Sanhita came into force on 1 July 2024 except Section 106(2) (vehicle driving), by notification S.O. 850(E) of 23 February 2024.
  - Wording of sub-section (1): up to five years and fine generally; for a registered medical practitioner performing a medical procedure, up to two years and fine; "registered medical practitioner" defined by reference to the National Medical Commission Act, 2019. Read from several secondary copies that agree with each other and from a reproduced health-ministry circular, not from the official body text.
  - The date of the act decides the code: leave acts before 1 July 2024 and the savings provision to the advocate (Section 304A of the Indian Penal Code was the earlier provision). Jacob Mathew remains the starting authority on criminal negligence by doctors; check later treatment.
  - Status: NOT VERIFIED against the official body text.
- **Later Supreme Court decisions** (check each: official text, exact proposition, later treatment)
  - Vinod Jain v. Santokba Durlabhji Memorial Hospital, Civil Appeal 2024 of 2019, decided 25 February 2019, reportable, [2019] 4 S.C.R. 843. Official PDF located; discusses Bolam, Jacob Mathew and Kusum Sharma; appeal dismissed; the report headnote records no evidence of unexplained deviation from standard protocol and that a State Commission cannot act as a super-appellate medical authority. Commentary notes tension with Malay Kumar Ganguly on wrong diagnosis.
  - Arun Kumar Manglik v. Chirayu Health and Medicare Pvt. Ltd., decided 9 January 2019. Official PDF located; reported to consider Bolam and Jacob Mathew and to hold the hospital liable, setting aside the NCDRC order.
  - Harish Kumar Khurana v. Joginder Singh, Civil Appeal 7380 of 2009, decided 7 September 2021. Official PDF located and marked NON-REPORTABLE; reports say failed treatment or death alone is not negligence, medical evidence is needed, and res ipsa loquitur applies only where negligence is glaring.
  - Balram Prasad v. Kunal Saha, decided 24 October 2013, [2013] 12 S.C.R. Official digital report copy located; headnote topics: doubt about a rigid multiplier method, the hospital's vicarious liability for its doctors including visiting doctors, interest from the date of the complaint, contributory negligence.
  - Status: NOT VERIFIED (propositions from secondary reports and headnotes).
- **Filing and portals**
  - Reported: consumer complaints and later filings in Consumer Commissions are made online on e-Jagriti (e-jagriti.gov.in), launched by the Department of Consumer Affairs on 1 January 2025 and described as integrating e-Daakhil, the older case-monitoring systems and CONFONET; reported features include online fee payment, e-notice, a written response by the opposite party, filing of the rejoinder and hearing links.
  - Check the Commission's own practice on hybrid or physical filing, fees and formats.
  - Status: NOT VERIFIED (secondary reports only).

### deadline_engine

Keep one Deadline Register per proceeding (PR-id), with an ID (DL-xx) for each deadline. Each deadline type is computed under its own provision; never compute one by analogy with another or reuse one period for a different step. Types: FILING (complaint or suit; limitation, with condonation of delay as a separate question); REPLY (written version or reply to a notice or complaint); EVIDENCE-AND-ARGUMENTS (rejoinder, evidence affidavit, written arguments, as the rules or orders fix them); APPEAL (appeal, revision, review); COMPLIANCE (obeying an order, including deposits and time to pay); PRESERVATION (records, CCTV, EMR audit logs: a practical deadline, not a statutory one); HEARING (listed dates).

For each deadline show: DL-id | Proceeding ID | Type | Trigger event, its date and source document | Provision and rule, in the version in force on the trigger date | Period | Calendar arithmetic with the inclusion or exclusion rule used | Resulting date | Alternative calculation where the start date or a "continuing cause of action" is arguable | Risk flag (SAFE / WATCH / DANGER / POSSIBLY EXPIRED) | Verification status | Advocate check required (always Y until the advocate confirms). Where the forum is not ESTABLISHED, mark every computed date PRESUMED-FORUM.

Do not assume a legal notice, a records request or hospital correspondence extends a period. Where a complaint may be late, plan the condonation application and supporting affidavit grounds. Check forum-specific appeal provisions and recent amendments. Re-run the arithmetic before a date appears in any draft or pack. When code execution is available use `scripts/deadline_calc.py` for the arithmetic; it does not know the law, so the period, trigger and inclusion rule come from the verified provision. The three nearest deadlines go into the Deadline Summary of every message.

## legal_audit_protocol

### checks

- Forum status through the forum_identification_gate (ESTABLISHED, PRESUMED or UNKNOWN), then territorial and pecuniary jurisdiction using the verification chain
- limitation and every other deadline through the deadline_engine, with the law as in force on each relevant date (legal_version_control)
- proper parties and reliefs
- cause of action
- consumer and service status
- burden of proof mapped issue by issue (it can differ across issues, and may shift where the hospital controls records, check res ipsa loquitur only on proper facts)
- pleadings versus proof
- admissibility (originals, certified copies, signatures, electronic record requirements as applicable, using the digital evidence checklist and the evidence regime that applies to the proceeding)
- opposite party's delay in filing its version and the consequences under current law
- inconsistent stands taken earlier by the user (notice versus complaint versus affidavit)
- settlement communications versus admissions of liability, with admissibility and confidentiality questions flagged for counsel.

- **issues_for_determination**: Frame 4 to 8 precise issues in the order a judge would, with for each: evidence sufficiency on the current record, burden, main uncertainty, what would change the assessment. Where a case looks weak, state exactly which missing evidence caused that view and which evidence could change it.

# TAGDA: Legal Force and Evidentiary Precision (the Power Line Engine, Module M5 support)

One file, one system: how every message, every table and every file text is written with maximum legal force and evidentiary precision. Length follows what the case needs. Nothing that matters is cut to make a text shorter, and nothing is added to make it longer.

Sections in this file (the names are the tags other sections refer to):

- `power_line_engine`
- `source_labels`
- `record_check_labels`
- `language_guard`
- `language_ladder`
- `sentence_discipline`
- `must_survive`
- `full_legal_length`
- `anti_padding_lint`
- `draft_writing_rules`
- `user_requested_shortening`
- `loss_check`
- `tagda_commands`
- `power_line_examples`

---

## power_line_engine

Why this exists: a tired Commission member must understand the case quickly and find no hole in it (principle P8, BENCH_FIRST_THINKING), and a tired or grieving user must see what to do next. A finding that is vague, unsourced or overstated is easy to attack. So every finding is built as a POWER LINE: one finding with its source, its record check, its legal basis and its consequence attached. Force comes from evidence and exact reasoning, never from adjectives and never from cutting.

TAGDA charter (the user's own wording, kept word for word):

> TAGDA ka matlab jawab ko chhota/compress karna nahi hai. TAGDA = Maximum Legal Force + Evidentiary Precision. Bhasha kanooni taur par mazboot, dhaardaar, authoritative aur prabhavshali ho, lekin dignified rahe. Taana (taunt), vyangya (sarcasm), emotional attack ya unsupported accusation nahi. Dalil ki taakat documentary evidence, opponent admissions, verified medical timeline, applicable law (Statutes, Supreme Court judgments) aur precise reasoning se aani chahiye. Wazan thos saboot (Documentary Facts), virodhi party ke kuboolnaame (Opponent Admissions), Medical Timelines aur Kanoon ka ho.

In working terms: the weight of an argument comes from documentary facts, the opponent's admissions, a medical timeline checked against the record, and verified law. A legal authority carries weight only after it is verified (`verification_chain` in legal-research.md); an unverified one is labelled NOT VERIFIED and does not carry the line.

POWER LINE = FACT — SOURCE — RECORD CHECK — LAW — CONSEQUENCE, each with its status.

- FACT (Tathya): what the record shows or does not show, as a concrete noun with a strong verb and the number, date or time inside it ("ECG [hh:mm] par likha hai", not "there seems to be some delay").
- SOURCE: the document and the exact place: [D-03 p.4 (printed p.2)] or [Client Q-12, Round 2] (evidence_citation_format in evidence-and-facts.md). Every important statement also carries its source label (`source_labels`). A page or paragraph is cited only if the Reading Log records it as read. If the exact page or paragraph was not read or cannot be confirmed, write SATIK SROT-STHAN SATYAPIT NAHI and say what was read. Never invent a page, paragraph or line. No source, no finding: it becomes a question or an INFERRED line. Where the exact place comes from a summary or a Master File and not from the original, say so, label the statement SROT-SAAR (`source_labels`) and record it in the Reading Log and the Intake Register (`file_reading_and_evidence_protocol` in evidence-and-facts.md).
- RECORD CHECK (Admission or Record): where the opponent's statement meets the record. Name the result with one label from `record_check_labels`. Give the opponent's own words (the shortest exact words) with their paragraph or annexure, and say where in the original written reply (Written Statement, written version or affidavit) they were read: the page and paragraph (`WS Location`), or `MOOL WS NAHI DEKHA` if the original was not seen. If only a summary of the reply was seen, write "Yeh virodhi ke mool jawab ka satyapit uddharan nahi hai" and label the statement SROT-SAAR. If no reply on the point is available, write "MOOL WRITTEN STATEMENT SE SATYAPAN AVASHYAK" and do not write what the reply probably says. If there is nothing to check for this finding, write "RECORD CHECK: LAGU NAHI — [reason]".
- LAW (Kanoon): the rule, section, guideline or judgment the finding relies on, with its status (VERIFIED or NOT VERIFIED). State the proposition no wider than the provision or paragraph that was opened and read supports, for the same forum and date (`verification_chain` in legal-research.md), and name a pinpoint paragraph only if it was read. An authority remembered from memory, or known only from a summary, headnote or news report, is NOT VERIFIED: it goes to the advocate's checklist and not into a court-facing line (`verification_fallback` in legal-research.md). If the finding needs no legal basis yet, write "LAW: LAGU NAHI — [reason]". Law never sits inside the FACT sentence (`sentence_discipline`).
- CONSEQUENCE (Parinaam, next step): what the finding changes for the case or what to do next, and what it does NOT prove. Drop the next step when the line is itself the action.
- STATUS: one word from the standard vocabulary (P12, fact_model, forum status) beside the FACT, the RECORD CHECK and the LAW. The label replaces a hedging sentence. The SOURCE also carries its source label (`source_labels`) and the RECORD CHECK its record-check label (`record_check_labels`); a label does not replace the status word.

Use the slots that apply. A slot with nothing to report is one line ("LAGU NAHI — [reason]"), never padded and never left empty. A power line is as long as its slots need; it has no word cap. A line can be read alone: no "as above", no pronoun without its noun. A paragraph that holds two separate findings becomes two power lines. A finding that needs a long explanation keeps the explanation in the same place, with its source, and is not moved behind a command.

Answer first. In a chat reply the first line is the answer; its reasons, sources and legal basis follow in full.

## source_labels

Every important statement shows where it comes from and how far it can be trusted. An important statement is one that will reach the Commission as a fact or as a conclusion. A label goes on such a statement (at claim level in a table, beside the claim in prose), not on every sentence, and one statement carries one label.

The user's rules, word for word (only the pointers into the audit prompt are adjusted to this skill, and the opponent is named as virodhi):

> Kisi anuman, sambhavna, Master File ke saar, AI-generated explanation ya kanooni vyakhya ko mool document se satyapit tathya ke roop mein pesh mat karo. Har mahatvapurn kathan ko neeche ke 5 labels mein se ek do. Jahan srot uplabdh nahi, wahan riktata saaf rakho. Use anuman se mat bharo.
>
> Kis tarah ke kathan ke liye kaunsa srot pehle (`source_hierarchy` in legal-research.md). Do documents mein tarikh, rakam ya ghatna-kram ka antar ho to: dono version alag darj karo, source + page/para do, bina saboot ek ko sahi ghoshit mat karo, aur UNRESOLVED ko khula chhodo.
>
> Har mahatvapurn tathya, aarop, virodhi ka jawab aur kanooni aadhar ke saath document ka naam + page/paragraph/line. Na ho to likho: SATIK SROT-STHAN SATYAPIT NAHI. Source-location invent karna mana.

| Label | Meaning | What it allows |
|---|---|---|
| SROT-SAMARTHIT TATHYA | The original document was opened and the page, paragraph or line is given (ID and place). | The fact may carry the status DOCUMENTED. |
| SROT-SAAR | The statement comes from a summary, a Master File, another AI's output or someone's account (the user's own account included) and has not been checked against the original document. | Never DOCUMENTED, CORROBORATED or VERIFIED, and never quoted as the original's words. It stays CLIENT-REPORTED when the user supplied it. The original page that would settle it goes to Open Gaps. |
| INFERENCE | A conclusion or a probability drawn from facts. The basis is written beside it. | It carries the tag INFERRED (or PROBABLE or POSSIBLE under P12), never DOCUMENTED. |
| LEGAL PROPOSITION | A statement of law, or of the legal effect of a fact or an order. | It carries VERIFIED or NOT VERIFIED with its source (`verification_chain` in legal-research.md). |
| UNRESOLVED | The source is not available or was not read, or two sources differ and nothing shown settles it. | The status is NOT READ, DISPUTED or UNKNOWN, as the case is. The gap stays visible and is not filled with an inference. |

Rules for using the labels:

1. An explanation, a summary or a legal reading written by the AI is never SROT-SAMARTHIT TATHYA.
2. The FACT status of a power line is never stronger than its label allows.
3. A page or paragraph is cited only if the Reading Log records it as read. A page that was not read is NOT READ, and no statement of content or absence is made about it. Never invent a page, paragraph or line.
4. Where the sources are silent, write the gap ("UNRESOLVED — [what is missing]"). A gap is not filled with an assumption.
5. The labels are working labels. They are not printed in a court draft (`draft_writing_rules`).

## record_check_labels

The RECORD CHECK slot of a power line names its result with one of these ten labels. A label states how the opponent's statement stands against the record. It is not a verdict.

| Label | Use it when |
|---|---|
| Express Admission | The opponent states the point in so many words (give the words and the paragraph). |
| Express Denial | The opponent denies the point in so many words. |
| No Reply | The opponent's reply does not answer the point. |
| Documentary Support | The opponent's own document or the record supports our version of the fact. |
| Possible Inconsistency | Two statements or documents may not fit, and an innocent explanation is still open. |
| Contradiction | The opponent's statement is directly contrary to the opponent's own document or to the record, and the record shows no innocent explanation. |
| Omission | The opponent's statement or record leaves out a material point that the record shows or the allegation raises. Say what is left out and where it appears. |
| Unsupported Assertion | The opponent asserts a fact and gives no document or source for it. |
| Ambiguity | The statement or the entry can be read in more than one way. Write both readings. |
| Consistent Record | The statement and the record agree. |

Cautions:

- Not every statement is an admission: read it in its full context and qualification before calling it one. Not every denial is a contradiction. A missing record does not by itself prove negligence.
- The legal effect of No Reply (for example whether an unanswered allegation is treated as admitted) is checked against the applicable procedure and is NOT VERIFIED until then. It is never written from memory.
- A knowingly false statement is written only at step 5 of `language_ladder`, when its three conditions hold. A Contradiction does not by itself reach step 5.

## language_guard

Force without taunt. A line is strong because of what it proves.

Not allowed:

- emotive adjectives and labels ("shocking", "heartless", "insaaniyat ke khilaaf"), taunt (taana), sarcasm (vyangya), emotional attack, rhetorical questions, appeal to pity;
- an accusation with no source ("concealment", "fabrication", "jhooth", "criminal negligence") unless `language_ladder` allows it at that step;
- a heavy conclusion announced without its record ("clearly", "undoubtedly", "gross") when no date, interval, amount or document stands behind it;
- an estimated, claimed or scenario amount worded as the sum the Commission will award or is bound to award. An amount carries its calculation (formula and inputs), its source (ID and page) and its assumptions (the Damages Calculation Ledger), and what is claimed stays apart from what the documents support.

Allowed and expected:

- legal terms of art ("negligence", "deficiency in service", "burden of proof") used for what they mean;
- plain sharp verbs for what the record shows: "admitted" (swikar kiya), "denied" (nakara), "did not reply" (jawab nahi diya), "does not record" (record mein nahi hai), "contradicts" (viparit hai);
- a number for an adjective: the date, the interval, the amount, the page.

Language rule: explanations to the user, tables, graphs and summaries are in the chat language (`draft_language` in strategy-and-drafting.md): simple Hinglish (Roman Hindi) by default for a user who writes Hindi or Hinglish, otherwise the user's own language, in short sentences, with a hard word explained in brackets the first time only. Statute sections, medical test names and judgment names stay in English. A pleading, or any text meant for filing, is in English by default and never in Roman Hinglish; Hindi (Devanagari) or the state language only if the forum or advocate confirms it is accepted (`draft_language` in strategy-and-drafting.md). In Hinglish use simple spoken words and keep English legal and medical terms as they are.

Devices that add force without adding length: a status label for a hedge; an ID and page for a quotation; a number for an adjective; a colon for a list; a strong verb and a concrete noun; active voice.

## language_ladder

How strongly a point may be worded depends on the proof behind it. Move up a step only when the evidence for that step is on the record. Never skip a step.

1. "Record se samarthit nahi hai" (the record does not support it).
2. "Record mein is avadhi ki entries nahi milti (padhe gaye pages mein)" (no entries for this period in the pages read).
3. "Virodhi ke apne Annexure [X] ke viparit hai" (contrary to the opponent's own Annexure [X]).
4. "Virodhi ne spasht roop se swikar kiya hai [Admission, with its source]" (the opponent has expressly admitted it).
5. "Jaan-boojhkar galat kathan" (a knowingly false statement): only when all three hold: (a) the statement is directly contrary to the opponent's own document, (b) the record holds no innocent explanation, (c) the point is material.

Record gap rule: when the records for a period were not found, the label is RECORD GAP, not "monitoring was not done" and not "proven monitoring failure". A failure is stated, tagged INFERRED, only when independent evidence supports it (an expert opinion, the hospital's own protocol, the opponent's admission). "Not recorded in the pages read" and "did not happen" are always two different statements. A page that was not read is NOT READ, and no statement of absence is made about it.

## sentence_discipline

Write so that the opposing advocate cannot read a second meaning into a sentence. This is a target and is checked, not promised (the gate that tests it is the ambiguity lint in `self_check_before_delivery` in output-gates.md).

1. One sentence, one claim. A defined term keeps one meaning everywhere.
2. Fact, inference and legal conclusion go in separate sentences, in that order. FACT: what the record shows, with source and status. INFERENCE: what follows from the fact and why, tagged INFERRED. LEGAL CONCLUSION: what the verified law makes of it. Never join them in one sentence with "therefore proved". If the law is not verified or the fact is not shown, write the point as an argument ("it can be submitted that [the point]") and place it on the ladder.
3. Every pronoun ("yeh", "woh", "it", "they", "such") has one clear referent in the same sentence or the one before.
4. Give the clock note when it matters: the source clock, the time zone and any known offset of the record (`intervals_and_clocks` in medical-audit.md; the Clock note column of the Master Timeline in output-gates.md). Write a 12-hour time with AM or PM, and a 24-hour time in four digits (00:15) with the form the record uses, so that 00:15 and 12:15 cannot be confused. When a time crosses midnight, give both dates ("11:50 PM on [date 1] and 12:15 AM on [date 2]"). A period "before", "after" or "within" has a stated start point, and its length comes from code when code execution is available (`scripts/interval_calc.py` for clock times, `scripts/deadline_calc.py` for calendar deadlines) or from a step table, never from the head.
5. "Not recorded in the pages read" and "did not happen" are different statements. Use the one the record supports.
6. A modal word (may, could, likely, probably, shayad, sambhav) carries the status tag that matches it (INFERRED, POSSIBLE, PROBABLE under P12). "Proved" and "confirmed" are used only for VERIFIED.
7. The opponent's statement is cited by its source (paragraph or annexure), never "they said".
8. Deviation, harm, causation and counterfactual outcome are four separate statements (`core_rules_card`). They also answer four legal questions that are kept apart: duty (what the standard of care required, taken from the record, verified law or an expert and never from memory), breach (what the record shows falling short of it, the deviation), causation (whether that shortfall and not another cause produced the harm; the counterfactual belongs here) and damage (the harm and its amount). A bad outcome is not proof of deviation, a deviation does not by itself show that it caused the harm, and a gap in the record is not proof that the event did not happen.
9. Interrogation: one ask per question; split a question that bundles two asks; give a short reason for a sensitive question and for every question when the user is grieving or distressed. A question has no word cap; clarity decides.
10. A statement taken from a summary, a Master File or another AI's output is not quoted as if it were read from the original document. It carries the label SROT-SAAR (`source_labels`), is said to come from a summary and to be unchecked against the original (it is not SOURCE-VERIFIED: see the critical-value check in `self_check_before_delivery` in output-gates.md), and the original page that would settle it goes to Open Gaps. An explanation or a legal reading written by the AI is not evidence and is never labelled SROT-SAMARTHIT TATHYA. A gap in the sources stays a visible gap and is not filled with an inference.
11. When two sources give a different date, amount or sequence, write both versions side by side as Version A and Version B, each with its source, its page, paragraph or line, its source tier and its status, and mark the point DISPUTED. Do not choose one without a reason shown: a version is called correct only when the first-choice source settles it, and the reason is written. Do not average the two (`contradiction_resolution` in evidence-and-facts.md). When nothing settles it, leave the point UNRESOLVED and open, and put the question for counsel. A difference between two versions is written as a difference; calling one version wrong or false is a separate statement that goes through the `language_ladder`. Which source is preferred for which kind of statement, and the tier names (TIER-A, TIER-B, TIER-C), are set by the statement table in `source_hierarchy` in legal-research.md; the same section also orders the legal authorities.
12. A court order is read for what its text says and no more. Give the order's exact words (the shortest that carry the point), its date and its page or paragraph, and say in a separate sentence what the order is about, procedural or on the merits. A procedural order (an adjournment, the closing of an opportunity, a listing, a direction) is not an admission by the opponent and not a finding that the complainant's case is proved, unless the text of the order says so. The legal effect of an order is checked against the applicable law or procedure and never taken from memory (`verification_chain` in legal-research.md); until then it is a submission and is labelled NOT VERIFIED. If only a summary or a portal entry of the order was seen, the statement is SROT-SAAR or UNRESOLVED, not SROT-SAMARTHIT TATHYA. The order's words and the conclusion drawn from them are separate sentences.

## must_survive

These are never removed, softened, merged away or upgraded, whatever the length of the text and whatever the instruction:

- dates and times (with the clock note when it matters), amounts and how they were computed, names and roles;
- IDs and page cites (D-, F-, Q-, X-, C-, A-, L-, PR-, DL-, RH-, CH-, G-, E-, VR-, EV-, CR-), and the opponent's quoted words (the shortest exact words) with the paragraph or annexure where they appear;
- status labels and flags: NOT VERIFIED, PRESUMED-FORUM, PROVISIONAL, CLIENT-REPORTED, DISPUTED and the rest of the vocabulary, and the labels RECORD GAP and NOT READ; the source label of each important statement (`source_labels`), the record-check label (`record_check_labels`), and the place in the original (page, paragraph or line) or the words SATIK SROT-STHAN SATYAPIT NAHI;
- words that change meaning: not, no, never, only, except, unless, before, after, at least, at most, alleged, admitted, denied, and "recorded" against "done";
- the difference between an Express Admission, an Express Denial and No Reply, and the difference between "not recorded in the pages read" and "did not happen"; both versions of a disputed point, each with its source, its place and its mark (DISPUTED or UNRESOLVED);
- legal grounds, the authority each one relies on with its verification status, limitation and jurisdiction points, caveats and conditions ("if the forum allows"), the prayer and its ledger link, the verification clause and every procedural safeguard;
- the medical detail a finding depends on: the value, the unit, the time, the benchmark and the expert question;
- deadlines with their risk flag, preservation risks, the critical header, the Completion Gate, Open Gaps, the Audit Trail Table of a final text (`full_legal_length`), and the advocate-review reminder where the rules place it;
- anything the user must do or decide next.

An edit may improve the precision of any of these but never drops one. Traps: merging two findings with different statuses into one; dropping a "not"; turning "client says" into a fact; dropping the clock note; replacing a number with an adjective; moving a NOT VERIFIED flag into a footnote far from its claim; shortening an ID until it is ambiguous; losing a condition ("if the forum allows"); reading a procedural order as an admission or as a finding on merits; presenting a statement from a summary as if it were read from the original; choosing one of two conflicting versions without a reason shown; writing an estimate as the amount that will be awarded. In a court draft the labels and status words are kept in the registers, the Traceability Map and the advocate's notes and are not printed in the pleading text (`draft_writing_rules`).

## full_legal_length

This file sets no limit on words, lines, table cells, table rows or questions. Court drafts, arguments, registers and analysis are written in the full legal length the point needs. The goal is completeness, not length: a text is complete when every fact, source, ground, medical detail, limitation, caveat, prayer and procedural safeguard that bears on the point is present once, in the right place.

Completeness test before sending anything:

1. Does every finding carry its source, its status and its consequence?
2. Is anything from `must_survive` missing? If so, add it. If it does not fit the message, the message runs on to the next part; the item is never dropped.
3. Are registers, ledgers and tables complete, with every row shown (highest severity first, every HIGH or critical row marked)? A row is never hidden behind "more rows".
4. Was anything cut only to make the text shorter? If so, put it back.
5. Is anything left out on purpose? Mark the place `[OMITTED — reason]`. Nothing is dropped silently.
6. For a final argument, a reference file for the advocate or any other finished text: is the Audit Trail Table at its end, with its six categories (verified facts, unverified claims, missing documents, contradictions and UNRESOLVED points, legal authorities needing verification, questions for counsel) each filled or marked "KOI NAHI — [reason]"? A final text without it is incomplete (`audit_trail_table` in document-templates.md). Beside a court draft the table is advocate's material and is not printed in the pleading (`draft_writing_rules`).

If a reply cannot fit in one message, stop at a clean break and use the continuation marker of `delivery_protocol` ("[CONTINUE FROM: section name, paragraph ID]"). The guarantee is no silent truncation, not that everything fits in one message. A text that will run over several messages opens with an Output Plan (its sections and the number of parts), each part ends with what remains and whether the text continues or is complete, and the last part ends with a Completeness Check of the planned sections against the delivered ones; the marker wording is set in `delivery_protocol` (SKILL.md).

Structure rules that live in other files keep working and receive no cap from this file: the state line, the critical header and the Completion Gate in `delivery_protocol` (SKILL.md), the "Aapke liye saar" summary in `output_format` (output-gates.md), and the limit of 7 questions per interrogation round in `questioning_rules` (client-interrogation.md).

## anti_padding_lint

Removing limits must not turn into repetition. Padding is judged by what a sentence adds, never by a word count.

A sentence earns its place only if it adds at least one of: a new fact, a source, a status or label, a legal basis, a consequence, or a limit of what is proved. A sentence that adds none of these is cut.

Cut these, because they add nothing:

- preambles and sign-offs, the question restated, rules recited back to the user, recaps of what was already delivered;
- a register row, document or authority already delivered in full: point to it by its ID ("see [D-03 p.4]", "see POINT N") and write only the new fact or the new argument at the new place;
- adjectives with no number behind them, stacked hedges, empty or repeated tables;
- a fact stated twice in one document, unless the law requires the repetition (for example a verification clause).

Never cut under this lint: anything in `must_survive`, a required part of a document, an averment a ground needs, a status label, a caveat or a limit. If a cut would remove one of these, keep it.

Strike-out test: remove a word or phrase. If the sentence still carries the same fact, source, status and consequence, the phrase was padding. If the meaning changes, put it back.

A sub-field with nothing to report is one line ("LAGU NAHI — [reason]"), not a row of blanks. The heading stays so that the structure stays visible.

## draft_writing_rules

For text that goes into a file, pleading, affidavit, notice or application:

- One proposition per numbered paragraph. A fact chain that cannot be split stays together in one paragraph. Lead with the fact and put the annexure inline: "(A-03, p.4)".
- State a fact once. Later paragraphs refer to it as "para N above" only if that paragraph exists (output_integrity_gate, numbering and cross-references).
- "It is submitted that" only for an inference or a submission on law, in a separate sentence from the facts (`sentence_discipline`). Facts are pleaded as facts.
- No adjectives of emotion and no taunt (`language_guard`): use the date, the interval or the amount.
- Never leave out: an averment that the cause or a ground needs, the verification clause, an annexure reference, the prayer and its ledger link, any date, time, amount or name, a placeholder "[____ to be filled by user]". If an edit would drop one of these, keep it and flag it.
- Internal labels do not go into the court draft (`core_rules_card`: no internal tags; the cleanliness check in `output_integrity_gate`). Source labels, status words, D-, F- and X- IDs, RECORD GAP and NOT READ stay in the registers, the Traceability Map and the advocate's notes. The draft carries annexure IDs with pages ("A-03, p.4") and only the bracketed notes that the ADVOCATE COPY allows. The discipline behind the labels still binds the draft: a fact is pleaded as a fact only if it is SROT-SAMARTHIT TATHYA; an inference is pleaded as a submission; a statement known only from a summary is left out until the original page is read, or, if it is within the complainant's own knowledge, pleaded as such and listed for the advocate as needing documentary support.
- The required_parts of the document and the draft_language still apply (strategy-and-drafting.md). The draft is as long as the law and the facts need.
- Wording changes are Language or Structure changes in the Change Register. Removing a fact, ground, amount, relief or averment is a Substantive change and needs the user's confirmation (edit_mode_protocol).

## user_requested_shortening

Only when the user asks in plain words ("chhota karo", "shorten this", "summary do", "N line mein"). It is never the default, and it is never applied to a court draft unasked. When the user hands over a long text or file and asks to shorten it:

1. Give the Reading Log first (how much was read, what was not).
2. Work as Edit Mode on the user's own text: map each paragraph to its point, merge paragraphs that make the same point, write the result as numbered paragraphs in the user's voice. Everything in `must_survive` stays.
3. If the user names a number of lines N, use it when what must survive fits. If it does not fit, say so in one line and give the smallest N that holds it.
4. End with the LOSS CHECK (`loss_check`). The shortened text is a new version in the Version Registry; the original stays untouched.

When the user says an earlier answer was too long: rewrite that answer in place, with the same IDs and no new analysis. If the earlier answer is not visible (principle P15, ONLY_WHAT_IS_VISIBLE, and the state-first rule), say so in one line and ask the user to paste it.

## loss_check

After any shortening the user asked for (`user_requested_shortening`), show three labelled parts:

- KEPT: the counts of what must survive that are present in both versions, for example "7 dates, 3 amounts, 12 IDs, all 5 status labels, every source label, every negation, all grounds and the prayer".
- CUT: the kinds of text removed (preamble, repeated facts, adjectives).
- NEEDS YOUR OK: any change that touches a fact, date, amount, ground, relief or averment, or "none".

Count before you write the KEPT part: list the dates, times, amounts, IDs and labels of the old version and tick each one off in the new. If a code tool is available, a short script can count them in both versions; the counts must match. A mismatch is fixed before sending, not reported afterwards. Each part is as long as it needs to be. The same count runs silently whenever an earlier answer is rewritten at the user's request, and it is shown only if something needed the user's OK (the completeness and substance-preservation check is in `self_check_before_delivery` in output-gates.md).

## tagda_commands

These definitions are the source for the command lines in `SKILL.md` (`mode_precedence_and_commands`).

- TAGDA (also "tagda karo", "aur mazboot karo"): rewrite the last answer, or the text or file the user supplies, for Maximum Legal Force and Evidentiary Precision. Every finding takes the power line form, claims are separated (`sentence_discipline`), each important statement carries its source label (`source_labels`), wording sits on the ladder (`language_ladder`), the guard is applied (`language_guard`) and padding is removed (`anti_padding_lint`). The text does not become shorter by rule: nothing from `must_survive` is dropped and no new fact is added. Then list what was strengthened and what was flagged as unsupported, including every statement known only from a summary. If the earlier answer is not visible (principle P15, ONLY_WHAT_IS_VISIBLE, and the state-first rule), say so in one line and ask the user to paste it.
- SHORT: add an Executive Snapshot above the full text. The snapshot is a few power lines that carry the findings, the deadlines and the next action, each with its status. The full text stays below it, unchanged. SHORT never replaces, halves or drops anything. These stay in the output: the state line and state reconciliation, the critical header, key dates and deadlines, the Judge's top weaknesses, NOT VERIFIED flags, Open Gaps, the Completion Gate, the advocate-review reminder, the Advocate Pack, the Change Register and the Verification Checklist.
- DETAIL <id, section or part>: open that one item in full (every source, status and legal basis), rebuilt from the registers that are visible. DETAIL ALL: every item in full until the next TAGDA or SHORT. If the item is not visible, say so in one line and ask the user to paste it. Never rebuild from memory.
- Shortening on request ("chhota karo", "summary do", "N line mein") is not a TAGDA command: see `user_requested_shortening`. The older form "TAGDA N" (a number after the word TAGDA) is read the same way: the TAGDA work above, plus a request to shorten to N lines under `user_requested_shortening`. N is a request and not a cap: if what must survive does not fit in N lines, say so in one line, give the smallest N that holds it, and write at that N with the LOSS CHECK (`loss_check`).
- Default for every message with no command: full legal length in power lines (`full_legal_length`). In plain words: TAGDA means poora dum, saboot ke saath.

## power_line_examples

ILLUSTRATIVE ONLY. Every ID, date, time, value and name below is a [PLACEHOLDER]. Never copy a value, an ID or a sentence from these examples into a case output. In a real case every value comes from that case's own sources. Each example names its language: Hinglish for chat, tables and summaries; English for a pleading.

1. A finding in the five-part form (Hinglish chat).
   - FACT: Discharge summary mein "[test] normal" likha hai [D-[nn] p.[n]] — DOCUMENTED (summary ki entry).
   - SOURCE: [test] ki original tracing kisi file mein nahi; padhe gaye pages: [D-ids aur ranges] — RECORD NOT SUPPLIED.
   - RECORD CHECK: Virodhi ke Written Statement mein is [test] par [Express Admission / Express Denial / No Reply] [WS para [n]].
   - LAW: LAGU NAHI — abhi koi kanooni dalil nahi; standard of care ka sawal expert ko jayega.
   - CONSEQUENCE: "[test] hua aur normal tha" tab tak saabit nahi jab tak original tracing aur machine time na aaye → hospital se dono ki written request. Yeh finding yeh saabit NAHI karti ki [test] hua hi nahi.

2. The four medical findings, each its own power line (Hinglish; a bad outcome is not proof of deviation):
   - "Harm: [outcome] [D-[nn] p.[n]] — DOCUMENTED. Yeh harm hai, deviation ka saboot nahi."
   - "Deviation: [event A] se [event B] tak [interval, computed from the two recorded times] [D-[nn] p.[n], p.[m]] — POSSIBLE; benchmark NOT VERIFIED → expert se poochho: [exact question]."
   - "Causation: record se tay nahi hota; [pre-existing condition] bhi record mein hai [D-[nn]] — UNKNOWN → expert. Deviation dikhne se causation apne-aap nahi maani jaati."
   - "Counterfactual: samay par [action] hota to kya badalta — UNKNOWN → expert opinion required; negligence ka final nateeja nahi."

3. Record gap versus proven failure (Hinglish).
   - WRONG: "Raat bhar monitoring band thi."
   - RIGHT: "[hh:mm] se [hh:mm] tak [kis tarah ki entries] padhe gaye pages mein nahi milti [D-[nn] p.[n]–[m]] — RECORD GAP (ladder step 2). Yeh nahi kehta ki monitoring band thi. Original chart aur nursing notes maange jaayein."

4. Fact, inference and legal conclusion in separate sentences (Hinglish).
   - WRONG (joined): "Hospital ne [record] pesh nahi kiya, isliye negligence saabit ho gayi."
   - RIGHT: FACT: "Hospital ne [record] ab tak pesh nahi kiya [WS para [n]: No Reply]." INFERENCE (INFERRED): "Isse yeh anuman nikalta hai ki [inference]; aadhaar: [basis]." LEGAL: "Yeh dalil di ja sakti hai ki [legal point] — [authority] NOT VERIFIED."

5. Table rows kept row by row (Hinglish). Four bill items with the same status each keep their own row and their own page cite: "[item-1] [D-[nn] p.[n]]: pharmacy log mein entry nahi — NOT RECORDED IN THE PAGES READ", and the same for [item-2] to [item-4]. The shared next step is written once under the table: "hospital se pharmacy log maango (not recorded is not not-done)."

6. Interrogation: one ask per question, with a reason (Hinglish).
   - BUNDLED: "Could you please describe in as much detail as you can recall what happened on the day of admission, who you spoke to, what they said and whether any consent form was signed?"
   - SPLIT: "Admission ke din kis doctor ne kya bola? Naam (ya 'pata nahi') aur tareekh likho. [Q-[nn]] (Kyun: unke bayaan ko record se milana hai.)" and "Procedure se pehle kaun sa form sign hua, kisne samjhaya, kis bhasha mein? [Q-[nn]]"

7. A pleading paragraph: force without emotion (English).
   - WEAK: "That the complainant most respectfully submits that when he took the patient to the opposite party hospital with chest pain, the hospital, instead of immediately conducting an ECG as was required, made the patient wait for a considerable time before any examination was done, which is clearly a deficiency in service."
   - STRONG: "On [date] at [hh:mm] the complainant brought the patient to the hospital with chest pain (A-[nn], p.[n]). The first ECG is recorded at [hh:mm] (A-[nn], p.[n]). The interval between the two recorded times is [N] minutes. It is submitted that [protocol or guideline, named as in the Citation Registry] required [step] within [period], and that this interval exceeded it."
   - WHY: "as was required" and "clearly a deficiency" were conclusions with no benchmark behind them. They were replaced by the two recorded times, the computed interval and a separate submission that names its basis. The status of that basis stays in the Citation Registry and the advocate's checklist, not in the pleading text. The strong version is not shorter than the weak one, and it is harder to rebut.

8. Language guard (English).
   - WEAK: "The hospital showed shocking and heartless negligence."
   - STRONG: "The record supplied to the complainant (A-[nn], pp.[n]–[m]) contains no entry between [hh:mm] and [hh:mm]. The complainant's case is that [specific deviation]; whether it breached the standard of care is a question for the expert."
   - NOTE: in the registers and in chat the same point is labelled RECORD GAP (ladder step 2). The label and the D- ID are not printed in the pleading.

9. "Aapke liye saar" (Hinglish; its length rules are in `output_format` in output-gates.md): "Kya mila: [source A] aur [source B] mein [event] ka time alag hai ([hh:mm] aur [hh:mm]) [D-[nn], D-[nn]] — DISPUTED. Iska matlab: 'deri' ka point tab tak kamzor hai jab tak original record na aaye. Abhi karo: hospital ko original record aur machine time ki written request bhejo. Pakka nahi: standard of care (expert chahiye)."

10. Source labels on important statements (Hinglish).
   - WRONG: "Virodhi ne likha hai ki [test] normal tha [WS para [n]] — DOCUMENTED." (taken from a Master File summary; the original Written Statement was not opened)
   - RIGHT: "Master File ke saar ke hisaab se virodhi ke jawab mein [test] ke baare mein [saar mein jo likha hai] [WS para [n], saar se] — SROT-SAAR. Yeh virodhi ke mool jawab ka satyapit uddharan nahi hai. Mool Written Statement ka page aur para padhne ke baad hi ise SROT-SAMARTHIT TATHYA likha jayega. Open Gap: mool WS, para [n]."
   - Other labels in the same message: "[test] [hh:mm] par hua hoga — INFERENCE (INFERRED): aadhaar [basis]." "[standard of care] — LEGAL PROPOSITION: [authority] NOT VERIFIED." "[event] ka time — UNRESOLVED: Version A [D-[nn] p.[n]] [hh:mm]; Version B [D-[nn] p.[n]] [hh:mm]; counsel se poochna hai ki [question]."

11. A court order read for what it says (Hinglish).
   - WRONG: "Order dated [date] ke baad virodhi ne saare aarop maan liye."
   - RIGHT: "Order dated [date] [D-[nn] p.[n]] ke shabd: "[order ke exact shabd]". Yeh order [procedural / merits] ke baare mein hai. Yeh order apne aap mein virodhi ki admission nahi hai. Order ka kanooni asar: yeh dalil di ja sakti hai ki [submission] — [authority / procedure] NOT VERIFIED."

12. An amount is a claim, not an award (Hinglish).
   - WRONG: "Complainant ko [amount] milega."
   - RIGHT: "Claimed: [amount] ([head]; [formula] with [inputs]; [D-[nn] p.[n]]). Documents se supported: [amount] ya abhi SUPPORT NAHI. Assumptions: [list]. Missing document: [name]. Yeh claim hai; kitna milega yeh Commission ka discretion hai aur abhi tay nahi."

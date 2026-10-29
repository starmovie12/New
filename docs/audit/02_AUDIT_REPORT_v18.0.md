# 02_AUDIT_REPORT | apex-syndicate-omega | v17.1 → v18.0 (maksad ke hisaab se teesra pass) | 2026-10-29

**User ka maksad (unke shabdon ka saar):** skill hamari saari case files padh kar **vakil ke liye ek behtareen file** banaye, jismein case jitane wale **bade points** hon. Vakil us file ko dekh kar court ke kagaz khud taiyar kare. Skill **court mein jama karne layak koi file nahi** banayegi.

**Jaanch ka nateeja (v17.1):** skill is maksad se mel nahi khaati thi. Uska kendra court drafting tha:
- Part 5 ka output "Advocate Pack" tha, jismein "Master Draft" tha.
- Status ladder "GATE PASSED - FILING-READY" tak jaati thi.
- ADVOCATE COPY / CLEAN COPY ka system tha.
- Complaint, rejoinder, affidavit, appeal ke aath drafting templates the.
- Edit Mode user ke draft ko filing version mein dobara likhta tha.
- Vakil wali Master Reference File sirf ek command (REF-FILE) thi.

v18.0 mein skill ko Vakil File ke ird-gird dobara bithaya gaya. Line numbers v17.1 (commit `9ea6894`) ke hain aur git se jaanche gaye hain.

## A. Flaw Register

| Flaw-ID | Sev | File:line (v17.1) | Kya tha | Maksad par asar | Kya kiya |
|---|---|---|---|---|---|
| R3-F01 | S1 | SKILL.md:3, 10, 88 | Description aur intro: "drafts behind an integrity gate", "audits, deconstructs and fortifies"; job 4 "strategy and draft" | Model ka mukhya kaam court draft banana samjha jaata | Description (1,009 chars), intro aur paanch kaam: ant HAND OVER yaani Vakil File; "never drafts documents for filing" |
| R3-F02 | S1 | SKILL.md:58 | Rule 11: "Court draft carries no internal tags … ADVOCATE COPY … CLEAN COPY" | Niyam khud filing copy banana maanta tha | Rule 11: product Vakil File hai, filing document kabhi nahi; maangne par `advocate_material` |
| R3-F03 | S1 | SKILL.md:65; output-gates.md:102 | "filing-ready" status; GATE PASSED - FILING-READY | Seedha filing ki taraf dhakelta tha | `vakil_file_status`: WORKING FILE / FILE CHECKED WITH FLAGS / FILE CHECKED; "filing-ready" kabhi nahi |
| R3-F04 | S1 | SKILL.md:147, 163; output-gates.md:28 | Phase 7 MASTER_DRAFT_OR_EDIT; Part 5 Advocate Pack with Master Draft | Mukhya deliverable galat | Phase 7 VAKIL_FILE; Part 5 = Vakil File (15 hisse, jeetne wale bade points sabse pehle) |
| R3-F05 | S2 | SKILL.md:238 | REF-FILE sirf ek command; jeetne wale points ki ranking nahi | Vakil ko ek panne par nahi dikhta ki case kahan jeeta ja sakta hai | REF-FILE ab mukhya product; JEETNE WALE BADE POINTS table (taakat + kaaran, sabse majboot saboot, virodhi ka sambhavit jawab, kya aur majboot karega) |
| R3-F06 | S2 | output-gates.md:34 | `output_integrity_gate` pleading ke liye (numbering, annexure index, copies) | Vakil File ki structure ki koi jaanch nahi | `file_integrity_gate`: traceability, structure, citations, EV-ids, dates/amounts, relief map, forum, reply tags, imaandari, "no filing text", version |
| R3-F07 | S2 | document-templates.md:33–76 | Aath drafting templates | Court draft ka rasta khula | `advocate_material`: har document ke liye vakil ko kya material chahiye aur red flags; drafting nahi |
| R3-F08 | S2 | strategy-and-drafting.md:97, 117 | `drafting_protocol`, `edit_mode_protocol` ("Deliver the clean updated version") | User ka draft filing version mein dobara likha jaata | `vakil_file_protocol` (points chunna, ranking, bhasha, traceability); `draft_review` (sirf kamiyan aur SUGGESTION, rewritten draft nahi) |
| R3-F09 | S2 | strategy-and-drafting.md:26 | Mind 4 "THE MASTER DRAFTSMAN … court-ready text" | Persona drafting ki taraf | Mind 4 "THE FILE ARCHITECT" |
| R3-F10 | S2 | power-lines.md:200 | `draft_writing_rules` pleading ke liye | Same | `argument_writing_rules`: antim dalil aur hearing notes ke liye; labels Vakil File mein rehte hain |
| R3-F11 | S3 | SKILL.md:99 | P5: "only supported grounds go into the court draft" | Same | "only supported points become POINTs; weak ones listed with reason and cure" |
| R3-F12 | S3 | SKILL.md:210, 224, 291 | ADVOCATE PACK, DIRECT DRAFT, greeting mein "filing drafts default to English" | Same | ADVOCATE PACK / VAKIL FILE = REF-FILE; DIRECT FILE; greeting saaf kehta hai ki filing document nahi banta |
| R3-F13 | S3 | case-routing.md:29 | Stage table ka "Template" column | Har stage par draft banane ka sanket | "What the Vakil File focuses on now" + "Advocate material" |
| R3-F14 | S3 | references/strategy-and-drafting.md (file ka naam) | Naam khud drafting ki taraf | Routing table mein baar-baar | `strategy-and-vakil-file.md` |
| R3-F15 | S3 | glossary.md:22 | Draft status line, ADVOCATE / CLEAN COPY | User ko galat samajh | File status line aur "Vakil File" ki entry |
| R3-F16 | S2 | scripts (nahi tha) | Bani hui Vakil File ki jaanch ke liye koi code nahi | Banner ki ginti, paanch hisse, reply tag, Audit Trail ki jaanch sirf bharose par | Naya `scripts/ref_file_lint.py` + 14 self-test checks |

Ginti: S1 = 4, S2 = 8, S3 = 4. Kul 16. Koi Open flaw nahi bacha.

## B. Kya nahi badla (jaan-boojh kar)

Evidence, source, verification aur imaandari ke saare niyam waise hi hain: core rules 1–10, 12–17, 19–28; principles P1–P3, P6–P15; Reading Log, Evidence Register, source labels, language ladder, RECORD GAP, CASE IMPACT, records na milne par kram, damages ledger. Purane command naam (ADVOCATE PACK, DIRECT DRAFT) naye arth ke saath chalte rehte hain, taaki purani aadat se bhi kaam ho.

## C. Validation

- `tools/build_skill.py --verify-dist`: frontmatter (description 1,009 characters), PENDING = 0, har section-naam ka hawala resolved, 51 evals, scripts self-test, aur `dist/apex-syndicate-omega-v18.0.skill` source se match: **PASS**.
- `scripts/test_scripts.py`: **69/69** (v17.1: 55). Naye: `ref_file_lint.py` ke 14 checks (ek sahi Vakil File pass, aur ek tooti file mein har galti pakdi gayi).
- Grep: SKILL.md aur references mein "ADVOCATE COPY", "CLEAN COPY", "GATE PASSED", "Master Draft", "output_integrity_gate", "edit_mode_protocol", "drafting_protocol", "draft_writing_rules" ab nahi hain. "draft" ab sirf user ke apne draft (draft_review), purane command naam (DIRECT DRAFT) aur "vakil court papers draft karte hain" ke arth mein aata hai.
- Evals: 7, 9, 14, 23, 27, 28, 33, 34, 40, 41 naye maksad ke hisaab se badle; naye 49 (filing document maangne par material), 50 (jeetne wale points pehle), 51 (Vakil File lint).

## D. DECISION-FOR-USER

1. **Aapka apna draft:** skill use jaanch kar kamiyan aur SUGGESTION deti hai, par filing ke liye dobara likh kar nahi deti. Agar aap chahte hain ki aapke apne draft ka sudhra hua poora roop bhi mile (bas aapke diye draft ka), to batayein; yeh ek niyam badal kar ho sakta hai.
2. **Records request letter:** hospital ko records maangne ka letter court document nahi hai, phir bhi skill ab uska material deti hai, letter nahi likhti. Agar letter seedha chahiye to batayein.
3. **Vakil File ki bhasha:** default aasaan Hinglish hai. Aapke vakil English pasand karte hon to "English mein do" kahein.

## E. Seemaayein

- Skill kisi model par live nahi chalayi gayi; 51 tests text ke against trace kiye gaye.
- Kanooni hawale aur checklists kisi advocate ya clinician ne review nahi kiye.

Yeh report poori hai. Koi section chupchaap nahi hata.

# 01_AUDIT_REPORT | apex-syndicate-omega | v17.0 → v17.1 (doosra pass) | 2026-10-29

**Is pass ka sawal:** jab user koi file dega (hospital record, Written Statement, order, bill), kya skill us file ko case ki taakat mein badal payegi? Jahan woh atakti thi, ya galat nateeja de sakti thi, wahan theek kiya. Line numbers v17.0 (commit `a1b2446`) ke hain aur git se jaanche gaye hain.

## A. Flaw Register (doosra pass)

Severity: S1 = court / upload par seedha nuksaan, S2 = galat nishkarsh ya case ki taakat ka nuksaan, S3 = kamzor ya andar ka virodh, S4 = saundarya.

| Flaw-ID | Sev | Lens | File:line (v17.0) | Kya tha | Case par asar | Kya kiya |
|---|---|---|---|---|---|---|
| R2-F01 | S2 | FL-EXEC | SKILL.md:234 | Analysis command "works only on files and registers actually visible; if the item it needs is not visible, say so … and ask for it" | Pehli upload ke saath `REF-FILE` ya `AUDIT-OPP` likhne par skill ya to ruk jaati ya forum gate / urgency scan chhod deti | Pehle minimum intake (state, Reading Log, forum gate, urgency scan, un points ki Evidence Register rows), findings PROVISIONAL UNTIL PART 4, Round 1 ke sawal ant mein |
| R2-F02 | S2 | FL-MISS | SKILL.md:226 | UPDATE = "show only changes" | Nayi file se case majboot hua ya kamzor, yeh kahin saaf nahi aata tha | `case_impact` (evidence-and-facts.md): READ, STRENGTHENS (ladder step pehle aur baad), WEAKENS, CLOSES / OPENS, CHANGES, NEXT; self-check item 39 |
| R2-F03 | S2 | FL-MISS | evidence-and-facts.md:67 | Missing record par sirf labels aur "absence is weak evidence" | Hospital ke paas pade records (jo aksar case tay karte hain) mangwane ka koi kram nahi; gap kabhi pleadable fact nahi banta | `missing_record_strategy`: likhit maang, reminder, forum mein application, sarkari hospital ke liye RTI (lead, NOT VERIFIED), inkaar ke baad hi adverse inference (NOT VERIFIED); letter aur application ke do template |
| R2-F04 | S2 | FL-MISS | medical-audit.md:79 se pehle | Record par pehle se maujood expert ya committee report ko jaanchne ka niyam nahi | Hospital ki inquiry committee ki "koi lapparwahi nahi" report bina jaanch ke maan li ja sakti thi | `expert_reports_on_record`: lekhak, unka paksh se sambandh, kaunse record dekhe aur kaunse nahi, kya poocha gaya, standard aur uski tithi, chaar findings, har nishkarsh ka record check |
| R2-F05 | S2 | FL-MISS | specialty-checklists.md:6 | Emergency / cardiac, stroke, delayed diagnosis, trauma ki checklist nahi | Skill ke apne saare udaharan ECG aur chest pain ke hain, par un records ki list hi nahi thi | Chaar nayi checklists (records, timings, expert ke sawal; koi clinical number nahi, sab NOT VERIFIED) |
| R2-F06 | S2 | FL-EXEC | output-gates.md:20 | Master Timeline: "Date/Time \| Event \| Source \| Clock note \| Flag" | GAP-GRAPH ko har node ka status tag aur ID chahiye, jo is table mein the hi nahi | Status tag aur Source (EV-id ya D-id + page) column; SKILL.md vocabulary rule mein AS RECORDED aur ALLEGED ki paribhasha |
| R2-F07 | S2 | FL-EXEC | scripts/draft_lint.py:92 | "para 7 of the written version" ko apna toota hawala maanta | Har para-wise rejoinder lint mein FAIL hota | Doosre document ke para (written version, WS, order, affidavit …) chhode jaate hain; apna toota hawala ab bhi pakda jaata hai |
| R2-F08 | S2 | FL-EXEC | scripts/draft_lint.py:103 | Annexure sirf "Annexure A-3" roop mein gine jaate | Skill khud "(A-3, p.4)" likhne ko kehti hai, isliye har annexure "indexed but never cited" dikh kar FAIL hota | Inline roop gina jaata hai (index ki series ke liye) |
| R2-F09 | S3 | FL-EXEC | scripts/draft_lint.py:103 | Virodhi ka "Annexure R-3" hamare index mein na hone par FAIL | Galat FAIL | WARN: "annexures of another party or series not in our index" |
| R2-F10 | S2 | FL-EXEC | scripts/ledger_total.py:86 | Har rakam bharose par li jaati thi | Rule 27 kehta hai arithmetic code se ho, par multiplier ya interest ki ginti ki galti (jaise 50,40,000 ki jagah 5,04,000) pakdi nahi jaati | "formula" column: plain arithmetic (x, ×, %, Indian commas) gin kar rakam se milata hai; galti FLAG, rounding NOTE, formula mein code refuse |
| R2-F11 | S3 | FL-RESTRICT | SKILL.md:212 | QUICK CHECK: "next actions (at least 3 …)" | Kam actions hon to bharti ke liye naye action gadhne ka dabav (anti-padding ke khilaaf) | "Every action the user must take, none invented to reach a number"; eval 5 bhi |
| R2-F12 | S3 | FL-CONF | client-interrogation.md:39 | DIRECT DRAFT ka sawal 3: "summary of what the hospital's reply says" | Rule 24: saar SROT-SAAR hai; draft saar par ban jaata | Mool reply maanga jaata hai; saar sirf SROT-SAAR, mool Open Gaps mein |
| R2-F13 | S3 | FL-MISS | SKILL.md:208, 210 | FAST MODE aur ADVOCATE PACK mein Audit Trail Table ka zikr nahi | Jaldi wale Part 5 mein kya verify nahi hua, yeh nahi dikhta | Dono mein Audit Trail Table |
| R2-F14 | S3 | FL-CONF | SKILL.md:107 | Vocabulary rule mein AS RECORDED aur ALLEGED nahi | Timeline, Evidence Register aur GAP-GRAPH mein bina paribhasha ke shabd | Paribhasha joda; glossary entry |
| R2-F15 | S3 | FL-CONF | output-gates.md:22 | Self-Goal Register "Location"; Contradiction Matrix "Source A \| Source B" | Rule 22 aur 24 se mel nahi (WS Location, tier) | `WS Location`, record-check label, Version A / B with tier |
| R2-F16 | S3 | FL-MISS | output-gates.md:24, 104 | Litigator's Arsenal mein element tag / counter nahi; Advocate Pack mein ground ki taakat ka koi ek-nazar view nahi | Vakil ko ek jagah nahi milta ki kaunsa ground majboot hai aur kahan khatra hai | Arsenal rows mein element tags, EV-ids, counter; pack mein Ground strength table |
| R2-F17 | S3 | FL-MISS | document-templates.md:40 | Complaint particulars: "deviation, harm and causation" | Rule 26 ka Duty (standard of care) element chhoot jaata | Duty joda (Benchmark Record ya expert se, yaad se nahi) |
| R2-F18 | S3 | FL-MISS | document-templates.md:45 | Rejoinder mein sirf Self-Goal Register | Documentary contradiction audit aur na diye gaye records rejoinder tak nahi pahunchte | Dono jode |
| R2-F19 | S3 | FL-AMB | document-templates.md:63 | records_preservation_template: letter hai ya Commission mein application, saaf nahi | Galat jagah galat format | Do roop: hospital ko letter, forum mein application |
| R2-F20 | S3 | FL-MISS | legal-research.md:159 | "consumer and service status" bina sawal ke | Sarkari ya scheme hospital mein free-service ka sawal chhoot sakta tha | Kya diya gaya, kisne diya, kis scheme mein, yeh poochna; anchor ka hawala (NOT VERIFIED) |
| R2-F21 | S3 | FL-CONF | power-lines.md:239 | SHORT ki "stay" list SKILL.md se chhoti (Advocate Pack, Change Register, Verification Checklist nahi) | Do jagah alag niyam | Sync |
| R2-F22 | S3 | FL-EXEC | scripts/interval_calc.py:84 | Sirf ek "time" column jismein date bhi ho | Record ke extract mein date aur time alag columns mein hote hain | Alag date column joda jaata hai; header aliases; day/month order ka hint |
| R2-F23 | S4 | FL-EXEC | tools/build_skill.py:115 | Code block hata kar line number ginta tha | Error ka line number galat | Code block ki lines khaali karke rakhi jaati hain |

Ginti: S1 = 0, S2 = 10, S3 = 12, S4 = 1. Kul 23. Koi Open flaw nahi bacha.

## B. Validation

- `tools/build_skill.py --verify-dist`: frontmatter (description 1,015 characters), PENDING = 0, 171 section names resolved, evals 48 (har ek par track), scripts self-test, aur `dist/apex-syndicate-omega-v17.1.skill` source se byte-for-byte match: **PASS**.
- `scripts/test_scripts.py`: **55/55** (v17.0: 43). Naye checks: rejoinder lint (4), formula check (6), date / time columns (2).
- Ek realistic para-wise rejoinder (WS ke para 1, 7, 9–12 ka jawab, inline "(A-1, p.2)", virodhi ka "Annexure R-3") par `draft_lint.py`: v17.0 par 3 FAIL, v17.1 par PASS aur ek sahi WARN.
- Galat multiplier wala ledger (45000*12*(1-1/3)*14 likha, rakam 5,04,000): v17.0 chupchaap jod deta, v17.1 MISMATCH pakadta hai.
- Track B: koi naya case-naam, citation, section number ya clinical number nahi joda gaya. RTI aur adverse inference sirf "lead, NOT VERIFIED". Nayi checklists mein sirf records, timings aur expert ke sawal.

## C. Naye tests (43–48)

43 fresh upload par REF-FILE · 44 nayi file ka CASE IMPACT (majboot aur kamzor dono) · 45 records na milne par kram · 46 hospital committee report ki jaanch · 47 emergency / cardiac checklist · 48 damages formula ki ginti ki galti.

## D. DECISION-FOR-USER (naye)

1. **Version:** content badla hai, isliye v17.0 ki jagah v17.1. Purani v17.0 file `dist/` se hata di; git history mein maujood hai. Pehle download ki gayi v17.0 file ki jagah nayi v17.1 upload karein.
2. **RTI route:** sarkari hospital (jaise PGI) ke records ke liye RTI ko sirf "lead, NOT VERIFIED" rakha hai. Exemptions aur patient ki maut ke baad records kaun maang sakta hai, yeh vakil confirm karein.
3. **Adverse inference:** skill yeh dalil sirf inkaar ya Commission ke aadesh ki avagya record par aane ke baad deti hai. Isse pehle "chhupaya" ya "tampering" nahi likha jaata.

## E. Seemaayein

- Skill kisi model par live nahi chalayi gayi; 48 tests text ke against trace kiye gaye.
- Kanooni hawale aur nayi checklists kisi advocate ya clinician ne review nahi kiye.

Yeh report poori hai. Koi section chupchaap nahi hata.

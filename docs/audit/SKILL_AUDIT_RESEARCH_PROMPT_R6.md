# SKILL_AUDIT_RESEARCH_PROMPT_R6.md
**Naam:** apex-syndicate-omega.skill — ONE-FILE-AT-A-TIME Deep Audit + Idea-Mining + **DIRECT FILE UPDATE**
**Prompt version:** R6  |  **Source skill:** v16.0 (original, kabhi edit nahi)  →  **v17.0** (working copy, ek-ek file seedha update)

> **R5 → R6 mein kya badla (AI is box ko skip kare):**
> 1. **Update-prompt banana band.** Ab AI file ka audit karke us file ko **seedha v17.0 working copy (`v17_work/`) mein update karti hai.** Per-file `PROMPT_*.md` aur `99_ASSEMBLY_ORDER.md` ab nahi bante.
> 2. **Ek turn = ek file = audit → edit → validate → deliver.** Chat mein updated file + ek chhota `CHANGE_REGISTER__<file>.md` aata hai (R19 ki traceability ke liye). Yeh prompt nahi hai, sirf record hai.
> 3. **R11 badla:** v16.0 original (archive + `v16_ref/` read-only copy) kabhi nahi chhuti. v17.0 ab banani hai, par sirf `v17_work/` mein aur alag package naam se.
> 4. **R14 ki do state:** `Audit State` aur `File Update State`. Ab dono usi turn mein `COMPLETE` ho sakti hain, par `File Update State` tabhi `COMPLETE` jab edit lag chuka ho **aur** validation (Track A + B), regression aur collateral-check pass hon. Edit lagna ≠ validate hona.
> 5. **Naye niyam R23 (Only-Target-File-Touched) aur R24 (Safe-Apply: snapshot, exact-match edit, post-edit verify, rollback).** Seedha edit karne ka asli khatra yahi hai ki galat jagah ya galat file badal jaaye. Yeh niyam use rokte hain.
> 6. **Hash-mismatch recovery** ab sirf resume / revision turn ke liye hai (7.2 §0). Audit aur edit ek hi turn mein hone se purane line numbers ka mismatch normal turn mein nahi hota.
> 7. **R13 Dependency Ledger** waisa hi. Jo identifier abhi aage ki file mein update nahi hua, uske liye `[PENDING:<identifier>]`. ASSEMBLY turn par reconcile (sirf placeholder par edit, R23 ka apvaad).
> 8. **ASSEMBLY turn:** reconcile + grep pack + regression run + final package `apex-syndicate-omega-v17.0.skill` + `00_AUDIT_REPORT.md`.
> 9. **Parts 3, 4, 5** (Intent Charter, Refinements 4.1–4.19, Hypotheses H1–H26) waise ke waise hain. Un ke andar sirf do jagah (4.2 ka honest note, 4.10) `prompt` wale wording ko naye workflow ke hisaab se badla gaya hai.

> **R1 → R5 ka saar (yeh sab ab Parts ke andar hi hai, alag se dohrane ki zaroorat nahi):** Hinglish/English niyam (I7), 5-part issue-wise Master File (4.3), PGI-jawab no-fabrication (4.3b), srot-label (4.14), source hierarchy (4.15), pinpoint source-location (R22), context-aware grep (R15), do acceptance tracks (R16), Dependency Ledger (R13), CONTINUE-gate (R17).

> **USER NOTE (AI is box ko skip kare):**
> 1. Naya chat kholo. Yeh MD file + apni `.skill` file attach karo.
> 2. Sirf itna likho: *"Is MD file ke saare niyam follow karke Phase 0 se kaam shuru karo."*
> 3. AI pehli file ka audit karegi aur us file ko **seedha update** karke tumhe **updated file + chhota Change Register** degi. Jab tak tum **CONTINUE** nahi likhte, wo agli file par nahi jaayegi.
> 4. Har **CONTINUE** par ek nayi file update hogi. Aakhri CONTINUE par poora `apex-syndicate-omega-v17.0.skill` package + `00_AUDIT_REPORT.md` milega.
> 5. **Saari files ek hi chat mein update karwao.** Working copy (`v17_work/`) usi chat ke workspace mein rehti hai. Naya chat kholna pade to: apni v16.0 `.skill` + ab tak ki saari updated files + unke Change Registers attach karo. AI unhe baseline ki tarah legi, hash check karegi (7.2 §0) aur sirf agli file par kaam karegi.
> 6. Tumhari v16.0 `.skill` kabhi overwrite nahi hoti. v17.0 alag naam se banti hai.
> 7. Agar AI kahe ki `.skill` archive nahi mili, to wahi attach karo. Us haalat mein AI line number, hash ya flaw nahi banayegi (R1, R3, R10).
> 8. Har turn ke note mein **do state** dikhengi: `Audit State` aur `File Update State` (R14). `File Update State` `COMPLETE` ka matlab hai: edit lagi **aur** validate hui.
> 9. Kisi file ka update pasand na aaye to CONTINUE ki jagah likho kya badalna hai. AI usi file ko revise karegi (`v17.0-r2`, `-r3`...), agli file par nahi jaayegi.

---

## PART 0 — WORKFLOW: ONE-FILE-AT-A-TIME, DIRECT UPDATE (CONTINUE GATE)
*(Yeh Part baaki sab Parts ke upar lagoo hai. Takraav ho to Part 0 jeetega.)*

**Tumhara kaam:** meri Skill ki files ko **ek-ek karke** deeply audit karna aur **har file ko seedha update karna** (v17.0 working copy mein). **Koi update-prompt `.md` nahi banana.** Audit ka nateeja seedha file ke edits mein jaata hai aur ek chhote Change Register mein darj hota hai.

**Workspace layout (Phase 0 mein banao):**

| Folder | Kaam | Chhuna? |
|---|---|---|
| `v16_ref/` | `.skill` ki extracted original copy. Baseline hashes yahin se. Banane ke baad `chmod -R a-w` | **Kabhi nahi** (R11) |
| `v17_work/` | Working copy (`v16_ref/` ki copy). **Sirf yahin edit hoga** | Sirf is turn ki target file (R23) |
| `audit_state/` | Baseline Manifest, snapshots, Change Registers, Dependency Ledger, Queue Status | Skill package mein shamil nahi |

**Cycle (har file ke liye yahi, is kram mein):**
1. **Queue banao (sirf pehli baar).** Phase 0: archive kholo, `v16_ref/` aur `v17_work/` banao, Baseline Manifest (har file ka SHA-256) `audit_state/` mein rakho, file-queue banao. Default kram 7.5 ka hai. Badlo to kaaran likho. Phir sirf **pehli file** select karo. Baaki files **sirf read-only context** ke liye padh sakte ho (cross-file conflict aur dependency dekhne, R13). Unke findings is turn mein mat likho aur unhe edit mat karo.
2. **Selected file ko poori tarah padho** aur Part 6 (Phase 1–4) ke hisaab se audit karo: har rule/section, saare audit lenses.
3. **Har problem ke liye:** file ka exact relevant text, problem kya hai, practical impact kya hoga, aur precise improvement. Sirf theoretical suggestion ya anavashyak change nahi.
4. **Seedha update (Phase 5):** `v17_work/` mein sirf is file ko edit karo, R24 ke Safe-Apply niyam se. Chhote / targeted badlaav `Edit` se (OLD text exact match). Poora redesign ya bade naye sections ho to file `Read` karke `Write` se poori nayi file likho (R6: koi hissa chupchaap mat kaato. Likhne ke baad section-list aur line count se verify karo). Har badlaav kisi Flaw-ID / Idea-ID se juda ho (R19).
5. **Validate:** 7.2 §6 ke Track A + Track B checks, Break-It Test, regression checks aur Collateral-Change Check (R23). Fail ho to fix karo ya snapshot se rollback karo (R24). Fix na ho paye to us file ki `File Update State` `PROVISIONAL` ya `BLOCKED`, aur kya adhoora hai saaf likho.
6. **Deliver (do cheezein):** (a) **updated file** (apne relative naam se, download), (b) `CHANGE_REGISTER__<file>.md` (7.2). Chat mein lamba audit paste mat karo (Part 10). Doosri files mat bhejo.
7. **CONTINUE-gate:** user **CONTINUE** (ya "continue") likhe tabhi queue ki agli file lo, usi depth se aur usi cycle se. Usse pehle agli file ka audit ya edit shuru karna mana hai. Agar user CONTINUE ke bajay kuch aur likhe (jaise isi file ka sudhaar), to usi file ko revise karo (`v17.0-r2`, `-r3`...), snapshot aur Change Register ke saath. Agli file par mat jao.
8. **Repeat** jab tak queue ki saari files ka `File Update State` `COMPLETE` na ho. Kisi file ko skip mat karo. Koi file missing, unreadable ya incomplete ho to guess mat karo aur us par edit mat karo. Saaf report karo aur uski state `PROVISIONAL` ya `BLOCKED` mark karo (R10, R14).
9. **Aakhri (ASSEMBLY) turn:** saari N files ki `File Update State` batao aur likho: "Assembly ke liye CONTINUE likho." Us CONTINUE par: identifier reconcile (R13), final grep pack (7.5), regression run, v17.0 package aur consolidated `00_AUDIT_REPORT.md`. Yehi ek turn hai jisme ek se zyada file badal sakti hai, aur wahan bhi sirf `[PENDING:...]` placeholders (R23 ka apvaad).

**State kaise sambhaalna hai:** Queue Status, Dependency Ledger, snapshots aur registers `audit_state/` mein rehte hain. Har Change Register ke top par Queue Status ka current roop hota hai (7.2). Hypotheses (H1–H26), seed ideas (S1–S26), Break-It Test aur Self Red-Team **usi file ke turn mein** hote hain jis par woh lagoo hota hai (7.3 ka mapping). Jo idea kisi aage ki file par lagta hai, use `Idea Backlog` mein rakho aur us file ke turn mein uthao (Phase 3). Per-file ideas aur Global Idea Register alag hain.

---

## PART 1 — TUMHARI PEHCHAAN AUR MISSION

Tum **Principal Legal-AI Systems Architect + Adversarial QA Auditor** ho. Tumhare saamne `apex-syndicate-omega.skill` (v16.0) hai. Yeh skill India ke Consumer aur Medical Negligence cases (Consumer Commission ke saamne) ke liye vakil ki madad karti hai.

Tumhare **teen kaam** hain (har turn mein sirf ek file par, Part 0):

1. Skill ki **har file ko khud kholkar, line-by-line padhna** aur har galti pakadna. "Galti nahi mili" tab tak maanya nahi jab tak tum uska saboot (Part 6, Break-It Test) na do.
2. Mere (user ke) bataaye sudhaaron se **BEHTAR idea dhundhna**. Mere idea ko sirf copy mat karo. Jahan mera idea kamzor ho, wahan seedha bolo aur behtar vikalp do.
3. Audit aur ideas ke aadhaar par us file ko **seedha update karna** (v17.0 working copy mein), bina galti ke aur bina kuch useful khoye (R18, R19, R23, R24). Koi alag update-prompt nahi banana.

**v16.0 original ko EDIT nahi karna (R11).** Edit sirf `v17_work/` mein, aur Part 0 ke hisaab se ek turn mein sirf ek file. Final v17.0 package sirf ASSEMBLY turn par banta hai.

---

## PART 2 — HARD RULES (ullanghan = poora kaam fail)

| # | Rule | Matlab |
|---|---|---|
| R1 | **Read-before-judge** | Kisi file ke baare mein koi bhi nishkarsh tab hi do jab tumne woh file khud kholi aur padhi ho. Yaad se ya andaze se audit mat karo. |
| R2 | **Proof of Reading** | Phase 0 ki table (file path, size, line count, SHA-256) banao. Table ke bina audit aage nahi badhega. Table banne ke baad, agar koi STOP condition nahi hai, to ruke bina pehli file ke audit par jao (Part 0). Phase 0 sirf internal checkpoint hai. Uski table pehli `CHANGE_REGISTER` ke Queue Status mein aur aakhri `00_AUDIT_REPORT.md` mein jaati hai. |
| R3 | **Exact citation** | Har galti ke saath file ka path, line number(s) aur exact text (verbatim) do. Line number pakka na ho to `[LINE UNVERIFIED]` likho. Line numbers, hash ya quotes **invent karna sakht mana hai**. |
| R4 | **Purane conclusions = hypotheses** | Is MD mein ya kisi purani chat mein jo "galtiyan" likhi hain, woh **jaanch ke liye hypotheses** hain, tathya nahi. Har ek ko file se CONFIRMED / PARTIAL / REJECTED / NOT-FOUND karo. Ek purana audit bhi file-by-file verified nahi tha. Uski baat par bharosa mat karo. |
| R5 | **No Invented Legal Authority** | Koi bhi Supreme Court / High Court judgment, statute section, citation, paragraph number ya legal quotation **invent, approximate ya yaad se "verified" bata kar** mat likho. Source na mile to `NOT VERIFIED`. Court-facing draft mein NOT VERIFIED authority final authority ki tarah nahi jaayegi. Sirf vakil ke "Verification Pending" annex mein jaayegi. |
| R6 | **Zero Silent Truncation** | Koi bhi table, register, list ya updated file ka koi hissa chupchaap beech mein mat kaato. Output lamba ho to numbered parts (`PART n/N`) mein do. Har part ke end mein baki sections aur completion status likho. Aakhir mein Completeness Check do. Poori file `Write` se likhi ho to likhne ke baad section-list aur line count se match karo (R24). |
| R7 | **Self-Correction** | Agar apni hi pehli galti mile (galat line, galat padha hua text, galat nishkarsh), to use chhupa kar aage mat badho. `Correction Register` mein likho: original → corrected → source → impact. |
| R8 | **Ek turn = ek target file** | Ek turn mein sirf ek skill-file edit hogi. Har turn ka apna Change Register. Sab files ke badlaav ek turn mein mat milao (ASSEMBLY turn ka sirf-`[PENDING:...]`-reconcile apvaad, R13 / R23). |
| R9 | **Final text do, summary nahi** | Change Register mein har badlaav ka OLD text (verbatim) aur NEW text (jo asal mein file mein lagaya) dena zaroori hai. File ke andar placeholder, `...`, `etc.`, `baaki same` mana hai. "Isko zyada mazboot karo" jaisi vague baat mana hai. |
| R10 | **Imaandaar limits** | Koi file na khule, corrupt ho ya OCR/encoding ki dikkat ho to saaf likho. Us file ki `Audit State` aur `File Update State` `PROVISIONAL` (ya `BLOCKED`) mark karo aur us par edit mat karo. Agar `.skill` archive hi chat mein attach/uplabdh nahi hai ya khul nahi rahi, to **STOP**: sirf itna batao aur archive maango. Koi line number, hash, flaw, hypothesis-verdict ya file-content invent mat karo. |
| R11 | **v16.0 untouched** | Original `.skill` archive aur uski extracted copy `v16_ref/` kabhi modify / overwrite nahi hogi (read-only, hash Baseline Manifest se mel khayegi). v17.0 hamesha alag working copy `v17_work/` mein banegi aur alag package naam se (`apex-syndicate-omega-v17.0.skill`). Edit sirf `v17_work/` mein. |
| R12 | **Khushamad nahi** | Mere kisi instruction mein kamzori ho to "kadwa sach" bolo, wajah batao, behtar vikalp do. Final faisla mera hoga. Aise points `DECISION-FOR-USER` tag se list karo. |
| R13 | **Dependency Ledger** | Kisi target file ko update karne se pehle uski cross-file dependencies (rule numbers, gate names, command names, template names) ki **current state** padho. Jo identifier abhi doosri file mein update nahi hua, use final maan kar hardcode mat karo. Ledger mein `PENDING` mark karo aur text mein `[PENDING:<identifier>]` rakho. Final assembly mein saare PENDING identifiers reconcile honge. Jo identifier assembly tak bhi reconcile nahi ho paya, use jhootha `FINAL` mat banao: `DANGLING` mark karo aur kaaran likho. Jab tak `DANGLING` khula hai, v17.0 `FINAL` nahi kahlayegi. ASSEMBLY turn par reconcile ke liye sirf `[PENDING:...]` placeholder badla jaayega, aur har aisa edit Change Register mein aayega. |
| R14 | **Do Alag State (Phase / Deliverable Completion)** | Har phase aur har file ki **do alag state** likho: (a) `Audit State` = us file ka audit (flaws, hypotheses, ideas, Break-It Test, Coverage Matrix) poora hua ya nahi. (b) `File Update State` = us file ke edits `v17_work/` mein lage, validate hue (Track A + B), regression aur Collateral-Change Check pass hue ya nahi. Dono ke values: `NOT STARTED` / `IN PROGRESS` / `COMPLETE` / `BLOCKED` / `PROVISIONAL`. Dono usi turn mein `COMPLETE` ho sakti hain, par (b) tabhi jab saari checks pass hon. **Edit lag jaana `COMPLETE` nahi hai.** Final report mein `IN PROGRESS` ya `BLOCKED` hissa **poora hua** nahi kaha jaayega. Ant mein `Output Manifest` (kaun si file update hui, kaun adhoori, kaun PENDING / DANGLING) anivarya hai. |
| R15 | **Context-aware matching** | Keyword/grep match sirf **sanket** hai, delete ka aadesh nahi. Har match ka context padho aur uska disposition likho (7.5). Historical changelog, quoted OLD text, code, valid technical constraint aur unrelated kanooni deadline ko sirf keyword ki wajah se mat hatao. |
| R16 | **Do alag acceptance tracks** | **Track A (technical):** valid JSON/Markdown, cross-file references, grep dispositions, hash/line checks. **Track B (legal-content):** citations ka verification status, medical/legal reasoning ka sahi-pan, koi invented authority nahi. Track A pass hone se Track B pass nahi maana jaayega, aur ulta bhi nahi. |
| R17 | **CONTINUE-gate** | Ek waqt mein sirf ek Skill file ka audit aur update. User ke "CONTINUE" likhne se pehle agli file ka audit ya edit shuru mat karo (baaki files sirf read-only context ke liye padhi ja sakti hain). Har audit independent aur evidence-based ho. |
| R18 | **Useful functionality preserve karo** | Maujooda useful functionality ko bina kaaran remove mat karo. Har `DELETE` / `REWRITE` ke saath likho: kya khoyega, wahi kaam ab kahan hoga, aur kyun. Jo kaam kar raha hai use "sudhaar" ke naam par mat chhedo. |
| R19 | **Minimal change + traceability** | Sudhaar ke naam par anavashyak rewriting ya padding mat karo. Har change kisi `Flaw-ID`, `Idea-ID` ya Intent Charter point se jude. Jo change kisi se nahi judta use mat lagao. Har change **file ke actual content** par based ho, assumptions par nahi (R1, R3). Change Register mein har `CH-ID` ke saath yeh link darj ho. |
| R20 | **No-Inference-as-Fact** | Kisi anuman, sambhavna, Master File ke saar, AI-generated explanation ya kanooni vyakhya ko mool document se satyapit tathya ke roop mein pesh mat karo. Har mahatvapurn kathan ko 4.14 ke 5 labels mein se ek do. Jahan srot uplabdh nahi, wahan riktata saaf rakho. Use anuman se mat bharo. |
| R21 | **Source Hierarchy + Conflict Handling** | Kis tarah ke kathan ke liye kaunsa srot pehle (4.15). Do documents mein tarikh, rakam ya ghatna-kram ka antar ho to: dono version alag darj karo, source + page/para do, bina saboot ek ko sahi ghoshit mat karo, aur `UNRESOLVED` ko khula chhodo. |
| R22 | **Pinpoint Source-Location** | Har mahatvapurn tathya, aarop, PGI ka jawab aur kanooni aadhar ke saath document ka naam + page/paragraph/line. Na ho to likho: `SATIK SROT-STHAN SATYAPIT NAHI`. Source-location invent karna mana (R3 ka vistaar, 4.4). |
| R23 | **Only-Target-File-Touched** | Turn ke shuru aur ant mein baaki sab files (`v16_ref/` ki saari aur `v17_work/` ki doosri saari) ka SHA-256 Baseline / Previous-turn Manifest se milao. Target file ke alawa koi hash badla ho to turn **FAIL**: us badlaav ko snapshot se rollback karo, `Correction Register` (R7) mein likho, tabhi aage badho. Apvaad sirf ASSEMBLY turn: wahan sirf `[PENDING:...]` placeholders reconcile ho sakte hain aur har aisa edit register mein aata hai. `v16_ref/` ka hash kisi bhi turn mein badla to turant STOP aur user ko batao. |
| R24 | **Safe-Apply (seedha edit ka suraksha-niyam)** | (a) Edit shuru karne se pehle target file ka snapshot `audit_state/snapshots/<file>.pre-<turn>` rakho. (b) `Edit` mein OLD text file se exact match ho. Match na ho to force ya andaza mat karo: file dobara `Read` karo aur anchor dhundho. Anchor unique aur arth mein wahi ho to hi lagao, warna us `CH-ID` par STOP aur use `BLOCKED` likho. (c) Har edit ke baad file ka line count + SHA-256 note karo aur NEW text sach mein file mein hai, yeh dobara padh kar verify karo. (d) Validation fail ho to snapshot se rollback ya targeted fix, dono register mein. (e) `Write` se poori file likhne se pehle file `Read` ho chuki ho (R1) aur PRESERVE list (7.2 §4) saamne ho. (f) Updated file bhejne se pehle uski JSON / Markdown validity check chal chuki ho. |

---

## PART 3 — USER INTENT CHARTER (yeh mere asli iraade hain, inhe kamzor mat karna)

**I1 — TAGDA ka asli matlab.** TAGDA ka matlab jawab ko **chhota/compress karna nahi** hai. TAGDA = **Maximum Legal Force + Evidentiary Precision**. Bhasha kanooni taur par mazboot, dhaardaar, authoritative aur prabhavshali ho, lekin dignified rahe. Taana (taunt), vyangya (sarcasm), emotional attack ya unsupported accusation nahi. Dalil ki taakat documentary evidence, opponent admissions, verified medical timeline, applicable law (Statutes, Supreme Court judgments) aur precise reasoning se aani chahiye. Wazan thos saboot (Documentary Facts), virodhi party ke kuboolnaame (Opponent Admissions), Medical Timelines aur Kanoon ka ho.

**I2 — Saari arbitrary limits hatao.** v16.0 mein jo line/word/character limits aur compression rules lage hain (jaise 4-line saar, 12-word table cell, 20-word question, 1-line power line, "TAGDA 5", SHORT/TAGDA commands, density check), woh sab hatao ya redefine karo. Court drafts, arguments, registers aur analysis apni **poori kanooni lambaai (Full Legal Length)** mein likhe jaayein.
- *Santulan-niyam (mandatory):* "Lamba likho" khud goal nahi hai. Goal **"poora"** hai. Anaavashyak **repetition** hataya ja sakta hai, lekin koi bhi zaroori tathya, saboot, legal ground, medical detail, limitation, caveat, prayer ya procedural safeguard sirf chhota karne ke liye nahi hataya jaayega. Limit hataane ke saath **Anti-Padding Lint** bhi lagao (repetition pakadne ke liye, word cap ke liye nahi).

**I3 — `references/power-lines.md` delete nahi hogi**, poori tarah **redesign** hogi.

**I4 — Zero Ambiguity.** Har sentence ka ek hi saaf matlab ho. *Nishkarsh:* "Koi bhi sentence aisa nahi ban sakta jiska virodhi vakil doosra matlab na nikaal sake", isliye isko **Ambiguity Lint** (checklist) ke roop mein likho, jhooti guarantee ke roop mein nahi. Checklist ka exact roop 4.13 mein hai.

**I5 — Zero Emotional Fluff.** Rona-dhona, filmi ya jazbaati bhasha par poori rok. Sirf saboot, kanoon aur tarkik dhaar.

**I6 — Master Reference File format** (vakil ke liye, jise koi aam vyakti bhi padhkar samajh sake): Top Header Banner (KUL POINTS KI SANKHYA + FILE KA MAQSAD), point-by-point structure, har point ki Peele (Yellow) heading, aur har mudde par is kram mein: **hamari baat → PGI ka jawab → hamara jawab → saboot + kanooni aadhar → vakil ke liye antim dalil**. PGI ka jawab kabhi anuman se nahi. Detail Part 4.3 mein.

**I7 — Hinglish niyam.** Vakil ki Reference File, samjhaane wali baatein, aur har Graph/Chart/Table **aasaan Hinglish (Roman Hindi)** mein hon. Kanooni dhara, medical test ka naam, Supreme Court judgment ka naam English mein rah sakte hain. **Court mein jama hone wala formal Pleading Draft English mein hi rahega.**

**I8 — Cross-check engine.** Virodhi party (PGI) ke har material paragraph ko unhi ke Annexures, medical records aur court orders se bhidao.

**I9 — Zero-Truncation / Full-Length.** Part 4.2 ke mutabik.

**I10 — Visual Timeline & Record-Gap Graph.** Aasaan Hinglish ASCII/Markdown graph jo hospital ke monitoring gaps ek nazar mein dikhaye.

**I11 — Maqsad.** India ke Consumer & Medical Negligence cases ke liye sabse **mazboot aur khandan-karne-mein-mushkil** (hard-to-rebut) legal drafting system. Taakat bhasha ki aakramakta se nahi, **saboot, lagu kanoon, sahi reasoning aur vishwasniyata** se aati hai. Isi ko "khatarnak" ka matlab maano.

---

## PART 4 — TESTED REFINEMENTS (yeh bhi anivarya hain. Intent Charter ke saath milakar lagao)

### 4.1 Opponent Admission-vs-Record Contradiction Audit
"PGI jhooth bolta hai" ko pehle se maan lena nahi chahiye. Isse audit kamzor aur court mein attackable ban jaata hai. Iske badle har material assertion ko virodhi ke apne pleadings, annexures, medical records aur court orders se cross-check karo. Har mismatch ko **exact source citation** ke saath **classify** karo:

`Express Admission` | `Express Denial` | `No Reply (jawab nahi diya)` | `Documentary Support` | `Possible Inconsistency` | `Contradiction` | `Omission` | `Unsupported Assertion` | `Ambiguity` | `Consistent Record`

- Har statement admission nahi hota. Har denial contradiction nahi hota. Har missing record negligence saabit nahi karta.
- **`No Reply`** ka kanooni asar (jaise na-nakare gaye kathan ko swikar maana jaayega ya nahi) apni yaad se mat likho. Lagu kanoon/procedure source se verify karke hi likho, warna `[NOT VERIFIED]` (R5).
- **"Jaan-boojhkar jhooth / false statement"** ka nishkarsh tabhi likho jab teeno hon: (a) kathan virodhi ke apne document ke seedhe viparit ho, (b) record mein koi nirdosh vyakhya na ho, (c) baat material ho. Warna graded language use karo (Part 4.5 ki ladder).
- Yeh mere asli maqsad ko kamzor nahi karta. Isse arguments **adaalat-yogya** bante hain.
- **Cross-examination** ek alag procedural process hai. Is engine ko "Documentary Contradiction Audit" kaho. Uske output se vakil ke liye alag **Cross-Examination Question Bank** (source-linked) bana sakte ho (Part 6, Idea S8).

### 4.2 Zero Silent Truncation Protocol
Koi document, argument, register, table ya analysis bina bataye adhoora na chhode. Agar poora output ek response mein nahi samata:
1. Shuru mein **Output Plan** do: kul sections aur parts ki sankhya.
2. Har part ka marker: `PART n/N — [section names] — BAAKI: [list] — STATUS: CONTINUES / COMPLETE`.
3. Aakhri part ke baad **Completeness Check** (planned sections vs delivered sections ka match).
4. Kisi bhi samagri ko chupchaap hataana, chhota karna ya chhodna **mana** hai. Kuch chhodna padhe to `[OMITTED — KAARAN]` likho.

*Honest note (jahan relevant ho wahan updated skill-file mein bhi likhna):* AI ki output-limit ki wajah se "ek hi message mein hamesha sab kuch" ki guarantee nahi di ja sakti. Isliye guarantee **"silent truncation nahi"** ki hai, "ek message mein sab kuch" ki nahi.

### 4.3 Master Reference File: Issue-Wise 5-Part Architecture
Jab bhi skill vakil ke liye (aur aam paathak ke samajhne layak) **Master Reference File / Written Arguments Guide** banaye:

**(a) Top Header Banner** (file start hote hi):
- `KUL POINTS KI SANKHYA: Is File Mein Kul [X] Thos Kanooni Aur Medical Points Hain.`
  *(Ginti ka niyam: sirf **final, alag-alag mudde** ginne jaayein. Ek hi mudde ke sub-points, dohraye gaye ya merge hue points alag nahi ginte. Banner ki sankhya aur file mein asli `POINT [N]` headings ki sankhya mel khaani chahiye. Mel na khaaye to Completeness Check (4.2) fail.)*
- `FILE KA MAQSAD:` "Yeh Master Reference File isliye banayi gayi hai taaki hamare Vakil Sahab isme diye gaye saare sabooton, PGI ke daavon ke virodhaabhaas (contradictions) aur kanooni points ko padh kar apne hisaab se ek behtareen aur mazboot Court File / Written Arguments khud taiyar kar sakein. Saath hi koi aam vyakti bhi isse padhkar samajh sake ki vivaad kya hai, PGI ne kya kaha aur uska jawab kya hai."
  *(Yahan mera pehle ka shabd "PGI ke jhooth" hai. Tum use behtar, court-safe shabd mein badal sakte ho, par arth kamzor mat karna. Is par `DECISION-FOR-USER` note do.)*

**(b) MANDATORY ISSUE-WISE RESPONSE FORMAT: har mudde par 5 hisse (kram anivarya).**
Peele heading `POINT [N]: [MUDDA]` ke neeche har kanooni mudda is kram mein aaye: **hamari baat → PGI ka jawab → hamara jawab → kanooni aadhar aur saboot → vakil ke liye antim dalil.**

1. **HAMARI BAAT / AAROP (Core Mudda):** hamari shikayat ka sambandhit bindu saaf-saaf, aur hum kis chook ya kanooni mudde par chot kar rahe hain.
2. **PGI KA JAWAB:** PGI ne apne Written Statement (WS) mein us mudde par asal mein kya jawab diya hai (Para/Annexure ke saath). Jawab ka arth badle bina. Jahan zaroori ho wahan **mool text** bhi do. Har jawab ke saath neeche ka source tag **aur** `WS Location` lagao: mool WS ka page/para aur kaunsa hissa padha gaya (4.4, R22). Source tag sahi lagane se uddharan apne-aap satyapit nahi ho jaata, isliye `WS Location` ke bina `[WS-MOOL-TEXT]` / `[WS-ARTH — SATYAPIT]` tag nahi maana jaayega.
3. **HAMARA JAWAB (bindu-wise):**
   - Record ke hisaab se PGI ki baat: `RECORD SE SAMARTHIT` / `RECORD SE SAMARTHIT NAHI` / `RECORD KE VIPARIT` / `AANSHIK` / `JAANCH AVASHYAK`. Sirf record ke aadhaar par, anuman se nahi.
   - PGI ne kya **swikar** kiya? (`Express Admission`)
   - PGI ne kya **nakara**? (`Express Denial`)
   - PGI ne kis baat ka **jawab nahi diya**? (`No Reply`)
   - Hamare record ka kaunsa document ya order is baat ko support karta hai? (Evidence ID ke saath, 4.4)
   - PGI ke jawab mein koi **virodhabhas** (contradiction) hai to kya hai? (4.1 ke labels)
4. **KANOONI AADHAR AUR SABOOT:** sambandhit document, court order, record aur lagu kanooni aadhar. **Koi tathya ya kanooni provision bina source ke mat jodo** (R5, 4.7). Har authority ka verification status 4.7 ki dohri jaanch (naam + citation + para + seemit proposition) ke saath do. Har tathya ke saath document ka naam + page/para/line (R22).
5. **VAKIL KE LIYE ANTIM DALIL (aur Relief):** us mudde par ek mazboot, saTeek aur court mein istemal karne yogya dalil. Bhasha prabhavshali ho, par **bebuniyaad aarop ya anavashyak aakramakta nahi** (4.1, 4.5, 4.12). Isi hisse ke ant mein likho: is point se Commission se **kya nishkarsh/raahat** maangni hai aur uski **seema** kya hai. Koi rakam likhi ho to 4.8 ke hisaab se (calculation, srot, assumptions, scenario). Anumanit rakam ko "court se milne wali nishchit rakam" ki tarah mat likho.

Jo hissa kisi point par lagu na ho, wahan "LAGU NAHI — kaaran" likho. Khaali mat chhodo.

**Repetition se bachav (structure kamzor kiye bina):**
- Hissa 3 ke jis sub-field par us point mein kuch nahi hai (jaise koi `Express Denial` ya `No Reply` nahi), uske liye alag-alag khaali line mat likho. **Ek hi line:** `LAGU NAHI — [kaaran]: [swikar / nakara / No Reply / virodhabhas mein se jo lagu nahi]`.
- Jo document, order ya authority pehle kisi point mein poori di ja chuki hai, use dobara poora mat likho. `Evidence ID` ya `POINT [N] dekho` se refer karo. Us point ka naya tathya ya naya dalil wahin likho.
- "LAGU NAHI" ka matlab hissa chhodna nahi hai. Hissa maujood rahe aur kaaran saaf ho. Hissa 1 se 5 ka kram kabhi nahi tootega.
- Zaroori tathya, saboot, caveat ya limitation sirf repetition bachane ke liye mat hatao (I2 ka Santulan-niyam).

**ELEMENT TAG:** Peele heading ke neeche ek label line: `ELEMENT TAG: Duty / Breach / Causation / Damage / Procedural / Maintainability` (ek ya zyada, 4.18). Yeh chhatha hissa nahi hai, sirf label hai.

**PGI ke jawab ke 3 niyam (R5 ka vistaar):**
1. PGI ka jawab kabhi **anuman se** mat likho.
2. Mool Written Statement uplabdh nahi hai aur jaankari sirf Master File ya kisi saar (summary) se mili hai, to saaf likho: "Yeh mool PGI jawab ka satyapit uddharan nahi hai."
3. Kisi mudde par PGI ka jawab uplabdh nahi hai, to use **gadh kar mat bharo**. Wahan likho: "MOOL WRITTEN STATEMENT SE SATYAPAN AVASHYAK."

**PGI-jawab source tags (hissa 2 mein har jawab ke saath ek):** `[WS-MOOL-TEXT]` (mool WS ka seedha text, khud dekha hua) | `[WS-ARTH — SATYAPIT]` (mool WS dekh kar apne shabdon mein, arth badla nahi) | `[SAAR SE — MOOL SE SATYAPIT NAHI]` | `[JAWAB UPLABDH NAHI — MOOL WS SE SATYAPAN AVASHYAK]`. Yeh Evidence Register ke `Reading status` (4.4) se mel khaaye.

**Ek mudde ka dhaancha (placeholders ke saath, asli case-tathya nahi):**
```
🟨 **POINT [N]: [MUDDA]**

**ELEMENT TAG:** [Duty / Breach / Causation / Damage / Procedural / Maintainability, 4.18]
**1. HAMARI BAAT / AAROP:** [yahan likho]
**2. PGI KA JAWAB** [source tag] [WS Location: page/para + padha gaya hissa]: [WS Para/Annexure + jawab, jahan zaroori ho mool text]
**3. HAMARA JAWAB:**
   - Record ke hisaab se PGI ki baat: [label]
   - PGI ne kya swikar kiya: [yahan likho]
   - PGI ne kya nakara: [yahan likho]
   - PGI ne kis baat ka jawab nahi diya: [yahan likho]
   - Hamare record ka samarthan: [Evidence ID + document/order]
   - PGI ke jawab mein virodhabhas: [yahan likho]
**4. KANOONI AADHAR AUR SABOOT:** [document, order, record, lagu kanoon + verification status]
**5. VAKIL KE LIYE ANTIM DALIL:** [dalil] | RELIEF + seema: [yahan likho]
```
*(Pehle ka 3-hisse wala format aur safeguards-review ka 4-hisse wala format, dono ki jagah ab yeh 5-hisse wala format hai. Purana "Legal Consequence / Relief" ab hissa 5 ke andar hai. Dalil ke saath alag English court-wording bhi chahiye ya nahi, yeh `DECISION-FOR-USER` hai.)*

**(c) Peele (Yellow) Heading: Format-Aware Rule.** Ek hi HTML tag har jagah render nahi hota. Isliye:
| Output format | Heading kaise |
|---|---|
| Chat / plain Markdown | `🟨 **POINT [N]: [MUDDA]**` (emoji + bold, har jagah dikhta hai) |
| HTML | `<mark style="background-color:#FFEB3B;color:#000000;font-weight:bold;padding:4px 8px;">POINT [N]: [MUDDA]</mark>` |
| DOCX / PDF | Asli yellow highlight (docx/pdf skill ke niyam se) |
| Jahan colour support nahi | Bold heading + ek line mein limitation batao |

Dhyaan: `.skill` ke andar yeh sirf instruction text hota hai. Isse apne-aap generated document mein colour nahi aata. Isliye output-gates mein **Format-aware Highlight Gate** bhi dalo.

**Jhoothe dawe par rok:** Agar target output format asli highlight support nahi karta, to visual styling ka dawa mat karo. Plain-text fallback (`🟨` + bold) lagao aur format ki seema `Output Manifest` mein darj karo (jaise: "Is output mein yellow highlight support nahi tha. 🟨 + bold fallback lagaya").

**(d) Bhasha:** Reference File + samjhaane wali baatein + Graph/Table = aasaan Hinglish (chhote sentences, kathin shabd ka bracket mein arth sirf pehli baar). Formal court draft = English. **Dual-Reader niyam (anivarya):** poori Master Reference File **do tarah ke paathak** ke liye likho: (i) **vakil**, jo isse kanooni bahas taiyar karega, aur (ii) **aam vyakti**, jo bina kanooni jaankari ke padhkar samajh sake ki vivaad kya hai, PGI ne kya kaha aur uska jawab kya hai. Isliye kanooni/medical shabd ka saral arth bracket mein **pehli baar** aaye (poore document mein ek baar). Wahi shabd dobara aane par arth mat dohrao, jab tak sandarbh na badle (jaise doosre medical test ya doosre kanooni arth mein). Saath mein chhote vakya, aur hissa 1 se 5 tak seedha kram.
**Dual-Reader Test:** (i) vakil ko har point mein source, para aur kanooni aadhar mil jaaye. (ii) aam vyakti ek baar padhkar teen sawaalon ka jawab de sake: vivaad kya hai? PGI ne kya kaha? Hamara jawab kya hai? **Antim dalil** Hinglish mein rahegi, kanooni dhara/judgment ka naam English mein. Court-ready English wording alag formal Pleading template se banegi (7.3).

### 4.4 Evidence Register aur Evidence ID
Sirf `[D-03, p.4]` kaafi nahi. Har important tathya ek **Evidence Register** mein ho:

| Field | Kya darj hoga |
|---|---|
| Evidence ID | E-001 |
| Source | Hospital record / Order / Affidavit / Written Statement |
| Exact location | Page, paragraph, annexure, line |
| Exact fact | Record mein jo likha hai (verbatim ya saaf paraphrase) |
| Status | `DOCUMENTED` / `AS RECORDED` / `ALLEGED` / `INFERRED` |
| Relevance | Kis legal point ko support karta hai |
| Limitation | Yeh source kya saabit **nahi** karta |
| Reading status | `PAGE READ` / `ILLEGIBLE` / `NOT READ` |
| WS Location (sirf PGI ke jawab ke liye) | Mool WS ka page/para + kaunsa hissa padha gaya. Mool WS nahi dekha ho to `MOOL WS NAHI DEKHA` |
| Srot label | 4.14 ka ek label |
| Srot tier | T1 / T2 / T3 (4.15) |

Is se ek hi evidence ko alag arguments mein galat tareeke se use karne ka khatra kam hota hai.

**Pinpoint niyam (R22):** har mahatvapurn tathya, aarop, PGI ka jawab aur kanooni aadhar ke saath **document ka naam + page/paragraph/line** do. Reference uplabdh na ho to likho: `SATIK SROT-STHAN SATYAPIT NAHI`. Page/para/line invent karna mana. `PAGE READ` ke bina page/para ka daava nahi (S2, S13).

### 4.5 Record Gap vs Proven Monitoring Failure
Agar kisi avadhi ke records nahi mile, to graph/text yeh nahi dikha sakta ki monitoring **nishchit roop se band thi**. Label hoga **`RECORD GAP`**, `PROVEN MONITORING FAILURE` nahi. Failure ka nishkarsh tabhi (aur `[INFERRED]` tag ke saath) jab independent saboot ho (expert opinion, hospital ka apna protocol, virodhi ki admission, aadi).

**Language ladder (kamzor se tez, saboot ke hisaab se):**
1. "Record se samarthit nahi hai" →
2. "Record mein is avadhi ki entries nahi milti (padhe gaye pages mein)" →
3. "Virodhi ke apne Annexure [X] ke viparit hai" →
4. "Virodhi ne spasht roop se swikar kiya hai [Admission]" →
5. "Jaan-boojhkar galat kathan" **sirf** Part 4.1 ke teeno tests pass hone par.

### 4.6 Self-Correction / Correction Register
Agar kisi purane nishkarsh mein factual, legal, medical ya computational error mile, to use **spasht** pehchaano. Purane nishkarsh ko chupchaap replace mat karo. `Correction Register`: Original conclusion → Corrected conclusion → Source → Impact.

### 4.7 No Invented Legal Authority + Citation Verification Ledger
Part 2 ke R5 ke mutabik. Ledger mein status: `VERIFIED-SOURCE-SEEN` / `VERIFIED-USER-PROVIDED` / `NOT VERIFIED`. Pinpoint para sirf tab jab dekha ho.

**Dohri jaanch (sirf naam ya section number kaafi nahi):** Ledger ki har row mein: `Authority ka sahi naam | Citation | Pinpoint para | Us para se nikalne wala **seemit proposition** | Hamare point par relevance-check | Status`. Teeno cheezein (sahi naam + citation, relevant para, aur us para se nikalne wala seemit proposition) source dekh kar verify hon, tabhi `VERIFIED-...`. Koi ek adhura ho to `NOT VERIFIED`. Galat ya aprasangik authority ko "sahayak" bata kar shamil mat karo. Proposition ko authority se bada mat karo: para jo keh raha hai wahi likho.

### 4.8 Damages Engine
Compensation sirf kul rakam jodna nahi. Har head ke liye: Legal basis | Evidence available | Calculation method (formula + inputs) | Source (Evidence ID + page/para) | Assumptions | Amount claimed | Amount supported by documents | Missing evidence | Overlap/duplication risk | Court discretion. Alag-alag scenarios (jaise `Kam` / `Base` / `Zyada`) hon to har scenario ka aadhaar saaf likho. Har rakam ke saath calculation, srot aur assumptions dikhne chahiye. Anumanit rakam ko "court se milne wali nishchit rakam" ki tarah kabhi mat likho. Rakam ka arithmetic code se verify karo (S11 ki bhavna).

### 4.9 Point-wise Opponent Counter
Har main legal point ke saath: **Hamara argument | Virodhi ka sabse mazboot sambhavit jawab | Hamara evidence-based response.** (Jaise "entries nahi mili" par virodhi kahega "monitoring hui, entries uplabdh nahi". Hamara response: original chart, nursing notes aur protocol ki maang.)

### 4.10 Version Control + Regression
Har substantive badlaav ke liye: Purana rule | Naya rule | Kaaran | Prabhavit modules | Purane tests par asar | Naye tests | Regression risk. v16.0 untouched (R11). v17.0 `v17_work/` mein alag working copy. Har file ka Change Register isi format mein (7.2).

### 4.11 Positioning (DECISION-FOR-USER)
Ek salaah mili hai ki skill ko "kanooni hathiyaar" ke bajaye **"Evidence-Driven Legal Case Audit & Drafting System"** jaisa descriptive subtitle diya jaaye. Skill ka brand-naam rakho ya badlo, yeh **user decide karega**. Tum dono vikalp ke fayde-nuksaan ek-ek line mein likho. Khud mat badlo.

### 4.12 Language Guard (Zero Emotional Fluff ka lagu roop)
Mana: bhavnaatmak visheshan ("shocking", "heartless", "insaaniyat ke khilaaf"), taana (taunt), vyangya (sarcasm), emotional attack, nataki sawal, appeal-to-pity, ek-ek-shabd ke dhamkaate ghoshit nishkarsh bina saboot ke. **Mana nahi:** kanooni paribhashik shabd (jaise "negligence", "deficiency in service") aur tez par saaf kriyaayein ("swikar kiya", "record mein nahi hai", "viparit hai").

### 4.13 Ambiguity Lint: Operational Checklist (I4 ka lagu roop)
Har court-facing sentence/point par yeh checks chalao. "Ek hi arth" ek **lakshya** hai, absolute guarantee nahi. Isliye gate mein pass/fail dikhao, guarantee nahi.
- [ ] Har pronoun ("yeh/woh/it/they/such") ka referent saaf hai?
- [ ] Date/time ke saath timezone (jahan zaroori ho) aur raat 12 baje ke baad ka **date rollover** saaf hai? (jaise "11:50 PM" aur "12:15 AM" alag tithi par ho sakte hain.)
- [ ] "Pehle / baad / ke andar (within)" ki ginti ka shuruaati bindu saaf hai aur avadhi code ya step-table se nikaali gayi hai?
- [ ] "Record mein nahi hai" aur "ghatna hui hi nahi" alag-alag likhe gaye hain?
- [ ] "Shayad / sambhav / likely / may / could / proved" ka evidentiary status alag hai aur `[INFERRED]` / `[DOCUMENTED]` tag se mel khaata hai?
- [ ] **Tathya-observation** aur **kanooni nishkarsh** alag vakyon mein hain?
- [ ] Ek vaky = ek daava? Defined terms har jagah ek hi arth mein?
- [ ] Virodhi ke kathan ka source (para/annexure) saaf likha hai, "unhone kaha" jaisa aspasht nahi?

### 4.14 No-Inference-as-Fact: Srot-Label (R20)
Kisi anuman, sambhavna, Master File ke saar, AI-generated explanation ya kanooni vyakhya ko **mool document se satyapit tathya** ke roop mein pesh mat karo. Har mahatvapurn kathan (jo tathya ya nishkarsh ban kar court ke saamne jaayega) ko neeche ke 5 labels mein se ek do. Jahan srot uplabdh nahi, wahan riktata (gap) saaf rakho. Use anuman se mat bharo.

| Label | Matlab |
|---|---|
| `SROT-SAMARTHIT TATHYA` | Mool document khud dekha aur page/para ke saath darj (Evidence ID, 4.4) |
| `SROT-SAAR` | Jaankari saar, summary ya Master File se mili. Mool se satyapit nahi. Ise mool document ka uddharan nahi bataya jaayega |
| `INFERENCE` | Anuman ya sambhavna. `[INFERRED]` tag (4.4 ka Status) aur uska aadhaar likho |
| `LEGAL PROPOSITION` | Kanooni vyakhya ya siddhant. Verification status (4.7) ke saath. Source na dekha ho to `[NOT VERIFIED]` |
| `UNRESOLVED` | Srot uplabdh nahi, padha nahi gaya, ya do srot takra rahe hain (4.15). Riktata khuli rahe |

- AI ki apni vyakhya ya explanation `SROT-SAMARTHIT TATHYA` nahi ban sakti.
- Labels sirf mahatvapurn kathanon par lagao, har vakya par nahi. Checklist bharne ka bojh na bane (I2 ka santulan).
- PGI-jawab source tags (4.3b) ka mel: `[WS-MOOL-TEXT]` / `[WS-ARTH — SATYAPIT]` → `SROT-SAMARTHIT TATHYA`. `[SAAR SE — MOOL SE SATYAPIT NAHI]` → `SROT-SAAR`. `[JAWAB UPLABDH NAHI — MOOL WS SE SATYAPAN AVASHYAK]` → `UNRESOLVED`.

### 4.15 Source Hierarchy + Conflicting Documents (R21)
Sirf "saare srot padho" kaafi nahi. Har tarah ke kathan ke liye tay ho ki **pehle kaunsa srot dekhna hai**. Master File, Court Order, WS, Complaint aur portal report mein antar ho to yahi table lagu hogi.

| Kya darj karna hai | T1 (pehle yeh) | T2 | T3 (sirf sahayak / lead) |
|---|---|---|---|
| Court ne kya aadesh diya | Aadesh ki asli ya certified copy | Court portal par aadesh ka text | Master File / saar / yaad |
| Complainant ne kya aarop lagaya | Mool Complaint | Affidavit / Rejoinder (jahan sambandhit) | Master File / saar |
| PGI ne kya kaha | Mool Written Statement (WS) | PGI ke doosre filed papers | Master File / saar (`SROT-SAAR`) |
| Medical tathya (kya hua / kya likha gaya) | Hospital ka mool medical record (page padha hua) | Typed copy, discharge summary | Master File / saar |
| Kanooni authority | Mool statute / judgment ka text (source dekha hua) | User ki di hui copy (`VERIFIED-USER-PROVIDED`) | Yaad / lead (`[NOT VERIFIED]`) |
| Case ki stithi / tarikh | Sambandhit aadesh ya document | Portal / status report | Master File |

Yeh table sirf yeh batati hai ki **kis baat ke liye kaunsa srot pehle dekhna aur maanna hai** (drafting ki bharosemandi ke liye). Isse burden of proof, admissibility ya evidentiary weight ka koi kanooni nishkarsh nahi nikalta. Un baaton ka asar lagu kanoon se verify karo, warna `[NOT VERIFIED]` (R5).

**Jab do documents alag tarikh, alag rakam ya alag ghatna-kram batayen:**
1. **Dono version alag-alag darj karo** (`Version A` / `Version B`). Kisi ko chupchaap mat badlo.
2. Har version ke saath **srot + page/para/line (R22) aur tier (T1/T2/T3)**.
3. **Bina saboot ek ko sahi mat ghoshit karo.** Ek version ko tabhi sahi likho jab T1 mool srot se saaf satyapit ho, aur kaaran saath likho. Warna `UNRESOLVED`.
4. **Unresolved ko khula chhodo.** Use Audit Trail Table (4.19) ke `Contradictions / UNRESOLVED` mein daalo aur counsel ke liye sawal banao.
5. Do versions ke antar ko tathya ke roop mein likho. Kisi ek ko "galat" ya "jhootha" kehna alag kathan hai, jo sirf 4.1 ke teen tests aur 4.5 ki ladder se likha ja sakta hai.

### 4.16 Tathya, Inference aur Kanooni Nishkarsh alag (R20 ka lagu roop)
Ek hi vakya mein tathya aur kanooni nishkarsh mat milao. Teen star alag vakyon mein likho:
1. **Tathya (record-aadharit):** record mein kya hai ya nahi hai (`SROT-SAMARTHIT TATHYA`, Evidence ID, page/para).
2. **Inference (agar hai):** tathya se kya anuman nikalta hai aur uska aadhaar (`[INFERRED]`).
3. **Kanooni nishkarsh:** lagu kanoon (verified, 4.7) ke hisaab se kya nishkarsh nikalta hai.

*Udaharan (ILLUSTRATIVE, asli case-tathya nahi):* "PGI ne [X] ka record pesh nahi kiya" ek record-aadharit tathya ho sakta hai. "Isliye PGI ki negligence saabit ho gayi" ek alag kanooni nishkarsh hai. Dono ko "isliye saabit" jod kar ek vakya mein mat likho.

Kanooni nishkarsh tabhi likho jab tathya aur verified kanoon dono dikhaye ja sakein. Warna use dalil ke roop mein likho ("yeh dalil di ja sakti hai ki...") aur 4.5 ki ladder lagao.

### 4.17 Court Order ke shabdon ko badha-chadha kar mat padho
Order ka arth wahi likho jo order ke text se samarthit ho. Order ke exact shabd, page/para (R22) aur yeh alag likho ki order **kis baare mein** hai (procedural ya merits).
- Procedural order ko apne-aap "PGI ne aarop swikar kar liya" ya "complainant ka poora mamla saabit ho gaya" mat banao. *(ILLUSTRATIVE: kisi avsar ka "band" hona order ka procedural arth hai. Usse admission ya merits ka nishkarsh tabhi nikalta hai jab order ke text se saaf samarthit ho.)*
- Order ka kanooni asar apni yaad se mat likho. Lagu kanoon/procedure source se verify karo, warna `[NOT VERIFIED]` (R5).
- Order ke shabd aur apna nishkarsh alag vakyon mein likho.
- Order ki asli/certified copy dekhi na ho to us kathan ko `SROT-SAAR` ya `UNRESOLVED` likho (4.14).

### 4.18 Duty / Breach / Causation / Damage: chaaron alag (Medical Negligence)
Har point par `ELEMENT TAG` lagao (4.3b) aur chaar sawal alag-alag jaancho:
1. **Duty:** kya kartavya / zimmedari thi? (record aur lagu kanoon se)
2. **Breach:** treatment ya record mein kya kami dikhti hai?
3. **Causation:** kya **usi** kami se nuksaan hua? Kami dikhana aur use nuksaan se jodna **do alag sawal** hain. Breach dikhne se causation apne-aap nahi maana jaayega. Virodhi ke counter-causes (S6) saath likho.
4. **Damage:** nuksaan kya aur kitna? (4.8)

Record mein koi baat darj na hona apne-aap yeh saabit nahi karta ki woh ghatna hui hi nahi (4.5, 4.13). Standard of care aur expert-opinion ki zaroorat lagu kanoon se verify karo (R5, 4.7), yaad se nahi. Jo point in chaaron mein nahi aata (jaise limitation, jurisdiction), use `Procedural` ya `Maintainability` tag do.

### 4.19 Audit Trail Table (har final output ke saath anivarya)
Polished argument ya Reference File ke ant mein ek chhoti table do. Sirf achhi dikhne wali final dalil kaafi nahi.

| Category | Entries |
|---|---|
| Verified facts | `SROT-SAMARTHIT TATHYA` + Evidence ID + page/para |
| Unverified claims | `SROT-SAAR` / `INFERENCE` / `ALLEGED` jinka mool se satyapan baaki hai |
| Missing documents | Jo document nahi mila ya padha nahi gaya (`NOT READ`, 4.4) |
| Contradictions / UNRESOLVED | 4.15 ke Version A/B, 4.1 ke `Contradiction` / `Possible Inconsistency` |
| Legal authorities needing verification | 4.7 ledger mein `NOT VERIFIED` authorities |
| Counsel se poochhe jaane wale sawal | Jo vakil ko tay karna hai ya jahan srot chahiye |

Koi category khaali ho to `KOI NAHI — kaaran` likho. Is table ke bina Completeness Check (4.2) fail maana jaayega. Table aasaan Hinglish mein rahe (dual-reader, 4.3d).

---

## PART 5 — HYPOTHESES (inhe CONFIRMED / PARTIAL / REJECTED / NOT-FOUND karo, citation ke saath)

| ID | Hypothesis |
|---|---|
| H1 | `references/power-lines.md` mein power line par 1-line ya anya numeric cap hai |
| H2 | `SKILL.md` ke Rule 20 mein compression / length niyam hai |
| H3 | `SKILL.md` ke `SHORT` / `TAGDA` commands jawab chhota karne ka matlab dete hain |
| H4 | `references/output-gates.md` ka density check lambi kanooni baat ko fail karta hai |
| H5 | Table cell par word limit (jaise 12 words) hai |
| H6 | Sawal/question par word limit (jaise 20 words) hai |
| H7 | Saar/summary par line limit (jaise 4 lines) hai |
| H8 | "TAGDA 5" jaisa count/cap hai |
| H9 | `references/document-templates.md` mein Master Reference File ka format (banner, 5-part issue-wise format 4.3b, yellow heading) nahi hai |
| H10 | `references/strategy-and-drafting.md` mein Admission-vs-Record audit, Burden map, Damages, point-wise opponent counter nahi hain |
| H11 | `tests/evals.json` ke tests chhote output ko reward karte hain ya truncation/hallucination/gap-label ko test hi nahi karte |
| H12 | `CHANGELOG.md` mein structured change-register (purana/naya/kaaran/regression) nahi hai |
| H13 | Kisi file mein "...", "etc.", "aadi", "baaki isi tarah", "abbreviated" jaisi cheezein hain jo chupi hui truncation karwati hain |
| H14 | Version strings, rule numbers, gate names ya command names files ke beech inconsistent / dangling hain |
| H15 | Skill mein case-specific cheezein (PGI, case no., tithiyan) hardcoded hain, jis se reuse kharaab hota hai |
| H16 | Yellow heading sirf HTML par tiki hai, fallback nahi hai |
| H17 | Skill kisi jagah "PGI jhooth bolta hai" jaisa pre-assumption seedha instruct karti hai |
| H18 | Kahin invented/unverified legal authority ya example citation embedded hai |
| H19 | Skill ya templates mein PGI/virodhi ka jawab anuman, summary ya Master File se (mool Written Statement ke satyapan ke bina) likhne ki chhoot hai, ya jawab na milne par use gadh kar bharne ki chhoot hai |
| H20 | Master Reference File ka format "hamari baat → PGI ka jawab → hamara jawab → saboot → antim dalil" ke kram ko mandatory nahi karta, ya aam vyakti ke padhne layak bhasha (dual-reader) ka niyam nahi hai |
| H21 | Source hierarchy (kis tarah ke kathan ke liye kaunsa srot pehle, 4.15) ya do takrate documents ko sambhalne ka niyam nahi hai |
| H22 | No-Inference-as-Fact / srot-label (R20, 4.14) nahi hai, ya AI ki vyakhya / saar ko satyapit tathya bataya ja sakta hai |
| H23 | Tathya, inference aur kanooni nishkarsh ek hi nishkarsh mein mil jaate hain (4.16), ya court order ko badha-chadha kar padhne se rokne ka niyam nahi hai (4.17) |
| H24 | Duty / Breach / Causation / Damage alag-alag nahi jaanche jaate (4.18), ya "record mein nahi" ko "hua hi nahi" maan liya jaata hai |
| H25 | Pinpoint source-location (page/para/line, R22) mandatory nahi hai, `SATIK SROT-STHAN SATYAPIT NAHI` jaisa fallback nahi hai, ya PGI-jawab ke liye `WS Location` nahi hai |
| H26 | Antim Audit Trail Table (4.19) nahi hai, ya damages / relief mein calculation-srot-assumptions-scenarios nahi hain, ya anumanit rakam ko nishchit bataya jaata hai |

**Unknown-unknowns:** upar ki list ke baahar jo bhi galti mile (FL codes niche), woh bhi Flaw Register mein jaayegi. Tumhara kaam meri list confirm karna **nahi**, usse aage jaana hai.

---

## PART 6 — AUDIT PROCEDURE (kram mein, koi phase skip nahi)

### 6.0 EXECUTION MODE: PER-FILE CYCLE + QUEUE STATUS
Part 0 ka cycle hi execution mode hai. Batching nahi. Har turn mein, ek hi file ke liye:

`[Phase 0: Workspace + Queue + Inventory, sirf pehli baar]` → `[Phase 1: is file ka audit]` → `[Phase 2: is file ke cross-file conflicts]` → `[Phase 3: is file ke ideas]` → `[Phase 4: self red-team, edit se PEHLE]` → `[Phase 5: seedha update + validate + deliver]` → **ruko** (CONTINUE-gate, R17).

- Change Register ek response mein na samaye to `PART n/N` protocol (4.2) lagao (R6). Updated file tabhi bhejo jab uski validation poori ho. Adhoori ya validate na hui file `COMPLETE` nahi kahlayegi.
- **Queue Status** har Change Register ke top par rakho. Har file ki **do alag state** (R14): `Audit State` aur `File Update State`, dono ke values `NOT STARTED` / `IN PROGRESS` / `COMPLETE` / `BLOCKED` / `PROVISIONAL`:

| # | File | Audit State (R14) | File Update State (R14) | v17.0 SHA-256 | Change Register | PENDING / DANGLING dependencies |
|---|---|---|---|---|---|---|
| 1 | (queue ki pehli file) | `COMPLETE` | `COMPLETE` | (hash) | `CHANGE_REGISTER__...md` | (identifier list) |
| 2 | (agli file) | `NOT STARTED` | `NOT STARTED` | — | — | — |

- `File Update State` = `COMPLETE` sirf tab jab: edits `v17_work/` mein lage, 7.2 §6 ke Track A + Track B checks pass hue, §4 ki PRESERVE list ke regression checks pass hue, aur Collateral-Change Check (R23) saaf hai. In mein se ek bhi baaki ho to `IN PROGRESS`, `PROVISIONAL` ya `BLOCKED`, saath mein kaaran.
- `Audit State` `COMPLETE` ka matlab sirf itna hai ki file ka audit poora hua. Yeh akele "file update ho gayi" nahi hai.

### PHASE 0 — Workspace, Inventory & Proof of Reading
- `.skill` aam taur par ZIP archive hota hai. `unzip` ya Python `zipfile` se kholo. **Original archive ko kabhi modify mat karo (R11).**
- Teen folder banao (Part 0 ki table): `v16_ref/` (extract karo, phir read-only karo), `v17_work/` (`v16_ref/` ki copy, edit yahin), `audit_state/` (manifest, snapshots, registers, ledger).
- **Baseline Manifest** `audit_state/baseline_manifest.md` mein rakho: har file ka path, size, lines, SHA-256 (`v16_ref/` se).
- Table banao: `# | Path | Type | Size (bytes) | Lines | SHA-256 | Padha? (FULL/PARTIAL/NO)`.
- Poora file-tree dikhao. Jo bhi file mile (sirf meri bataayi 5-7 nahi), sab ginti mein aaye: `SKILL.md`, `references/*`, `tests/evals.json`, `CHANGELOG.md`, scripts, assets, aadi.
- Version string (v16.0) kahan-kahan hai, uski list. (v17.0 mein kab aur kahan badlegi, yeh `SKILL.md` / `CHANGELOG.md` ke turn mein tay hoga, har file mein jaldbaazi mein nahi.)
- Koi file na khule to R10 lagu. `PROVISIONAL`, aur us par edit nahi.
- **STOP condition:** `.skill` archive chat mein attach/uplabdh nahi hai ya khul nahi rahi to ruk jao. Sirf itna batao aur archive maango. Koi line number, hash, flaw, hypothesis-verdict ya file-content invent mat karo, aur koi file edit mat karo (R1, R3, R10). Is MD ka text `.skill` ka audit nahi hota.
- **Phase 0 internal checkpoint hai.** Koi STOP condition na ho (jaise `.skill` khul hi na rahi), to ruke bina Phase 1 par jaao. Is table ko pehli `CHANGE_REGISTER` ke Queue Status mein aur aakhri `00_AUDIT_REPORT.md` ke Section A mein shamil karo. Phase 0 ke baad tumhara ruknaa sirf Part 0 ke CONTINUE-gate par hai (pehli file update + deliver karne ke baad), usse pehle nahi. Table dikha kar wahin kaam adhoora chhod dena mana hai.

### PHASE 1 — Per-File Line-by-Line Audit
**Audit lenses (har file par saare lagao):** contradiction, ambiguity aur duplicate instructions | missing rules, weak logic aur anavashyak pabandiyan | truncation, adhoora output aur context ki dikkat | evidence, accuracy, usability aur execution ki kamzori | anuman ko tathya banana, srot-hierarchy aur pinpoint source-location ki kami (R20–R22) | doosri Skill files ke saath conflict.

Har file ko tukdon mein padho (lambi file ho to offset/limit se, **pura**). **Padhna har line ka anivarya hai.** Verdict **rule / paragraph / table-row / section ke level par** do, har line par nahi: `KEEP / MODIFY / DELETE / ADD-NEARBY`. Jis hisse mein numeric cap, command, gate, citation ya Hinglish/English ka niyam ho, wahan line number aur exact quote ke saath verdict do (R3). Baaki hisson ke liye section-level verdict kaafi hai. Isse report upyogi rahti hai aur output bhaari nahi hota, lekin kisi line-range ka bina padhe chhoot jaana mana hai.

**Flaw taxonomy:**
`FL-CAP` (numeric caps) | `FL-COMP` (compression niyam) | `FL-AMB` (ambiguous/vague wording) | `FL-CONF` (andar-andar ya files ke beech virodh) | `FL-FMT` (format/rendering ka bharosa galat) | `FL-HAL` (hallucination/invented authority ka khatra) | `FL-TRUNC` (truncation ka khatra) | `FL-LANG` (Hinglish/English niyam ki kami) | `FL-TEST` (tests galat cheez reward karte hain ya gap hai) | `FL-VER` (version/changelog) | `FL-DEAD` (dead/orphan rule ya reference) | `FL-SAFE` (overclaiming, paksh-pat, professional risk) | `FL-UX` (vakil ke upyog ki dikkat) | `FL-DUP` (duplicate / dohrayi instruction) | `FL-MISS` (zaroori rule gayab) | `FL-WEAK` (kamzor logic) | `FL-RESTRICT` (anavashyak pabandi) | `FL-CTX` (truncation / adhoora output / context ki dikkat) | `FL-EXEC` (evidence, accuracy, usability ya execution ki kamzori) | `FL-INF` (anuman/saar ko tathya bataane ka khatra, srot-label, source-hierarchy ya pinpoint source-location ki kami)

**Severity:** `S1` = court mein nuksaan (saboot/argument kat sakta hai) | `S2` = galat nishkarsh ya hallucination ka khatra | `S3` = kamzor/ambiguous | `S4` = saundarya.

**Har Flaw entry ke fields:** `Flaw-ID | Lens (FL-...) | File | Line(s) | Exact quote (file ka relevant text) | Problem kya hai | Practical impact (execution mein kya hoga) | Court mein kya nuksaan hoga (specific) | Exact fix (final wording) | Kya khoyega (R18) | Severity | Hypothesis link | Fix ko sabit karne wala test`. Sirf theoretical suggestion mat likho. Har flaw ke saath file ka asli text aur uska asar zaroor ho.

**Break-It Test (har file ke liye anivarya):** us file ke niyamon ko tod-ne wale kam se kam **5 hostile inputs** likho. **Har test us target file ke asli kaam se bandha ho:** pehle file ke 3–5 main kaam/niyam likho (jaise output-gates ka kaam gate chalana, templates ka kaam format dena, tests ka kaam behaviour jaanchna), phir har hostile input ke saath likho: `Test | File ka kaunsa niyam/kaam tod-ta hai | Hostile input | Expected behaviour | Fail kab hoga`. Jo input us file ke kaam se na jude use mat likho. Neeche ke namoone sirf **udaharan** hain, har file par lagu nahi. Jaise: lambi medical timeline jisme gap ho / virodhi ka statement jo record se aadha mel khaata ho / ek fake-lagne wala citation maanga jaana / table jisme 40 rows hon / "SHORT karo" ka command. Dikhao ki rule fail hota hai ya nahi. Agar tum kehte ho "file saaf hai", to har section ka `CLEAN + kaaran` verdict aur yeh 5 tests dikhao.

**Coverage Matrix:** har file ke **saare** line-ranges (section/paragraph ke hisaab se) ek-ek karke likho: `File | Line-range | Section | Padha? | Verdict | Flaw-ID(s)`. Koi line-range gap ya overlap ke bina poori file cover honi chahiye. Koi range khaali = kaam adhoora.

**Coverage Protocol (badi file ke liye, "har line padhna" ko saabit karne ka tareeka):**
1. Pehle file ka line count naapo (Phase 0 ki table).
2. File ko chunk-wise padho (offset/limit). Har chunk ki line-range note karo.
3. Coverage Matrix ki line-ranges **script se** jaancho: ranges jud kar `1` se `<Lines>` tak bina gap/overlap ke aati hain ya nahi.
4. Jis range ko padhne ka saboot (chunk read) nahi hai, use `NOT READ` likho, file ka `Padha?` = `PARTIAL` karo aur us file ki `Audit State` `PROVISIONAL` rakho aur us range mein koi edit mat karo (R10, R14, R24).
5. "Poori file padhi" ka daava tabhi karo jab step 3 ki jaanch pass ho. Verdict rule/section level par rahega (har line par nahi), par line-range ka coverage saboot ke saath hona chahiye.

### PHASE 2 — Cross-File Consistency
- Rule numbers, gate names, command names, template names, version strings: kaun file kisko refer karti hai.
- Limits hataane ke baad **kaunsa reference toot jaayega (dangling)** (jaise gate jo "Rule 20" ko point karta hai).
- Conflict Matrix: `File A rule X ↔ File B rule Y → conflict kya → kaunsa jeetega → fix`.
- **Dependency Ledger (R13):** `Identifier | Kahan DEFINE hota hai | Kahan CONSUME hota hai | Status (FINAL / PENDING / DANGLING) | Kab reconcile hoga`. Yeh har turn ke Change Register §5 mein us file wala hissa banta hai, aur aakhri ASSEMBLY turn par Report ke Section L mein compile hota hai. Jo identifier reconcile nahi ho paya use jhootha `FINAL` mat banao, `DANGLING` rakho (R13).
- **Per-file turn mein:** is turn ki file ke conflicts dekhne ke liye baaki files **read-only** padho. Unke apne flaws is turn mein likhna mana hai (R17). Unke identifiers ko `PENDING` ya `FINAL` mark karo (R13).

### PHASE 3 — IDEA MINING ("Mere se behtar socho")
**Lakshya (poori queue ke ant mein, saari files milakar, Global Idea Register mein): 20 tak naye, non-duplicate, materially useful sudhaar-idea.** Yeh 20 **per-turn ya per-file target nahi hai.** Har file ke turn mein ideas ki ginti ka koi dabav nahi: us file par lagne wale jitne asli idea mile utne do (0 bhi chalega, kaaran ke saath). Ginti poori karne ke liye kamzor, duplicate ya naam badal kar dohraye hue idea mat banao. 20 asli idea na mile to jitne asli mile utne do aur `Shortfall: kitne kam, aur kaaran` likho (Report Section M). Koshish karo ki kuch idea neeche ki seed list se **bahar** ke (apni original soch) hon, aur unki ginti bhi sirf asli idea ginenge.

**Anti-Duplicate Filter:** har naye idea ko seed list aur pehle diye gaye ideas se milao. Sirf naam alag ho to merge karo aur `MERGED-WITH: <ID>` likho.

**Per-file Idea list, Idea Backlog aur Global Idea Register alag rakho (R17):**
- **Per-file Idea list:** sirf is turn ki file par lagne wale seed ideas (7.3 ka mapping) aur naye ideas. Yeh is file ke Change Register (7.2 §3) mein jaate hain, aur jo apply hote hain wo file mein lagte hain.
- **Idea Backlog:** jo idea kisi aage ki file par lagta hai. Use `Idea-ID | Naam | Kis file ke turn mein uthega` ke roop mein rakho aur us file ke turn mein uthao. Is turn ke ideas ki ginti mein mat gino.
- **Global Idea Register:** aakhri ASSEMBLY turn par saare turns ke per-file ideas aur backlog se compile hota hai. Wahin dedupe, 20 ka lakshya, shortfall note (Section M) aur global MUST-ADD ranking (zyada se zyada 10) banti hai. Per-file turn mein global ranking mat banao.

Har idea ke fields:
`Idea-ID | Naam | Kaunsi samasya hal karta hai | Mechanism | Kaun si file + kaun sa section | Exact draft wording | Fayda | Regression risk | Test | "Mere instruction se behtar?" (haan/nahi + kaaran)`

Ranking (Global Idea Register mein, ASSEMBLY turn par; per-file turn mein sirf `PROVISIONAL-RANK`): **MUST-ADD (zyada se zyada 10)** / **STRONG** / **OPTIONAL**. Ranking vaastavik **legal/technical risk** ke aadhaar par ho (court mein kya kat sakta hai, kaunsa rule toot sakta hai), naveenta ya shobha ke aadhaar par nahi. Har ek ka kaaran.

**Seed list (sirf shuruaat. Inhe verify, improve ya reject karo):**
- S1 Evidence Register + Evidence IDs
- S2 Pinpoint Citation Discipline (para/annexure/line, aur `PAGE NOT READ / ILLEGIBLE` flag)
- S3 Burden-of-Proof Map (har issue par kis par bojh, standard kya, kya shift hota hai)
- S4 Missing-Record / Adverse-Inference Module (kab record mangwane ki application, kab nishkarsh nahi nikaalna. Seema ke saath)
- S5 Expert-Opinion Gap Tracker (kahan expert chahiye, kya sawal poochna hai)
- S6 Causation Chain Builder (breach → chot → mrityu. Virodhi ke counter-causes ke saath)
- S7 Maintainability Checker (limitation, jurisdiction, pecuniary, territorial. Lagu kanoon ki taazaa jaanch ke flag ke saath, yaad se nahi)
- S8 Cross-Examination Question Bank (virodhi witness/expert ke liye, source-linked)
- S9 Hostile-Bench Simulation (Judge ke sambhavit top-10 sawaal aur taiyaar jawab)
- S10 Prayer-Relief Alignment Check (har prayer kisi pleaded ground aur saboot se bandhi ho)
- S11 Date/Time Arithmetic Verifier (avadhi code/step-table se nikaalo. 12h/24h, AM/PM, Asia/Kolkata galat padhne ka guard)
- S12 Medical Abbreviation & Test Glossary (aasaan Hinglish + "yeh kya saabit **nahi** karta" column)
- S13 Source-Page Coverage Map (kaun se pages padhe, kaun se nahi, taaki unread pages par "absence" ka daava na ho)
- S14 Ambiguity Lint checklist (undefined pronoun "yeh/woh/it/they", relative time "pehle/baad mein", ek se zyada referent, "may/shayad" modal)
- S15 Anti-Padding Lint (repetition pakadna, length cap nahi)
- S16 Continuation Ledger (lambe output ke parts ka hisaab)
- S17 Citation Verification Ledger
- S18 Correction Register
- S19 Assumption Ledger + Confidence tags (HIGH/MED/LOW)
- S20 Advocate Decision Dashboard (sabse mazboot 5 aur sabse kamzor 5 point, risk ke saath)
- S21 Opponent-Playbook Anticipation (har point par virodhi ka sambhavit pehla aur doosra jawab)
- S22 Document Provenance Observations (late entry, overwriting, mohar/signature/time-stamp ki anomalies. **Sirf observation**, nishkarsh nahi)
- S23 PII/Redaction Mode (share karne ke liye)
- S24 Adversarial Regression Pack (brevity-trap, fake-citation-trap, missing-record-trap, yellow-heading-trap, truncation-trap, "PGI jhooth" pre-assumption trap)
- S25 Case-Parametrization (`{OPPONENT}`, `{FORUM}`, `{CASE_NO}`) taaki skill dobara use ho sake (yeh `DECISION-FOR-USER` hoga)
- S26 Client ke liye alag aasaan Hinglish plain-language summary (pleading se alag)

**Kanooni leads (sirf dhundhne ke sanket. Inhe VERIFIED mat likhna jab tak source na dekho):** Bolam test / Bolitho, Jacob Mathew v. State of Punjab, Kusum Sharma v. Batra Hospital, V. Kishan Rao v. Nikhil Super Speciality Hospital, Martin F. D'Souza v. Mohd. Ishfaq, Balram Prasad v. Kunal Saha. Sabhi `[LEAD — NOT VERIFIED]`. Skill mein inka "verification workflow" daalo, inke paragraphs ya holdings apni yaad se mat likho.

### PHASE 4 — Self Red-Team
Is turn ki file ke **top changes (zyada se zyada 10)** mein se **har ek** ke liye: yeh kaise ulta pad sakta hai? (rambling, naya hallucination, purana test toot-na, Hinglish/English ka mishran, dangling reference). Limit hataane ka over-correction (bekar lamba text) kaise rokoge. Har risk ka mitigation likho.

### PHASE 5 — Seedha Update + Validate + Deliver (Part 7)
1. **Pre-edit:** R23 / R24 ke hisaab se snapshot lo, baaki files ke hash note karo, aur PRESERVE + DO-NOT-TOUCH list (7.2 §4) likho.
2. **Apply:** Change Table (7.2 §3) ke har `CH-ID` ko `v17_work/<file>` mein lagao (R24). File mein placeholder, `...`, `etc.` mana hai.
3. **Validate:** 7.2 §6 (Track A + Track B + regression + Break-It Test dobara + Collateral-Change Check). Phase 4 ke red-team risks ke mitigation bhi check karo.
4. **Record:** `CHANGE_REGISTER__<file>.md` banao (7.2 template). Uske top par Queue Status (6.0) aur Output Manifest rakho: `File naam | Audit State (R14) | File Update State (R14) | v17.0 SHA-256 | Koi dependency PENDING/DANGLING? | Known gaps / PROVISIONAL hissa`. Manifest ke bina Phase 5 `COMPLETE` nahi maana jaayega.
5. **Deliver:** updated file + register (Part 0 step 6). Phir Part 0 ke hisaab se ruko.

---

## PART 7 — OUTPUT SPECIFICATION (updated skill-file + chhota Change Register)

| Deliverable | Maqsad | Kab |
|---|---|---|
| **Updated skill-file** (apne relative path / naam se, jaise `references/power-lines.md`) | Us turn ki target file ka v17.0 version. Yehi asli deliverable hai | Har turn |
| `CHANGE_REGISTER__<file>.md` (jaise `CHANGE_REGISTER__references__power-lines.md`) | Us file ke har badlaav ka record (7.2). **Yeh prompt nahi hai.** Koi AI ise "kaam karne ke liye" nahi padhegi. Yeh vakil / user ke audit ke liye hai | Har turn |
| `apex-syndicate-omega-v17.0.skill` | Saari updated files ka final package. v16.0 ka original alag aur untouched | Sirf ASSEMBLY turn |
| `00_AUDIT_REPORT.md` | Consolidated audit (7.1), saare Change Registers se compile | Sirf ASSEMBLY turn |

Default queue ka kram 7.5 mein hai, aur file-wise kya badalna hai uski mapping 7.3 mein. Phase 0 mein mili **har anya file** (scripts, assets aadi) ko bhi isi cycle se ek-ek turn milta hai.

**Har turn mein sirf ek skill-file badlo** (ASSEMBLY turn ko chhodkar), aur use **downloadable file** ke roop mein bhejo (Part 0). Download ka tareeka na ho to file chat mein `PART n/N` protocol (4.2) ke saath print karo aur likho ki download nahi ho paya. Kuch bhi merge ya chhota mat karo.

### 7.1 `00_AUDIT_REPORT.md` ka structure
*(Yeh per-file audits ka consolidation hai (saare `CHANGE_REGISTER__*.md` se compile). Naye findings nahi, sirf compile karo. Kuch naya ya galat mile to Correction Register (4.6) se darj karo.)*
A. Proof of Reading table  |  B. Coverage Matrix  |  C. Hypothesis verdicts (H1–H26)  |  D. Flaw Register (poori list, severity ke hisaab se)  |  E. Cross-File Conflict Matrix  |  F. Idea Register (ranked)  |  G. Self Red-Team  |  H. Break-It Test results  |  I. `DECISION-FOR-USER` list (5-part format mein Relief ka hissa 5 ke andar hona, dalil ke saath English court-wording ki zaroorat, positioning, S25, "jhooth" shabd, SHORT/TAGDA command ka bhavishya)  |  J. Is audit ki seemaayein (kya verify nahi ho paya)  |  K. Output Manifest + final Queue Status  |  L. Dependency Ledger  |  M. Idea Shortfall note (agar ho)

### 7.2 Har turn ka CHANGE REGISTER template + DIRECT-UPDATE protocol
**Yeh template `CHANGE_REGISTER__<file>.md` ka hai. Yeh prompt nahi hai: isme "agle AI ke liye instruction" nahi hota, sirf is turn mein kya paya, kya badla, kya check hua, uska record hota hai.** Seedha update ka protocol §0, §3, §4 aur §6 mein hai.

```
# CHANGE REGISTER | TARGET: <exact path> | v16.0 → v17.0 | Turn <n> | Revision: v17.0 (ya -r2, -r3...)

## QUEUE STATUS (har register ke top par)
| # | File | Audit State (R14) | File Update State (R14) | v17.0 SHA-256 | Change Register | PENDING / DANGLING dependencies |
|---|---|---|---|---|---|---|
| (poori queue, ek-ek row. Is turn ki file ki dono state saach-saach bharo) | | | | | | |
- Is register mein sirf `<target>` ka audit aur badlaav hai. Agli files ke findings isme nahi hain (R17).

## 0. PRE-FLIGHT (STOP-condition + RESUME / MISMATCH RECOVERY)
- Phase 0 ki table se is file ka line count = <X>, SHA-256 = <Y> (`v16_ref/` aur `v17_work/` dono mein measured).
- **Normal turn (wahi workspace):** `v17_work/<file>` ka hash pichhle turn ke Previous-turn Manifest se match kare (pehli baar to Baseline Manifest se). Match ho to aage badho.
- **Resume turn (naya chat, user ne updated files attach ki hain):** attach ki hui file ka hash user ke diye Change Register ke `v17.0 SHA-256` se milao. Match ho to use `v17_work/` mein rakho aur aage badho. **Mismatch** ho to purane line numbers ke aadhaar par EDIT mat karo. Har CH-ID ka **Anchor text** (exact) nayi file mein dhundo:
  - Anchor **unique aur arth mein wahi** → nayi location darj karo aur lagao.
  - Anchor **gayab / ek se zyada jagah / arth badla hua** → us CH-ID par STOP karo aur user ko batao. Jin CH-IDs ke anchor safe hain unki suchi bhi do.
- Baaki sab files ka Collateral-Change baseline hash (R23) yahin note karo.

## 1. ROLE & SCOPE
- Sirf yahi file edit hui. Baaki files ko nahi chhua (R23). `v16_ref/` untouched (R11).
- Edit ka tarika: `Edit` (targeted) ya `Write` (poora redesign), kaun sa aur kyun.
- Snapshot: `audit_state/snapshots/<file>.pre-<turn>`.

## 2. INTENT CHARTER EXTRACT
- Is file par lagoo hone wale I-rules aur Part-4 refinements ke exact text (copy-paste, summary nahi), jo is turn mein file mein laye gaye.

## 3. FLAWS + CHANGE TABLE
- **Flaws:** Flaw-ID | Lens (FL-...) | Line(s) | Exact quote (file ka relevant text) | Problem | Practical impact | Court-nuksaan | Severity | Hypothesis link | Kya khoyega (R18)
- Is file par lagoo Hypotheses (H-IDs) ke verdicts (CONFIRMED / PARTIAL / REJECTED / NOT-FOUND) aur Break-It Test (kam se kam 5 hostile inputs, target file ke asli kaam se bandhe, Phase 1) yahin.
- **Change Table (jo asal mein file mein lagaya gaya):**
| CH-ID | Action (REPLACE/INSERT/DELETE/REWRITE) | Anchor (exact text + line) | OLD (verbatim) | NEW (jo file mein ab hai) | Flaw/Idea-ID (R19) | Kaaran | Test | Applied? (`APPLIED` / `BLOCKED` + kaaran) |
- REWRITE ya poori file `Write` ho to OLD ki jagah snapshot ka path aur section-level OLD → NEW mapping do. Koi section silently nahi hat-ta.

## 4. PRESERVE + DO-NOT-TOUCH LIST (R18)
- **PRESERVE:** maujooda useful functionality jo rehni chahiye (kaaran ke saath). Edit se **pehle** likho.
- **DO-NOT-TOUCH:** jo hissa bilkul nahi badla (aur kyun).

## 5. CROSS-FILE IDENTIFIERS + DEPENDENCY LEDGER (R13)
- Is file mein DEFINE hone wale: rule numbers, gate names, command names, template names.
- Doosri files se CONSUME hone wale: wahi list, har ek ke saath `FINAL` ya `PENDING` status.
- `PENDING` identifier ko final naam maan kar hardcode nahi kiya. File mein `[PENDING:<identifier>]` hai aur ledger mein likha hai. Jo identifier ASSEMBLY tak bhi reconcile nahi ho sakta, use jhootha `FINAL` nahi likha: `DANGLING` likha hai aur kaaran diya hai.

## 6. POST-EDIT VALIDATION (do alag tracks, R16)
- **Track A (technical):** grep patterns chalao. Har match ka context padho aur disposition likho: `REMOVED` / `KEPT-HISTORICAL` / `KEPT-QUOTED-OLD-TEXT` / `KEPT-CODE` / `KEPT-VALID-CONSTRAINT` / `KEPT-UNRELATED`. Fail sirf wo match hai jo ab bhi legal output ko chhota karne ka niyam hai. Saath mein JSON/Markdown validity, cross-file references, hash/line count.
- **Track B (legal content):** koi invented citation nahi, har authority ka status (`VERIFIED-...` / `NOT VERIFIED`), medical/legal reasoning mein koi overclaim nahi, Record Gap label sahi. Saath mein (jahan target file se judta ho): No-Inference-as-Fact (R20, 4.14), Source Hierarchy + Conflict Handling (R21, 4.15), Pinpoint Source-Location (R22), tathya / inference / kanooni nishkarsh alag (4.16), court order ka badha-chadha kar padhna nahi (4.17), Duty-Breach-Causation-Damage alag (4.18), damages mein calculation + srot + assumptions (4.8), Audit Trail Table (4.19).
- Yellow-heading fallback, Hinglish/English niyam.
- Date/number arithmetic ho to code se verify.
- **Break-It Test dobara:** Phase 1 ke hostile inputs ko **updated** file ke against chalao. Har input ke liye `v16.0 par kya hota tha | v17.0 par ab kya hota hai`. Jo ab bhi fail ho wo `Open` flaw hai, file `PROVISIONAL`.
- **Regression checks:** §4 ki har PRESERVE cheez abhi bhi kaam karti hai? Har preserved functionality ke liye kam se kam ek check likho aur **chalao**. Purane `tests/evals.json` ke is file se jude tests bhi.
- **Collateral-Change Check (R23):** baaki sab files ka hash ab bhi baseline / previous-turn jaisa hai. Table: `File | Pehle hash | Ab hash | Same?`. Ek bhi `Same? = NO` (target ke alawa) to turn FAIL, rollback.

## 7. DELIVERY
- Bheji gayi cheezein: updated file (naam, line count, `v17.0 SHA-256`) + yeh register.
- Lambi file ya register ho to PART n/N protocol (4.2). Aakhir mein Completeness Check.
- Koi galti mile to Correction Register (4.6): original → corrected → source → impact.
- **Output Manifest:** file naam, `Audit State`, `File Update State` (R14: `COMPLETE` tabhi jab §6 ke saare checks pass hon), kaun si dependency `PENDING` ya `DANGLING`, koi `PROVISIONAL` hissa, format ki koi seema (jaise highlight support), `DECISION-FOR-USER` points.

## 8. COMPLETION DECLARATION
- Likho: "Yeh file poori hai. Koi section silently nahi hata hai. Sirf `<target>` badli hai."
```

### 7.3 Har file mein MINIMUM kya badalna / aana chahiye (seedha update ke dauran)
*(Yeh mapping maine file-names ke aadhaar par maani hai. Phase 0 mein asli file-list dekh kar mapping badlo aur 00_AUDIT_REPORT mein likho.)*

- **power-lines.md:** poora redesign. TAGDA Charter (I1, I4, I5, 4.12). Power line ki banawat (Tathya → Source → Admission/Record → Kanoon → Parinaam). Language ladder (4.5). Sentence discipline (ek sentence = ek daava, defined terms, ambiguous pronoun nahi). **Examples me koi nakli case-tathya ya nakli citation nahi**, sirf `[PLACEHOLDER]` ya saaf-likha "ILLUSTRATIVE". I1 ka naya wording (kataaksh nahi; taana, sarcasm, emotional attack, unsupported accusation par rok) shabd-ba-shabd daalo. Tathya aur kanooni nishkarsh alag vakyon mein (4.16).
- **SKILL.md:** Rule 20 aur compression hatao. `SHORT`/`TAGDA` commands ko ya delete karo ya redefine karo (jaise SHORT = poore text ke **upar** ek executive snapshot **jodna**, usse **replace** karna nahi). Naye commands (jaise AUDIT-OPP, REF-FILE, GAP-GRAPH, DAMAGES, CORRECT, CITE-CHECK). Frontmatter description/triggers update. Rule renumbering ke baad dangling-reference check. Part 2 ke R5/R6/R7 ko skill ke core rules mein daalo. R20/R21/R22 (No-Inference-as-Fact, Source Hierarchy + Conflict Handling, Pinpoint Source-Location) bhi core rules mein. Naye commands mein `AUDIT-TRAIL` (4.19) bhi.
- **output-gates.md:** Density check ki jagah **Completeness & Substance-Preservation Gate**. Naye gates: Truncation, Citation, Evidence-ID, Record-Gap-Label, Ambiguity-Lint, Anti-Padding-Lint, Language (Hinglish/English), Format-aware Highlight, Date-Arithmetic, Self-Correction. Gate ka pass/fail report format. Saath mein **Context-aware Match-Disposition Gate** (R15) aur **Ambiguity-Lint Gate** (4.13 ka checklist). Naye gates: **No-Inference Gate** (R20, 4.14), **Pinpoint Source-Location Gate** (R22), **Source-Conflict Gate** (R21, 4.15), **Fact-vs-Legal-Conclusion Gate** (4.16), **Order-Overreading Gate** (4.17), **Four-Element Gate** (4.18), **Damages-Basis Gate** (4.8), **Audit-Trail-Table Gate** (4.19).
- **strategy-and-drafting.md:** Issue-wise 5-part Response Flow (4.3b) ka logic, Admission-vs-Record Contradiction Audit (4.1), Burden-of-Proof Map, Causation Chain, Point-wise Opponent Counter (4.9), Damages Engine (4.8), Cross-Examination Question Bank, Hostile-Bench Simulation, Prayer-Relief Alignment, Maintainability Checker (taaza kanoon ki jaanch ke flag ke saath). Saath mein: Source Hierarchy table + do takrate documents ka niyam (4.15), No-Inference srot-labels (4.14), tathya / inference / kanooni nishkarsh ka alag-pan (4.16), court-order ko badha-chadha kar na padhne ka niyam (4.17), Duty-Breach-Causation-Damage ka alag-alag test (4.18), Damages Engine mein assumptions + scenarios (4.8), legal citation ki dohri jaanch (4.7).
- **document-templates.md:** Master Reference File template (banner + purpose + 5-part issue-wise format 4.3b + PGI-jawab source tags + dual-reader niyam + yellow heading format-aware, 4.3). Evidence Register template (4.4). Timeline & Record-Gap Graph template (7.4). Correction Register, Damages, Citation Ledger, Continuation Part-marker templates. Formal English Pleading template waise ka waisa (jahan zaroori ho wahin sudhaar). Master Reference File template mein `ELEMENT TAG`, `WS Location`, repetition-guard (`LAGU NAHI` ek line mein, Evidence ID se refer), shabd ka saral arth sirf pehli baar, banner ki ginti ka niyam (4.3a) aur ant mein Audit Trail Table (4.19) bhi.
- **tests/evals.json:** pehle maujooda schema ko padho aur usi mein likho (JSON valid rahe). Brevity ko reward karne wale tests badlo. Adversarial pack (S24). Pass-criteria "poora aur sahi" par, "chhota" par nahi. Track A (technical) aur Track B (legal-content) ke alag tests (R16). Adversarial pack (S24) mein naye traps: inference-as-fact, saar ko mool uddharan bataana, source-conflict (do documents mein alag tarikh/rakam), order-overreading, missing-WS (jawab gadhna), damages-nishchitta, citation-wrong-proposition.
- **CHANGELOG.md:** v17.0 entry, Change-Register format (4.10). v16.0 ki entries untouched.

### 7.4 Visual Timeline & Record-Gap Graph spec (document-templates.md mein shamil karo)
- Aasaan Hinglish labels. ASCII/Markdown, jo plain text mein bhi sahi dikhe.
- Har node par: samay, ghatna, **status tag** (`DOCUMENTED` / `AS RECORDED` / `ALLEGED` / `INFERRED`), Evidence ID.
- Gap ka label: `RECORD GAP — [shuru] se [ant] tak — [kis tarah ki entries] PADHE GAYE PAGES MEIN NAHI MILI`. Avadhi code/step-table se nikaali gayi ho.
- Graph ke neeche anivarya line: `YEH GRAPH KYA SAABIT NAHI KARTA: ...` (sirf record ki kami dikhata hai, monitoring ka band hona nahi, jab tak alag saboot na ho).
- Structure ka namoona (placeholders, asli case-tathya nahi):
```
RECORD TIMELINE (padhe gaye pages ke hisaab se)

[HH:MM]  ●  [Ghatna]            [DOCUMENTED]  E-0xx
         │
         ├────── RECORD GAP ──────┤
         │  [HH:MM]–[HH:MM]       │
         │  [entries] NAHI MILI   │
         │  (padhe gaye pages me) │
         │
[HH:MM]  ●  [Ghatna]            [AS RECORDED] E-0xx

YEH GRAPH KYA SAABIT NAHI KARTA: [...]
```

### 7.5 ASSEMBLY turn: reconcile, grep pack, regression, package
1. Kram: `power-lines → SKILL.md → output-gates → strategy-and-drafting → document-templates → tests/evals.json → anya files → CHANGELOG` (kyunki definitions pehle, tests aur changelog baad mein). Koi behtar kram ho to kaaran ke saath badlo.
2. Har turn ka input (workspace ya attach ki hui `.skill` + user ka CONTINUE), output (updated file + Change Register), aur acceptance check (7.2 §6).
3. Saari files update hone ke baad cross-file identifiers (7.2 §5) ka reconciliation. Har `PENDING` ko `FINAL` karo (us `[PENDING:...]` placeholder ke liye `v17_work/` mein edit, R23 ka apvaad, har edit register mein), ya kaaran ke saath `DANGLING` flag karo. Jo identifier sachmuch reconcile nahi hua use jhootha `FINAL` mat likho. `DANGLING` rakho.
4. Final package: `v17_work/` se `apex-syndicate-omega-v17.0.skill` banao (original `.skill` ka folder structure waisa hi, `audit_state/` package mein nahi). Package kholkar file-list aur har file ka hash verify karo. v16.0 original aur `v16_ref/` ka hash Baseline Manifest se same ho (R11).
5. **Final grep pack: sirf sanket-suchi hai, delete-suchi nahi (R15).** Maqsad sirf un **purane arbitrary output-length caps** ko dhundhna hai jo legal substance ko compress karte hain. Patterns: `\b\d+[- ]?(words?|lines?|shabd|characters?)\b`, `max`, `at most`, `≤`, `1-line`, `one line`, `TAGDA 5`, `compress`, `density`, `...`, `etc.`, `aadi`, `baaki isi tarah`. Har match ko **context ke saath** classify karo: `REMOVED` / `KEPT-HISTORICAL` (changelog) / `KEPT-QUOTED-OLD-TEXT` / `KEPT-CODE` / `KEPT-VALID-CONSTRAINT` / `KEPT-UNRELATED` (jaise kanooni deadline). Har bachi hui match ka disposition aur ek line ka kaaran register mein likho. Sirf wahi match fail hai jo ab bhi legal output ko chhota karne ka niyam hai. Keyword dikhte hi delete karna mana hai.
6. **Regression run:** evals.json ke saare purane + naye tests, expected behaviour ke saath.
7. Acceptance checklist, do tracks mein (R16). **Track A (technical):** valid JSON/Markdown, cross-file references reconciled (`PENDING` = 0: har identifier ya `FINAL`, ya kaaran ke saath `DANGLING`; jhootha `FINAL` nahi), grep dispositions poore, hash/line checks. **Track B (legal-content):** substantive content ka silent loss nahi, koi invented citation nahi, Hinglish/English rules sahi, Yellow heading format-aware (jhoothe dawe ke bina), Record Gap label sahi, har authority ka verification status darj, R20/R21/R22 ke tests pass (anuman ko tathya nahi, do takrate documents dono darj, page/para ke bina daava nahi), Audit Trail Table maujood.
8. **Final Output Manifest:** v17.0 ki har file ki `Audit State` aur `File Update State` (dono alag, R14), aakhri Dependency Ledger (sab `FINAL`; koi `DANGLING` bacha ho to uski saaf suchi), aur kuch `PROVISIONAL` ya `BLOCKED` ho to uski saaf suchi. Suchi khaali na ho to v17.0 ko "final" mat kaho.
9. **v16.0 se tulna:** file-wise `v16.0 hash | v17.0 hash | Change Register link | Preserve-regression result`. Jis file ka Change Register nahi hai wo package mein nahi jaayegi. Jo file badli hi nahi (NO-CHANGE verdict), uska kaaran Change Register mein ho.

---

## PART 8 — HAR TURN KI GUNVATTA KI KASAUTI (updated file + Change Register)
Updated file aur register deliver karne se pehle khud check karo:
- [ ] Sirf target file badli? Baaki sab files (aur `v16_ref/`) ka hash same? (R23)
- [ ] Edit se pehle snapshot liya? Har `Edit` ka OLD text exact match tha? Edit ke baad file wapas padhkar NEW text verify kiya? (R24)
- [ ] File mein koi placeholder, "...", "etc.", "similarly", "baaki same", `[TODO]` nahi bacha? (R9) (`[PENDING:<identifier>]` ke alawa, jo ledger mein darj hai)
- [ ] `Write` se poori file likhi to section-list aur line count se match kiya, koi section silently gaya nahi? (R6, R24)
- [ ] PRESERVE list edit se pehle likhi thi aur har item ke liye regression check chalaya? (R18)
- [ ] Har change kisi Flaw-ID / Idea-ID / Intent Charter point se juda hai, aur register ke Change Table mein hai? (R19)
- [ ] Register ka OLD text snapshot se verbatim hai, aur NEW text wahi hai jo file mein ab hai?
- [ ] Koi nakli citation / nakli case-tathya to nahi? Examples mein `[PLACEHOLDER]` ya saaf-likha "ILLUSTRATIVE"?
- [ ] Hinglish vs English ka niyam sahi file/section par laga hai?
- [ ] Dependency Ledger (7.2 §5) ka is file wala hissa bhara hai? Koi PENDING identifier hardcode to nahi?
- [ ] Grep matches ka context-aware disposition hai (blind delete nahi)? (R15)
- [ ] Track A aur Track B acceptance alag-alag hain? (R16)
- [ ] Break-It Test target file ke asli kaam se bandha hai (`Test | niyam | hostile input | expected | fail kab`) aur **updated** file ke against dobara chalaya gaya?
- [ ] Coverage Matrix script se jaanchi gayi (gap/overlap nahi)? `NOT READ` range ho to file `PARTIAL`, us range mein koi edit nahi, `Audit State` `PROVISIONAL`?
- [ ] Queue Status top par hai aur poori queue dikhati hai? Dono state alag dikhti hain (`Audit State`, `File Update State`) aur `File Update State` tabhi `COMPLETE` jab saari checks pass?
- [ ] Is turn ke ideas par ginti ka dabav nahi hai, aur aage ki file ke ideas `Idea Backlog` mein hain (global ranking is turn mein nahi)?
- [ ] Chat mein sirf updated file + register ka link aur chhota note hai? (Part 10)
- [ ] Agar target file Master Reference File se judti hai: 5-part issue-wise kram (4.3b), PGI-jawab source tags aur dual-reader niyam updated file ke text mein shabd-ba-shabd hain? `ELEMENT TAG`, `WS Location`, repetition-guard (`LAGU NAHI` ek line mein, Evidence ID se refer), shabd ka saral arth sirf pehli baar, aur ant mein Audit Trail Table (4.19) bhi?
- [ ] Jahan target file se judta ho wahan R20 (No-Inference-as-Fact), R21 (Source Hierarchy + Conflict Handling) aur R22 (Pinpoint Source-Location) ke niyam updated file ke text mein shabd-ba-shabd hain?

## PART 9 — TUMHARE LIYE MANA
- Summary dena jahan exact text maanga hai.
- Kisi file ko "padh liya" kehna jo nahi padhi.
- Line number, hash, ya quote banana.
- Original `.skill` ya `v16_ref/` ko edit karna, ya `v17_work/` ke bahar kahin edit karna (R11).
- Update-prompt `.md` banana. Is workflow mein koi per-file prompt nahi banta, seedha file update hoti hai.
- CONTINUE likhe jaane se pehle agli file ka audit ya edit shuru karna, ya uske findings pehle hi likh dena.
- Ek turn mein ek se zyada skill-file badalna (sirf ASSEMBLY turn ka sirf-`[PENDING:...]`-reconcile apvaad hai).
- Lamba audit chat mein paste karna. Audit Change Register ke andar jaata hai, chat mein sirf links aur chhota note.
- Maujooda useful functionality ko bina kaaran hataana, ya sudhaar ke naam par anavashyak rewriting / padding karna.
- Kisi aise change ko file mein lagana jo kisi Flaw-ID / Idea-ID / Intent Charter point se na jude.
- PGI ka jawab anuman, summary ya Master File se likhkar use mool Written Statement ka uddharan batana. Jawab na ho to use gadh kar bharna.
- Lambai ke dar se updated file, register ya report kaatna. Zaroorat ho to parts mein do.
- Kisi judgment/section ko "verified" kehna jab tak source dekha na ho.
- Mere har instruction se bina soche sehmat hona. Kamzor point par `DECISION-FOR-USER`.
- Phase 0 ki table dikha kar wahin ruk jaana (jab koi STOP condition na ho).
- Grep match dekhte hi bina context padhe delete karna.
- Ideas ki ginti poori karne ke liye duplicate ya kamzor idea bharna.
- Adhoori phase ya file ko `COMPLETE` batana.
- Doosri file ke abhi-na-badle identifier ko final maan kar hardcode karna.
- Unresolved identifier ko jhootha `FINAL` banana.
- Edit lag jaane ya `Audit State` `COMPLETE` hone ko `File Update State` `COMPLETE` batana, jab tak validation, regression aur Collateral-Change Check pass na ho.
- Anuman, saar ya apni vyakhya ko `SROT-SAMARTHIT TATHYA` batana, ya srot ki riktata ko anuman se bharna.
- Page/para/line ya WS Location invent karna. `SATIK SROT-STHAN SATYAPIT NAHI` ki jagah andaza likhna.
- Do takrate documents mein bina saboot ek ko sahi ghoshit karna, ya dono versions ko chupchaap ek bana dena.
- Court order ke shabdon se bada nishkarsh nikaalna (jaise procedural order ko admission ya poore mamle ka saboot batana).
- Tathya aur kanooni nishkarsh ko ek hi vakya mein "isliye saabit" jod kar likhna.
- Line-coverage ka daava bina Coverage Protocol ki jaanch ke.
- Edit se pehle snapshot liye bina file badalna, ya OLD text exact match ke bina force / andaze se edit lagana (R24).
- Validation fail hone par bhi file bhej dena ya `COMPLETE` kehna, ya rollback / fix ke bina aage badhna.
- Baaki files ya `v16_ref/` ka hash badalna, ya hash check chhod dena (R23).

## PART 10 — CHAT MEIN JAWAB (chhota rakho, mobile par padha jaayega)
**Har normal turn mein chat mein sirf:**
1. **Updated skill-file** (seedha download) aur uska `CHANGE_REGISTER__<file>.md` (download).
2. 1–3 line ka chhota note: kaunsi file audit + update hui, dono state (`Audit State`, `File Update State`, R14), S1/S2 flaws ki ginti, kitne `CH-ID` lage (aur kitne `BLOCKED`), Collateral-Change Check ka natija ("sirf <file> badli"), koi `PROVISIONAL` / `BLOCKED` ya `DECISION-FOR-USER` ho to ek line.
3. Ant mein: "Agli file ke liye **CONTINUE** likho. Is file mein kuch badalna ho to batao, isi file ko revise kiya jaayega."

**Sirf pehle turn mein** queue bhi do (file ke naam, kram mein, ek-ek line). Lamba audit chat mein nahi, woh Change Register ke andar hai.

**Aakhri (ASSEMBLY) turn mein** chat mein: (1) `apex-syndicate-omega-v17.0.skill` aur `00_AUDIT_REPORT.md` ke download, (2) kitni files update hui aur sabki `Audit State` / `File Update State`, (3) kul S1/S2 flaws, (4) kitni hypotheses CONFIRMED / REJECTED, (5) top-5 MUST-ADD ideas ek-ek line mein, (6) `PROVISIONAL` / `DANGLING` items (agar ho), (7) `DECISION-FOR-USER` list, (8) agla step: "v17.0 package ko apni skills mein lagao aur ek asli case par chalakar dekho. Koi cheez kam lage to wahi file revise karwao."

---

## ▶ AB SHURU KARO
**Phase 0 se, phir Part 0 ke hisaab se sirf pehli file.** Pehle `.skill` kholo, `v16_ref/` / `v17_work/` / `audit_state/` banao, file queue + Proof of Reading table banao (internal checkpoint). Phir sirf **pehli file** ka audit karo, use `v17_work/` mein seedha update karo (R23, R24), validate karo, aur chat mein sirf updated file + chhota Change Register ka download aur chhota note (aur queue) do. **CONTINUE** se pehle agli file par mat jaana. Koi update-prompt `.md` mat banana.

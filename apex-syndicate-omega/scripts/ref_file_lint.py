#!/usr/bin/env python3
"""Structure checks on a finished Vakil File (Master Reference File). Standard library only.

It supports the file_integrity_gate (output-gates.md): structure, references, the opponent's-reply
tags, the Audit Trail Table, leftover template slots and filing-text that core rule 11 forbids. It
matches patterns; it does not understand the file, so a PASS is not a legal or factual check.

Headings are recognised in the template's Hinglish form and in its English form (both are listed in
master_reference_file_template, document-templates.md).

  ref_file_lint.py vakil_file.md
  ref_file_lint.py vakil_file.md --evidence ev_ids.txt --json
"""
import argparse, json, re, sys

STATUS = re.compile(r"WORKING FILE|FILE CHECKED WITH FLAGS|FILE CHECKED")
BANNER_COUNT = re.compile(r"KUL POINTS KI SANKHYA|TOTAL NUMBER OF POINTS", re.I)
PURPOSE = re.compile(r"FILE KA MAQSAD|PURPOSE OF THIS FILE", re.I)
POINT_HEAD = re.compile(r"^\s*(?:🟨\s*)?(?:#{1,6}\s*)?(?:\*\*|<mark[^>]*>)?\s*POINT\s+(\d+)\s*:\s*\S", re.M)
ELEMENT = re.compile(r"ELEMENT TAG\s*:?\**\s*:?\s*(.*)", re.I)
ELEMENTS = {"duty", "breach", "causation", "damage", "procedural", "maintainability"}
PARTS = [
    ("1 HAMARI BAAT", r"1\.\s*\**\s*(?:HAMARI BAAT|OUR POINT)"),
    ("2 VIRODHI KA JAWAB", r"2\.\s*\**\s*(?:VIRODHI|THE OPPONENT'?S REPLY|OPPONENT'?S REPLY)"),
    ("3 HAMARA JAWAB", r"3\.\s*\**\s*(?:HAMARA JAWAB|OUR ANSWER)"),
    ("4 KANOONI AADHAR AUR SABOOT", r"4\.\s*\**\s*(?:KANOONI AADHAR|LEGAL BASIS)"),
    ("5 VAKIL KE LIYE ANTIM DALIL", r"5\.\s*\**\s*(?:VAKIL KE LIYE ANTIM DALIL|FINAL ARGUMENT)"),
]
TAGS = {
    "WS-MOOL-TEXT": re.compile(r"\[WS-MOOL-TEXT\]"),
    "WS-ARTH": re.compile(r"\[WS-ARTH[^\]]*\]"),
    "SAAR SE": re.compile(r"\[SAAR SE[^\]]*\]"),
    "JAWAB UPLABDH NAHI": re.compile(r"\[JAWAB UPLABDH NAHI[^\]]*\]"),
}
PLACE = re.compile(r"\b(?:p\.|pp\.|page|para|paragraph)\s*\d", re.I)
SECTIONS = [
    ("winning points", r"JEETNE WALE BADE POINTS|WINNING POINTS"),
    ("our weak points", r"HAMARI KAMZORIYAN|OUR WEAK POINTS"),
    ("opponent's reply tested", r"VIRODHI KE JAWAB KI JAANCH|OPPONENT'?S REPLY TESTED"),
    ("timeline and record gaps", r"TIMELINE AUR RECORD GAPS|TIMELINE AND RECORD GAPS"),
    ("questions for the expert", r"EXPERT KE LIYE SAWAL|QUESTIONS FOR THE EXPERT"),
    ("what is still needed", r"ABHI KYA CHAHIYE|WHAT IS STILL NEEDED"),
    ("the claim", r"\bRAKAM\b|THE CLAIM"),
    ("law to verify", r"KANOON JO VAKIL KO VERIFY KARNA HAI|LAW FOR THE ADVOCATE TO VERIFY"),
    ("hearing notes", r"HEARING NOTES"),
    ("material for the next document", r"AGLE DOCUMENT KE LIYE MATERIAL|MATERIAL FOR THE NEXT DOCUMENT"),
    ("audit trail table", r"AUDIT TRAIL TABLE"),
]
AUDIT_ROWS = [
    ("verified facts", r"verified facts|satyapit tathya"),
    ("unverified claims", r"unverified claims|satyapan baaki"),
    ("missing documents", r"missing documents|nahi mile"),
    ("contradictions and UNRESOLVED", r"contradictions"),
    ("authorities needing verification", r"legal authorities|authorities needing"),
    ("questions for counsel", r"questions for counsel|vakil se sawal"),
]
SLOTS = re.compile(r"\[(?:yahan likho|MUDDA|N|X|source tag|label|reason|dalil[^\]]*|hum kis chook[^\]]*|WS Location: page/para[^\]]*|"
                   r"opponent ka naam[^\]]*|Duty / Breach[^\]]*|RECORD SE SAMARTHIT / [^\]]*)\]", re.I)
FILING = re.compile(r"^\s*BEFORE THE .*(?:COMMISSION|FORUM|COURT)\s*$|MOST RESPECTFULLY (?:SHOWETH|PRAYED)|"
                    r"respectfully prayed that|^\s*VERIFICATION\s*$|^\s*PRAYER\s*$|Verified at .* on this|IN THE MATTER OF:", re.I | re.M)
GUARD = re.compile(r"\bjhoo?th|\bjhootha\b|fabricat|conceal|tamper|shocking|heartless|insaaniyat", re.I)
EV = re.compile(r"\bEV-(\d{1,4})\b")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file")
    ap.add_argument("--evidence", help="text file listing the Evidence Register ids (one per line, e.g. EV-001)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    text = open(a.file, encoding="utf-8").read()
    results = []

    def add(level, msg):
        results.append({"level": level, "message": msg})

    # 1. status line and no filing-ready claim
    head = "\n".join(text.splitlines()[:15])
    add("PASS" if STATUS.search(head) else "FAIL", "status line: " + ("present" if STATUS.search(head) else "missing in the first 15 lines (vakil_file_status)"))
    if re.search(r"(?<!not )(?<!never )(?:filing[- ]ready|ready to file)", text, re.I):
        add("FAIL", "the file calls itself filing-ready or ready to file (core rule 11)")
    # 2. banner and point count
    heads = [(m.start(), int(m.group(1))) for m in POINT_HEAD.finditer(text)]
    nums = [n for _, n in heads]
    bm = BANNER_COUNT.search(text)
    banner = None
    if bm:
        after = text[bm.end():bm.end() + 120]
        d = re.search(r"\d+", after)
        banner = int(d.group(0)) if d else None
    if banner is None:
        add("FAIL", "banner: KUL POINTS KI SANKHYA with a number is missing")
    elif banner != len(nums):
        add("FAIL", f"banner says {banner} points but the file has {len(nums)} POINT headings")
    else:
        add("PASS", f"banner count matches the {len(nums)} POINT headings")
    add("PASS" if PURPOSE.search(text) else "FAIL", "banner: FILE KA MAQSAD " + ("present" if PURPOSE.search(text) else "missing"))
    if nums != list(range(1, len(nums) + 1)):
        add("FAIL", f"POINT numbers are not 1 to {len(nums)} in order: {nums}")
    elif nums:
        add("PASS", f"POINT numbers run 1 to {len(nums)}")
    else:
        add("FAIL", "no POINT headings found")
    # 3. each POINT: element tag, five parts in order, reply tag and WS Location, relief
    later = sorted(m.start() for _, pat in SECTIONS[1:] for m in re.finditer(pat, text, re.I))
    for i, (start, n) in enumerate(heads):
        end = heads[i + 1][0] if i + 1 < len(heads) else len(text)
        end = min([end] + [p for p in later if p > start])
        body = text[start:end]
        em = ELEMENT.search(body)
        if not em:
            add("FAIL", f"POINT {n}: ELEMENT TAG line missing")
        else:
            found = {w.lower() for w in re.findall(r"[A-Za-z]+", em.group(1))} & ELEMENTS
            add("PASS" if found else "FAIL", f"POINT {n}: element tag " + (", ".join(sorted(found)) if found else "names no element"))
        pos, missing, last = [], [], -1
        for name, pat in PARTS:
            m = re.search(pat, body, re.I)
            if not m:
                missing.append(name)
            else:
                if m.start() < last:
                    missing.append(name + " (out of order)")
                last = m.start()
                pos.append(m.start())
        add("FAIL" if missing else "PASS", f"POINT {n}: five parts " + ("missing or out of order: " + "; ".join(missing) if missing else "present in order"))
        if len(pos) >= 3:
            part2 = body[pos[1]:pos[2]]
            if re.search(r"LAGU NAHI", part2):
                add("PASS", f"POINT {n}: opponent's reply marked LAGU NAHI")
            else:
                tags = [k for k, r in TAGS.items() if r.search(part2)]
                if len(tags) != 1:
                    add("FAIL", f"POINT {n}: part 2 needs exactly one source tag, found {len(tags)} ({', '.join(tags) or 'none'})")
                else:
                    loc = re.search(r"WS Location\s*:?\s*([^\]\n]*)", part2, re.I)
                    if not loc:
                        add("FAIL", f"POINT {n}: part 2 has no WS Location")
                    elif tags[0] in ("WS-MOOL-TEXT", "WS-ARTH") and (not PLACE.search(loc.group(1)) or "NAHI DEKHA" in loc.group(1).upper()):
                        add("FAIL", f"POINT {n}: {tags[0]} needs a WS Location with page or paragraph that was read")
                    else:
                        add("PASS", f"POINT {n}: reply tag {tags[0]} with WS Location")
        if len(pos) == 5 and not re.search(r"RELIEF", body[pos[4]:], re.I):
            add("WARN", f"POINT {n}: part 5 names no RELIEF and its limit")
    # 4. cross-references
    bad_refs = sorted({int(x) for x in re.findall(r"POINT\s+(\d+)\s+dekho", text, re.I)} - set(nums))
    if bad_refs:
        add("FAIL", f"'POINT N dekho' points to missing POINTs: {bad_refs}")
    evs = sorted({f"EV-{int(x):03d}" for x in EV.findall(text)})
    if a.evidence:
        known = {f"EV-{int(x):03d}" for l in open(a.evidence, encoding="utf-8") for x in EV.findall(l)}
        miss = sorted(set(evs) - known)
        add("FAIL" if miss else "PASS", "EV-ids not in the Evidence Register: " + (", ".join(miss) if miss else "none"))
    else:
        add("WARN" if evs else "FAIL", f"EV-ids cited: {len(evs)}" + (" (no register file given, not cross-checked)" if evs else " — no proof is cited by EV-id"))
    # 5. sections of the file
    for name, pat in SECTIONS:
        if not re.search(pat, text, re.I):
            add("FAIL", f"section missing: {name} (write it, or one line LAGU NAHI — reason)")
    wp = re.search(SECTIONS[0][1], text, re.I)
    if wp and heads:
        table = text[wp.end():heads[0][0]]
        absent = [n for n in nums if not re.search(rf"POINT\s*{n}\b", table)]
        if absent:
            add("WARN", f"winning-points table does not list POINT(s) {absent}")
    # 6. audit trail table
    at = re.search(r"AUDIT TRAIL TABLE", text, re.I)
    if at:
        tail = text[at.end():]
        for name, pat in AUDIT_ROWS:
            row = re.search(rf"^\|[^\n]*(?:{pat})[^\n]*$", tail, re.I | re.M)
            if not row:
                add("FAIL", f"Audit Trail Table: category missing: {name}")
                continue
            cells = [c.strip() for c in row.group(0).strip().strip("|").split("|")]
            if len(cells) < 2 or not cells[1]:
                add("FAIL", f"Audit Trail Table: category '{name}' is empty (write the items or KOI NAHI — reason)")
    # 7. leftovers, filing text, language guard
    slots = sorted(set(SLOTS.findall(text)))
    add("FAIL" if slots else "PASS", "unfilled template slots: " + (", ".join(slots[:10]) if slots else "none"))
    filing = sorted({m.group(0).strip()[:40] for m in FILING.finditer(text)})
    add("FAIL" if filing else "PASS", "filing text (core rule 11): " + ("; ".join(filing) if filing else "none"))
    guard = sorted({m.group(0).lower() for m in GUARD.finditer(text)})
    if guard:
        add("WARN", "strong words to check against the language ladder (step 5 needs all three conditions): " + ", ".join(guard))
    worst = any(r["level"] == "FAIL" for r in results)
    if a.json:
        print(json.dumps({"points": len(nums), "results": results, "fail": worst}, indent=2, ensure_ascii=False))
    else:
        for r in results:
            print(f"{r['level']}: {r['message']}")
        print("RESULT: " + ("FAIL (fix first)" if worst else "no pattern failures (this does not prove the file is right)"))
    sys.exit(1 if worst else 0)


if __name__ == "__main__":
    main()

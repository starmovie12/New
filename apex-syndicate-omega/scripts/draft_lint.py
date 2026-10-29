#!/usr/bin/env python3
"""Pattern-based checks on a draft that the user or their advocate wrote (plain text or markdown).
Standard library only. The skill itself writes no draft for filing; this script supports
draft_review (strategy-and-drafting.md): numbering and cross-references, annexures, and
cleanliness (internal IDs, status words, persona names and Vakil File labels pasted into the draft).
It matches patterns; it does not understand the draft, so a PASS is not a legal or factual check.

A reference to another document's paragraph ("para 7 of the written version", "paragraphs 9 to 12
of the WS") is not one of the draft's own paragraphs and is not checked against its numbering.
Annexures are counted when written "Annexure A-3" or inline as the skill drafts them, "(A-3, p.4)";
inline ids count only for the annexure series of the index (A- when no index is given). An id from a
series the index does not use (for example the opposite party's R-3) is reported as another party's
annexure, not as a failure.

  draft_lint.py draft.md --annexures index.txt --copy advocate
  draft_lint.py draft.md --copy clean --stop-at "^(LIST OF ANNEXURES|VERIFICATION)"
"""
import argparse, re, sys
from collections import defaultdict

NUM = re.compile(r"^\s{0,3}(\d{1,3})[.)]\s+\S")
PARA_REF = re.compile(r"\bparas?(?:graphs?)?\.?\s+(\d{1,3}(?:\s*(?:,|and|&|to|-|–)\s*\d{1,3})*)", re.I)
OTHER_DOC = re.compile(r"\s*,?\s*(?:of|in|under)\s+(?:the\s+)?(?:(?:opposite\s+part(?:y|ies)|op|respondents?|complainants?|appellants?)(?:'s|’s|s')?\s+)?"
                       r"(?:written\s+version|written\s+statement|w\.?\s?s\b\.?|reply|complaint|order|affidavit|judge?ment|version|notice|application|petition|memo|appeal|rejoinder|report|evidence)", re.I)
INLINE_ANX = re.compile(r"\(\s*([A-Z]{1,2}-\d{1,3}(?:\s*(?:,|and|&|to|–|-)\s*[A-Z]{1,2}-\d{1,3})*)\s*(?=[,;)]|\s+pp?\.)")
PRAYER_REF = re.compile(r"\bprayer\s*(?:clause\s*)?\(([a-z])\)", re.I)
LABEL = re.compile(r"^\s*\(([a-z])\)\s")
ANX_REF = re.compile(r"\bAnnexures?\s+((?:[A-Z]{1,2}-?\d{1,3})(?:\s*(?:,|and|&|to|-|–)\s*[A-Z]{0,2}-?\d{1,3})*)", re.I)
ID_TOKEN = re.compile(r"([A-Za-z]{1,2})-?(\d{1,3})")
TAGS = re.compile(r"\b(?:D|F|C|X|RH|DL|CH|Q|PR|E|G|L|VR|EV|CR)-\d{1,3}\b")
STATUS = re.compile(r"\b(?:NOT VERIFIED|PRESUMED-FORUM|PRESUMED|DISPUTED|CLIENT-REPORTED|CORROBORATED|WORKING DRAFT|FOR COUNSEL REVIEW|CONFLICTED|UNKNOWN|STALE|SUPERSEDED)\b")
PERSONA = re.compile(r"Apex Syndicate|Sentinel|Red Team|Judge's Chamber|Litigator's Arsenal")
# working labels of power-lines.md and the REF-FILE / GAP-GRAPH / AUDIT-TRAIL material, never printed in a pleading
LABELS = re.compile(r"SROT-SAMARTHIT TATHYA|SROT-SAAR|SATIK SROT-STHAN SATYAPIT NAHI|MOOL WS NAHI DEKHA|"
                    r"MOOL WRITTEN STATEMENT SE SATYAPAN AVASHYAK|WS-MOOL-TEXT|WS-ARTH|SAAR SE — MOOL|JAWAB UPLABDH NAHI|"
                    r"\bRECORD GAP\b|\bNOT READ\b|\bINFERRED\b|\bUNRESOLVED\b|\bLAGU NAHI\b|\bKOI NAHI\b|ELEMENT TAG|"
                    r"\bPROVISIONAL\b|\bTIER-[ABC]\b|WS Location|Audit Trail Table|🟨")
NOTE_BLANK = re.compile(r"\[_{2,}[^\]]*\]")
NOTE_CITE = re.compile(r"\(verify citation before filing\)", re.I)
BRACKET = re.compile(r"\[[^\]\n]+\]")
BRACKET_OK = re.compile(r"^\[(?:\d{4}\]|Annexures?\b|sic\b|emphasis)", re.I)


def ids_from(span):
    toks = [(p.upper(), int(n)) for p, n in ID_TOKEN.findall(span)]
    out, i = [], 0
    has_range = re.search(r"\bto\b|–|-\s*[A-Za-z]", span, re.I) is not None
    while i < len(toks):
        if has_range and i + 1 < len(toks) and toks[i][0] == toks[i + 1][0] and toks[i + 1][1] > toks[i][1] \
                and re.search(rf"{toks[i][0]}-?{toks[i][1]}\s*(?:to|–)\s*{toks[i+1][0]}-?{toks[i+1][1]}", span, re.I):
            out += [f"{toks[i][0]}-{k}" for k in range(toks[i][1], toks[i + 1][1] + 1)]
            i += 2
        else:
            out.append(f"{toks[i][0]}-{toks[i][1]}")
            i += 1
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("draft")
    ap.add_argument("--annexures", help="text file listing the master annexure index (one id per line, e.g. A-1)")
    ap.add_argument("--copy", choices=["advocate", "clean"], default="advocate",
                    help="advocate: a working draft, bracketed notes allowed; clean: a final draft must carry none")
    ap.add_argument("--stop-at", help="regex: ignore numbering from the first line matching it (e.g. an annexure list)")
    a = ap.parse_args()
    text = open(a.draft, encoding="utf-8").read()
    lines = text.splitlines()
    results = []  # (level, message)

    def add(level, msg):
        results.append((level, msg))

    # 1. numbering
    stop = re.compile(a.stop_at, re.I) if a.stop_at else None
    nums = []
    for ln, line in enumerate(lines, 1):
        if stop and stop.search(line):
            break
        m = NUM.match(line)
        if m:
            nums.append((ln, int(m.group(1))))
    if not nums:
        add("WARN", "numbering: no numbered paragraphs found (cannot check)")
        numset = set()
    else:
        numset = {n for _, n in nums}
        bad = []
        expect = 1
        for ln, n in nums:
            if n == expect:
                expect += 1
            elif n < expect:
                bad.append(f"line {ln}: paragraph {n} repeats or goes back (expected {expect})")
            else:
                bad.append(f"line {ln}: paragraph {n} skips ahead (expected {expect})")
                expect = n + 1
        add("FAIL" if bad else "PASS", "numbering: " + (f"{len(bad)} problem(s): " + "; ".join(bad[:8]) if bad else f"continuous 1 to {max(numset)}"))
    # 2. paragraph references
    dang = []
    for ln, line in enumerate(lines, 1):
        for m in PARA_REF.finditer(line):
            if OTHER_DOC.match(line, m.end()):
                continue  # a paragraph of another document (the written version, the order ...)
            for n in map(int, re.findall(r"\d{1,3}", m.group(1))):
                if numset and n not in numset:
                    dang.append(f"line {ln}: refers to paragraph {n}, which does not exist")
    add("FAIL" if dang else "PASS", "paragraph references: " + (f"{len(dang)} dangling: " + "; ".join(dang[:8]) if dang else "all point to existing paragraphs"))
    # 3. prayer references
    labels = {m.group(1).lower() for l in lines for m in [LABEL.match(l)] if m}
    miss = sorted({m.group(1).lower() for m in PRAYER_REF.finditer(text) if m.group(1).lower() not in labels})
    add("FAIL" if miss else "PASS", "prayer references: " + (f"no lettered item for {miss}" if miss else "ok"))
    # 4. annexures
    idx = set()
    if a.annexures:
        for l in open(a.annexures, encoding="utf-8"):
            idx.update(ids_from(l))
    series = {i.split("-")[0] for i in idx} or {"A"}
    refs = []
    for m in ANX_REF.finditer(text):
        refs += ids_from(m.group(1))
    inline = []
    for m in INLINE_ANX.finditer(text):
        inline += [i for i in ids_from(m.group(1)) if i.split("-")[0] in series]
    refs += inline
    refset = set(refs)
    if a.annexures:
        ours = {i for i in refset if i.split("-")[0] in series}
        other = sorted(refset - ours)
        nr, ni = sorted(ours - idx), sorted(idx - ours)
        add("FAIL" if nr else "PASS", "annexures cited but not in index: " + (", ".join(nr) if nr else "none"))
        add("FAIL" if ni else "PASS", "annexures indexed but never cited: " + (", ".join(ni) if ni else "none"))
        if other:
            add("WARN", "annexures of another party or series not in our index (check each is on the record): " + ", ".join(other))
    else:
        add("WARN", f"annexures: no index file given, cannot cross-check ({len(refset)} distinct cited)")
    byp = defaultdict(list)
    for i in refset:
        p, n = i.split("-")
        byp[p].append(int(n))
    gaps = [f"{p}-{k}" for p, ns in byp.items() for k in range(min(ns), max(ns) + 1) if k not in ns]
    if gaps:
        add("WARN", "annexure numbering gaps among cited ids: " + ", ".join(sorted(gaps)))
    # 5. cleanliness
    scrub = ANX_REF.sub(" ", text)
    scrub = INLINE_ANX.sub(lambda m: " " if all(i.split("-")[0] in series for i in ids_from(m.group(1))) else m.group(0), scrub)
    tags = sorted(set(TAGS.findall(scrub)))
    stat = sorted(set(STATUS.findall(text)))
    pers = sorted(set(PERSONA.findall(text)))
    add("FAIL" if tags else "PASS", "internal ids in the draft: " + (", ".join(tags[:12]) if tags else "none"))
    add("FAIL" if (stat or pers) else "PASS", "internal status words or persona names: " + (", ".join(stat + pers) if (stat or pers) else "none"))
    labs = sorted(set(LABELS.findall(text)))
    add("FAIL" if labs else "PASS", "working labels, source tags or reference-file material in the draft: " + (", ".join(labs) if labs else "none"))
    blanks, cites = NOTE_BLANK.findall(text), NOTE_CITE.findall(text)
    if a.copy == "clean":
        add("FAIL" if (blanks or cites) else "PASS", f"clean copy carries no notes: found {len(blanks)} blank(s), {len(cites)} citation note(s)")
    else:
        add("PASS", f"advocate copy notes allowed: {len(blanks)} blank(s), {len(cites)} citation note(s)")
    other = [b for b in BRACKET.findall(text) if not NOTE_BLANK.fullmatch(b) and not BRACKET_OK.match(b)]
    add("WARN" if other else "PASS", "other bracketed text: " + (f"{len(other)} item(s), e.g. {other[:3]}" if other else "none"))
    worst = 0
    for lvl, msg in results:
        print(f"{lvl}: {msg}")
        worst = max(worst, 1 if lvl == "FAIL" else 0)
    print("RESULT: " + ("FAIL (fix first)" if worst else "no pattern failures (this does not prove the draft is correct)"))
    sys.exit(worst)


if __name__ == "__main__":
    main()

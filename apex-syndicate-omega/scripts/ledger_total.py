#!/usr/bin/env python3
"""Totals for the Damages Calculation Ledger (Python standard library only).

Input: CSV (header row) or JSON list of objects. Recognised columns, any case:
  id / RH-id, head, amount, source, period, proof status, double-count (Y/N)
Rows marked double-count = Y are listed but not added. It checks arithmetic only; it cannot tell
whether a loss is really double counted or proved. Use --claimed to compare with the prayer.

  ledger_total.py ledger.csv --claimed 1250000
"""
import argparse, csv, json, re, sys
from collections import OrderedDict, defaultdict
from decimal import Decimal, InvalidOperation

ALIASES = {
    "id": {"id", "rh-id", "rh id", "rh"},
    "head": {"head", "heads", "relief head"},
    "amount": {"amount", "amt", "value"},
    "source": {"source", "document", "doc"},
    "period": {"period"},
    "proof": {"proof", "proof status", "proof_status"},
    "double": {"double-count", "double count", "double_count", "double-count check", "double"},
}


def norm_keys(row):
    out = {}
    for k, v in row.items():
        kk = (k or "").strip().lower()
        for canon, names in ALIASES.items():
            if kk in names:
                out[canon] = (v if v is not None else "")
    return out


def money(s):
    t = re.sub(r"(?i)(rs\.?|inr|₹)", "", str(s)).replace(",", "").strip()
    if t == "":
        raise InvalidOperation
    return Decimal(t)


def inr(d):
    d = d.quantize(Decimal("0.01"))
    s, frac = f"{abs(d):.2f}".split(".")
    head, tail = s[:-3], s[-3:]
    head = re.sub(r"(\d)(?=(\d\d)+$)", r"\1,", head) if head else ""
    body = (head + "," + tail) if head else tail
    return ("-" if d < 0 else "") + "₹" + body + "." + frac


def load(path):
    if path.lower().endswith(".json"):
        data = json.load(open(path, encoding="utf-8"))
        return [norm_keys(r) for r in data]
    with open(path, newline="", encoding="utf-8-sig") as f:
        return [norm_keys(r) for r in csv.DictReader(f)]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file")
    ap.add_argument("--claimed", help="amount in the prayer, to compare with the counted total")
    a = ap.parse_args()
    rows = load(a.file)
    if not rows:
        sys.exit("error: no rows found")
    problems, counted, excluded = [], [], []
    for i, r in enumerate(rows, 1):
        rid = r.get("id") or f"row{i}"
        try:
            amt = money(r.get("amount", ""))
        except InvalidOperation:
            problems.append(f"{rid}: amount '{r.get('amount','')}' is not a number")
            continue
        if amt < 0:
            problems.append(f"{rid}: negative amount {amt}")
        dbl = (r.get("double", "") or "").strip().upper() in {"Y", "YES", "TRUE"}
        rec = {"id": rid, "head": (r.get("head") or "(no head)").strip(), "amount": amt,
               "proof": (r.get("proof") or "(not stated)").strip(), "period": (r.get("period") or "").strip()}
        (excluded if dbl else counted).append(rec)
    seen = defaultdict(list)
    for rec in counted:
        seen[(rec["head"].lower(), rec["amount"], rec["period"])].append(rec["id"])
    for k, ids in seen.items():
        if len(ids) > 1:
            problems.append(f"possible double count (same head, amount, period): {', '.join(ids)}")
    by_head, by_proof = OrderedDict(), OrderedDict()
    for rec in counted:
        by_head[rec["head"]] = by_head.get(rec["head"], Decimal(0)) + rec["amount"]
        by_proof[rec["proof"]] = by_proof.get(rec["proof"], Decimal(0)) + rec["amount"]
    total = sum((rec["amount"] for rec in counted), Decimal(0))
    print(f"Rows: {len(rows)} | counted {len(counted)} | excluded as double-count {len(excluded)}")
    print("By head:")
    for h, v in by_head.items():
        print(f"  {h}: {inr(v)}")
    print("By proof status:")
    for h, v in by_proof.items():
        print(f"  {h}: {inr(v)}")
    for rec in excluded:
        print(f"  excluded {rec['id']} ({rec['head']}): {inr(rec['amount'])}")
    print(f"TOTAL COUNTED: {inr(total)}")
    status = 0
    if a.claimed:
        try:
            claimed = money(a.claimed)
        except InvalidOperation:
            sys.exit("error: --claimed is not a number")
        diff = claimed - total
        if diff == 0:
            print(f"PRAYER CHECK: MATCH ({inr(claimed)})")
        else:
            print(f"PRAYER CHECK: MISMATCH claimed {inr(claimed)} vs counted {inr(total)} (difference {inr(diff)})")
            status = 1
    for p in problems:
        print("FLAG: " + p)
    if problems:
        status = 1
    sys.exit(status)


if __name__ == "__main__":
    main()

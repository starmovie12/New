#!/usr/bin/env python3
"""Totals for the Damages Calculation Ledger (Python standard library only).

Input: CSV (header row) or JSON list of objects. Recognised columns, any case:
  id / RH-id, head, amount (or amount claimed), amount supported, scenario, source, period,
  proof status, double-count (Y/N)
Rows marked double-count = Y are listed but not added. It checks arithmetic only; it cannot tell
whether a loss is really double counted or proved. Use --claimed to compare with the prayer.

Claimed and supported amounts are totalled separately (core rule 27: what is claimed stays apart
from what the documents support). A blank supported amount, or "SUPPORT NAHI", counts as 0 and is
listed. When rows carry a scenario (Kam, Base, Zyada), a row with no scenario counts in every
scenario and a row with a scenario only in its own; no single total is printed across scenarios,
and --claimed then needs --scenario.

A "formula" column (plain arithmetic: numbers, + - * / and brackets; "x" or "×" for times, "9%" for
9/100, commas inside numbers allowed) is computed and compared with the claimed amount, so a
multiplier or interest head cannot carry an arithmetic slip. A difference under one rupee is
reported as rounding; anything more is flagged. Text that is not plain arithmetic is noted as not
machine-checked.

  ledger_total.py ledger.csv --claimed 1250000
  ledger_total.py ledger.csv --claimed 1250000 --scenario Base
"""
import argparse, ast, csv, json, operator, re, sys
from collections import OrderedDict, defaultdict
from decimal import Decimal, InvalidOperation

ALIASES = {
    "id": {"id", "rh-id", "rh id", "rh"},
    "head": {"head", "heads", "relief head"},
    "amount": {"amount", "amt", "value", "amount claimed", "claimed", "claimed amount"},
    "supported": {"amount supported", "supported", "supported amount", "amount supported by documents"},
    "scenario": {"scenario"},
    "source": {"source", "document", "doc"},
    "period": {"period"},
    "proof": {"proof", "proof status", "proof_status"},
    "double": {"double-count", "double count", "double_count", "double-count check", "double"},
    "formula": {"formula", "calculation", "calc"},
}
OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv}
NO_SUPPORT = {"", "-", "support nahi", "none", "nil", "no proof"}


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


def formula_value(expr):
    """Evaluate plain arithmetic with Decimal; raise ValueError for anything else."""
    e = str(expr).strip()
    if not e or len(e) > 300:
        raise ValueError("empty or too long")
    e = re.sub(r"(?i)(rs\.?|inr|₹)", "", e).replace("×", "*").replace("÷", "/")
    e = re.sub(r"(?<=\d),(?=\d)", "", e)
    e = re.sub(r"(\d+(?:\.\d+)?)\s*%", r"(\1/100)", e)
    e = re.sub(r"(?<=[\d)])\s*[xX]\s*(?=[\d(])", "*", e)

    def ev(n):
        if isinstance(n, ast.Expression):
            return ev(n.body)
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and not isinstance(n.value, bool):
            return Decimal(str(n.value))
        if isinstance(n, ast.BinOp) and type(n.op) in OPS:
            return OPS[type(n.op)](ev(n.left), ev(n.right))
        if isinstance(n, ast.UnaryOp) and isinstance(n.op, (ast.USub, ast.UAdd)):
            v = ev(n.operand)
            return -v if isinstance(n.op, ast.USub) else v
        raise ValueError("not plain arithmetic")
    try:
        return ev(ast.parse(e, mode="eval"))
    except (SyntaxError, ZeroDivisionError, InvalidOperation, ArithmeticError) as err:
        raise ValueError(str(err) or "cannot compute")


def inr(d):
    d = d.quantize(Decimal("0.01"))
    s, frac = f"{abs(d):.2f}".split(".")
    head, tail = s[:-3], s[-3:]
    head = re.sub(r"(\d)(?=(\d\d)+$)", r"\1,", head) if head else ""
    body = (head + "," + tail) if head else tail
    return ("-" if d < 0 else "") + "₹" + body + "." + frac


def load(path):
    if path.lower().endswith(".json"):
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        return [norm_keys(r) for r in data]
    with open(path, newline="", encoding="utf-8-sig") as f:
        return [norm_keys(r) for r in csv.DictReader(f)]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file")
    ap.add_argument("--claimed", help="amount in the prayer, to compare with the counted claimed total")
    ap.add_argument("--scenario", help="scenario the prayer follows (needed with --claimed when rows carry scenarios)")
    a = ap.parse_args()
    rows = load(a.file)
    if not rows:
        sys.exit("error: no rows found")
    problems, notes, counted, excluded, formula_lines = [], [], [], [], []
    has_supported = any("supported" in r for r in rows)
    for i, r in enumerate(rows, 1):
        rid = r.get("id") or f"row{i}"
        try:
            amt = money(r.get("amount", ""))
        except InvalidOperation:
            problems.append(f"{rid}: amount '{r.get('amount','')}' is not a number")
            continue
        if amt < 0:
            problems.append(f"{rid}: negative amount {amt}")
        sup = None
        if has_supported:
            raw = (r.get("supported", "") or "").strip()
            if raw.lower() in NO_SUPPORT:
                sup = Decimal(0)
                notes.append(f"{rid}: no documentary support recorded (counted as 0 supported)")
            else:
                try:
                    sup = money(raw)
                except InvalidOperation:
                    problems.append(f"{rid}: supported amount '{raw}' is not a number")
                    sup = Decimal(0)
                if sup > amt:
                    problems.append(f"{rid}: supported amount {sup} is more than the amount claimed {amt}")
        fx = (r.get("formula", "") or "").strip()
        if fx:
            try:
                val = formula_value(fx)
            except ValueError:
                notes.append(f"{rid}: formula '{fx}' is not plain arithmetic, not machine-checked (write it like 45000*12*14)")
            else:
                val = val.quantize(Decimal("0.01"))
                diff = (amt - val).copy_abs()
                if diff == 0:
                    formula_lines.append(f"{rid}: {fx} = {inr(val)} — MATCH")
                elif diff < 1:
                    formula_lines.append(f"{rid}: {fx} = {inr(val)} — amount {inr(amt)} is this figure rounded")
                else:
                    formula_lines.append(f"{rid}: {fx} = {inr(val)} — MISMATCH with amount {inr(amt)}")
                    problems.append(f"{rid}: amount {inr(amt)} does not equal its formula ({inr(val)})")
        dbl = (r.get("double", "") or "").strip().upper() in {"Y", "YES", "TRUE"}
        rec = {"id": rid, "head": (r.get("head") or "(no head)").strip(), "amount": amt, "supported": sup,
               "scenario": (r.get("scenario") or "").strip(),
               "proof": (r.get("proof") or "(not stated)").strip(), "period": (r.get("period") or "").strip()}
        (excluded if dbl else counted).append(rec)
    seen = defaultdict(list)
    for rec in counted:
        seen[(rec["head"].lower(), rec["amount"], rec["period"], rec["scenario"].lower())].append(rec["id"])
    for k, ids in seen.items():
        if len(ids) > 1:
            problems.append(f"possible double count (same head, amount, period): {', '.join(ids)}")
    scenarios = list(OrderedDict.fromkeys(rec["scenario"] for rec in counted if rec["scenario"]))

    def totals(recs):
        claimed = sum((x["amount"] for x in recs), Decimal(0))
        supported = sum((x["supported"] or Decimal(0) for x in recs), Decimal(0))
        return claimed, supported

    print(f"Rows: {len(rows)} | counted {len(counted)} | excluded as double-count {len(excluded)}")
    for rec in excluded:
        print(f"  excluded {rec['id']} ({rec['head']}): {inr(rec['amount'])}")
    if formula_lines:
        print("Formula check:")
        for x in formula_lines:
            print("  " + x)
    status = 0
    if scenarios:
        print("Scenarios: " + ", ".join(scenarios) + " (a row with no scenario counts in every scenario)")
        by_scenario = OrderedDict()
        for sc in scenarios:
            recs = [x for x in counted if x["scenario"] in ("", sc)]
            by_scenario[sc.lower()] = (sc, recs)
            claimed, supported = totals(recs)
            line = f"SCENARIO {sc}: claimed {inr(claimed)}"
            if has_supported:
                line += f" | supported by documents {inr(supported)} | not yet supported {inr(claimed - supported)}"
            print(line)
        print("No single total across scenarios: each scenario is a separate claim, not an award.")
        chosen = None
        if a.claimed:
            if not a.scenario:
                sys.exit("error: rows carry scenarios; give --scenario with --claimed")
            if a.scenario.lower() not in by_scenario:
                sys.exit(f"error: scenario '{a.scenario}' is not in the ledger ({', '.join(scenarios)})")
            chosen = by_scenario[a.scenario.lower()][1]
        compare_total = totals(chosen)[0] if chosen is not None else None
    else:
        by_head, by_proof = OrderedDict(), OrderedDict()
        for rec in counted:
            by_head[rec["head"]] = by_head.get(rec["head"], Decimal(0)) + rec["amount"]
            by_proof[rec["proof"]] = by_proof.get(rec["proof"], Decimal(0)) + rec["amount"]
        print("By head:")
        for h, v in by_head.items():
            print(f"  {h}: {inr(v)}")
        print("By proof status:")
        for h, v in by_proof.items():
            print(f"  {h}: {inr(v)}")
        claimed, supported = totals(counted)
        print(f"TOTAL COUNTED: {inr(claimed)}")
        if has_supported:
            print(f"TOTAL SUPPORTED BY DOCUMENTS: {inr(supported)} | NOT YET SUPPORTED: {inr(claimed - supported)}")
        compare_total = claimed
    if a.claimed:
        try:
            prayer = money(a.claimed)
        except InvalidOperation:
            sys.exit("error: --claimed is not a number")
        diff = prayer - compare_total
        if diff == 0:
            print(f"PRAYER CHECK: MATCH ({inr(prayer)})")
        else:
            print(f"PRAYER CHECK: MISMATCH claimed {inr(prayer)} vs counted {inr(compare_total)} (difference {inr(diff)})")
            status = 1
    for n in notes:
        print("NOTE: " + n)
    for p in problems:
        print("FLAG: " + p)
    if problems:
        status = 1
    print("Arithmetic only: a claimed or scenario total is a claim, not the sum the Commission will award.")
    sys.exit(status)


if __name__ == "__main__":
    main()

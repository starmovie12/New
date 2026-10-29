#!/usr/bin/env python3
"""Self-test for the three scripts. Run: python3 scripts/test_scripts.py"""
import json, os, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))


def run(*args):
    return subprocess.run([sys.executable, *args], capture_output=True, text=True)


def check(name, cond, info=""):
    print(("ok   " if cond else "FAIL ") + name + (f" :: {info}" if (info and not cond) else ""))
    return cond


def main():
    ok = True
    # deadline_calc
    r = run(f"{HERE}/deadline_calc.py", "--trigger", "2026-03-01", "--days", "45", "--today", "2026-03-10", "--json")
    d = json.loads(r.stdout)
    dates = {x["rule"]: x["date"] for x in d["results"]}
    ok &= check("days exclude", dates["exclude"] == "2026-04-15", dates)
    ok &= check("days include", dates["include"] == "2026-04-14", dates)
    ok &= check("risk on earliest date, 35 days", d["days_left_to_earliest"] == 35 and d["risk_flag"] == "SAFE", d)
    ok &= check("forum label", d["date_label"] == "PRESUMED-FORUM")
    r = run(f"{HERE}/deadline_calc.py", "--trigger", "2024-02-29", "--years", "2", "--rule", "exclude", "--today", "2026-03-05", "--json")
    d = json.loads(r.stdout)
    ok &= check("leap day plus 2 years clamps to 28 Feb", d["results"][0]["date"] == "2026-02-28", d)
    ok &= check("expired flag", d["risk_flag"] == "POSSIBLY EXPIRED", d)
    r = run(f"{HERE}/deadline_calc.py", "--trigger", "2026-10-01", "--days", "30", "--rule", "exclude", "--closed-weekdays", "sat,sun", "--today", "2026-10-02", "--json")
    d = json.loads(r.stdout)
    ok &= check("closed day rolls to next open", d["results"][0].get("if_forum_closed_that_day_next_open_date") == "2026-11-02", d)
    ok &= check("bad date rejected", run(f"{HERE}/deadline_calc.py", "--trigger", "2026-13-01", "--days", "5").returncode != 0)
    # ledger_total
    with tempfile.TemporaryDirectory() as t:
        p = os.path.join(t, "l.csv")
        open(p, "w", encoding="utf-8").write(
            "RH-id,Head,Amount,Source,Period,Proof status,Double-count\n"
            "RH-01,Medical expenses,\"₹1,20,000\",D-04,2026-01,DOCUMENTED,N\n"
            "RH-02,Medical expenses,Rs. 80000,D-05,2026-02,DOCUMENTED,N\n"
            "RH-03,Medical expenses,80000,D-05,2026-02,DOCUMENTED,N\n"
            "RH-04,Mental agony,50000,-,,CLIENT-REPORTED,Y\n")
        r = run(f"{HERE}/ledger_total.py", p, "--claimed", "280000")
        ok &= check("ledger total counts 3 rows", "TOTAL COUNTED: ₹2,80,000.00" in r.stdout, r.stdout)
        ok &= check("ledger excludes double-count row", "excluded RH-04" in r.stdout)
        ok &= check("ledger flags possible duplicate", "possible double count" in r.stdout and r.returncode == 1, r.stdout)
        r = run(f"{HERE}/ledger_total.py", p, "--claimed", "300000")
        ok &= check("prayer mismatch flagged", "MISMATCH" in r.stdout and "₹20,000.00" in r.stdout, r.stdout)
        # draft_lint
        good = os.path.join(t, "good.md")
        open(good, "w", encoding="utf-8").write(
            "1. The complainant was admitted on 5 March 2026 (Annexure A-1).\n2. As stated in para 1 above, the discharge followed (Annexures A-2 to A-3).\n"
            "PRAYER\n(a) compensation;\n(b) costs.\n3. The prayer (b) is also supported by para 2.\n")
        idx = os.path.join(t, "idx.txt")
        open(idx, "w", encoding="utf-8").write("A-1\nA-2\nA-3\n")
        r = run(f"{HERE}/draft_lint.py", good, "--annexures", idx)
        ok &= check("clean draft passes", r.returncode == 0, r.stdout)
        bad = os.path.join(t, "bad.md")
        open(bad, "w", encoding="utf-8").write(
            "1. First [D-03] fact (Annexure A-1) NOT VERIFIED.\n3. Third, see para 9 above and Annexure A-7 [____ to be filled by user] (verify citation before filing).\n3. Again.\n"
            "(a) item\nprayer (c)\n")
        r = run(f"{HERE}/draft_lint.py", bad, "--annexures", idx, "--copy", "clean")
        out = r.stdout
        ok &= check("bad draft fails", r.returncode == 1)
        for needle in ["skips ahead", "repeats", "paragraph 9", "no lettered item for ['c']", "A-7", "A-2", "D-03", "NOT VERIFIED", "clean copy carries no notes: found 1 blank(s), 1 citation note(s)"]:
            ok &= check(f"detects: {needle}", needle in out, out)
    print("ALL PASSED" if ok else "SOME FAILED")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()

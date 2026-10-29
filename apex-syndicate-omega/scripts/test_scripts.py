#!/usr/bin/env python3
"""Self-test for the four scripts. Run: python3 scripts/test_scripts.py"""
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
    # interval_calc
    r = run(f"{HERE}/interval_calc.py", "--start", "2026-03-05 11:50 PM", "--end", "2026-03-06 00:15", "--json")
    d = json.loads(r.stdout)
    ok &= check("interval across midnight is 25 minutes", d["minutes"] == 25 and d["crosses_midnight"], d)
    ok &= check("interval step table shows both sides of midnight", len(d["step_table"]) == 3, d)
    r = run(f"{HERE}/interval_calc.py", "--start", "2026-03-05 12:15 AM", "--end", "2026-03-05 12:15 PM", "--json")
    ok &= check("12:15 AM to 12:15 PM is 12 hours", json.loads(r.stdout)["minutes"] == 720, r.stdout)
    ok &= check("00:15 PM rejected", run(f"{HERE}/interval_calc.py", "--start", "2026-03-05 00:15 PM", "--end", "2026-03-06 01:00").returncode != 0)
    ok &= check("24:10 rejected", run(f"{HERE}/interval_calc.py", "--start", "2026-03-05 24:10", "--end", "2026-03-06 01:00").returncode != 0)
    ok &= check("time without a date rejected", run(f"{HERE}/interval_calc.py", "--start", "23:50", "--end", "00:15").returncode != 0)
    r = run(f"{HERE}/interval_calc.py", "--start", "2026-03-06 01:00", "--end", "2026-03-05 23:00", "--json")
    ok &= check("end before start flagged", r.returncode == 1 and "END BEFORE START" in json.loads(r.stdout)["flag"], r.stdout)
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
        # interval_calc record gaps
        ent = os.path.join(t, "e.csv")
        open(ent, "w", encoding="utf-8").write(
            "time,event,source,clock\n"
            "2026-03-05 22:00,vitals,D-04 p.3,nursing\n"
            "2026-03-05 23:00,vitals,D-04 p.3,nursing\n"
            "2026-03-06 02:30,vitals,D-04 p.4,nursing\n"
            "2026-03-06 03:00,ECG,D-07 p.1,ecg machine\n"
            "2026-03-06 05:00,vitals,D-04 p.5,nursing\n")
        r = run(f"{HERE}/interval_calc.py", "--entries", ent, "--gap-minutes", "60", "--kind", "vitals entries", "--json")
        d = json.loads(r.stdout)
        ok &= check("two record gaps found", [g["minutes"] for g in d["gaps"]] == [210, 120], d)
        ok &= check("gap label wording", d["gaps"][0]["label"].startswith("RECORD GAP — 2026-03-05 23:00 se 2026-03-06 02:30 tak — 3h 30m — vitals entries PADHE GAYE PAGES MEIN NAHI MILI"), d)
        ok &= check("gap across two clocks needs a clock note", d["gaps"][1]["clock_note_needed"] and not d["gaps"][0]["clock_note_needed"], d)
        # ledger_total: claimed versus supported, scenarios
        p2 = os.path.join(t, "l2.csv")
        open(p2, "w", encoding="utf-8").write(
            "RH-id,Head,Amount claimed,Amount supported,Scenario,Proof status,Double-count\n"
            "RH-01,Medical expenses,120000,100000,,DOCUMENTED,N\n"
            "RH-02,Loss of income,300000,SUPPORT NAHI,Kam,CLIENT-REPORTED,N\n"
            "RH-02,Loss of income,500000,SUPPORT NAHI,Base,CLIENT-REPORTED,N\n"
            "RH-03,Mental agony,200000,0,,CLIENT-REPORTED,N\n")
        r = run(f"{HERE}/ledger_total.py", p2)
        ok &= check("scenario totals kept apart", "SCENARIO Kam: claimed ₹6,20,000.00 | supported by documents ₹1,00,000.00" in r.stdout
                    and "SCENARIO Base: claimed ₹8,20,000.00" in r.stdout and "TOTAL COUNTED" not in r.stdout, r.stdout)
        ok &= check("no support is noted, not hidden", "RH-02: no documentary support recorded" in r.stdout, r.stdout)
        ok &= check("prayer needs a scenario", run(f"{HERE}/ledger_total.py", p2, "--claimed", "820000").returncode != 0)
        r = run(f"{HERE}/ledger_total.py", p2, "--claimed", "820000", "--scenario", "Base")
        ok &= check("prayer matches the Base scenario", "PRAYER CHECK: MATCH" in r.stdout and r.returncode == 0, r.stdout)
        p3 = os.path.join(t, "l3.csv")
        open(p3, "w", encoding="utf-8").write("RH-id,Head,Amount,Amount supported\nRH-01,Refund,50000,70000\n")
        r = run(f"{HERE}/ledger_total.py", p3)
        ok &= check("supported above claimed flagged", "more than the amount claimed" in r.stdout and r.returncode == 1, r.stdout)
        # ledger_total: formula check
        p4 = os.path.join(t, "l4.csv")
        open(p4, "w", encoding="utf-8").write(
            "RH-id,Head,Amount claimed,Formula\n"
            "RH-01,Loss of dependency,5040000,45000*12*(1-1/3)*14\n"
            "RH-02,Interest,45000,\"2,50,000 x 9% x 2\"\n"
            "RH-03,Interest,33333,100000/3\n"
            "RH-04,Mental agony,300000,lump sum\n")
        r = run(f"{HERE}/ledger_total.py", p4)
        ok &= check("formula with fraction matches", "RH-01: 45000*12*(1-1/3)*14 = ₹50,40,000.00 — MATCH" in r.stdout, r.stdout)
        ok &= check("formula with x and % matches", "RH-02: 2,50,000 x 9% x 2 = ₹45,000.00 — MATCH" in r.stdout, r.stdout)
        ok &= check("rounding is noted, not flagged", "RH-03" in r.stdout and "rounded" in r.stdout and r.returncode == 0, r.stdout)
        ok &= check("prose formula is noted as not checked", "RH-04: formula 'lump sum' is not plain arithmetic" in r.stdout, r.stdout)
        p5 = os.path.join(t, "l5.csv")
        open(p5, "w", encoding="utf-8").write("RH-id,Head,Amount,Formula\nRH-01,Loss of dependency,504000,45000*12*(1-1/3)*14\nRH-02,Bad,10,__import__('os')\n")
        r = run(f"{HERE}/ledger_total.py", p5)
        ok &= check("formula mismatch flagged", "MISMATCH with amount ₹5,04,000.00" in r.stdout and r.returncode == 1, r.stdout)
        ok &= check("code in a formula is refused, not run", "RH-02: formula" in r.stdout and "not plain arithmetic" in r.stdout, r.stdout)
        # interval_calc: separate date and time columns
        e2 = os.path.join(t, "e2.csv")
        open(e2, "w", encoding="utf-8").write("date,time,event\n2026-03-05,11:50 PM,arrival\n2026-03-06,00:40,ECG\n2026-03-06,04/05,bad\n")
        r = run(f"{HERE}/interval_calc.py", "--entries", e2, "--gap-minutes", "30", "--json")
        d = json.loads(r.stdout)
        ok &= check("date and time columns joined across midnight", [g["minutes"] for g in d["gaps"]] == [50], d)
        ok &= check("unparseable time reported with its line", any("line 4" in x for x in d["problems"]) and r.returncode == 1, d)
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
        lab = os.path.join(t, "labels.md")
        open(lab, "w", encoding="utf-8").write(
            "1. No entry is recorded between the two times (Annexure A-1) — RECORD GAP, SROT-SAMARTHIT TATHYA, EV-004.\n"
            "2. The reply says so [WS-MOOL-TEXT] (WS Location: p.3 para 4).\n")
        r = run(f"{HERE}/draft_lint.py", lab)
        for needle in ["RECORD GAP", "SROT-SAMARTHIT TATHYA", "WS-MOOL-TEXT", "WS Location", "EV-004"]:
            ok &= check(f"detects label in a pleading: {needle}", needle in r.stdout and r.returncode == 1, r.stdout)
        # draft_lint on a para-wise rejoinder: the written version's paragraphs, inline annexures, the other side's annexures
        rej = os.path.join(t, "rejoinder.md")
        open(rej, "w", encoding="utf-8").write(
            "1. The contents of para 1 of the written version are denied (A-1, p.2).\n"
            "2. In reply to para 7 of the written version, the first ECG is recorded later (A-2, p.1).\n"
            "3. In reply to paragraphs 9 to 12 of the WS, see para 2 above and the OP's own chart (Annexure R-3).\n"
            "4. As stated in para 6 above, nothing more.\n")
        idx2 = os.path.join(t, "idx2.txt")
        open(idx2, "w", encoding="utf-8").write("A-1\nA-2\n")
        r = run(f"{HERE}/draft_lint.py", rej, "--annexures", idx2)
        out = r.stdout
        ok &= check("written version paragraphs are not our paragraphs", "paragraph 7" not in out and "paragraph 9" not in out and "paragraph 12" not in out, out)
        ok &= check("our own dangling paragraph still caught", "refers to paragraph 6, which does not exist" in out, out)
        ok &= check("inline (A-1, p.2) counts as cited", "annexures indexed but never cited: none" in out, out)
        ok &= check("other party's annexure is a warning", "WARN: annexures of another party or series not in our index (check each is on the record): R-3" in out, out)
    print("ALL PASSED" if ok else "SOME FAILED")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()

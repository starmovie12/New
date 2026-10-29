#!/usr/bin/env python3
"""Calendar arithmetic for ONE deadline (Python standard library only).

It does not know the law. The period, the trigger date and the inclusion rule must come from the
provision you verified (references/legal-research.md, deadline_engine). The result is arithmetic
for the Deadline Register; an advocate still confirms every date.

Examples:
  deadline_calc.py --trigger 2026-03-01 --days 45 --forum PRESUMED --label "appeal"
  deadline_calc.py --trigger 2024-02-29 --years 2 --closed-weekdays sat,sun --json
"""
import argparse, calendar, datetime as dt, json, sys

WEEKDAYS = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]


def add_months(d, n):
    y, m = divmod(d.month - 1 + n, 12)
    y, m = d.year + y, m + 1
    return dt.date(y, m, min(d.day, calendar.monthrange(y, m)[1]))


def end_date(trigger, days, months, years, rule):
    base = add_months(trigger, months + 12 * years) if (months or years) else trigger
    base = base + dt.timedelta(days=days)
    return base if rule == "exclude" else base - dt.timedelta(days=1)


def next_open(d, closed_weekdays, closed_dates):
    while WEEKDAYS[d.weekday()] in closed_weekdays or d in closed_dates:
        d += dt.timedelta(days=1)
    return d


def risk(end, today):
    left = (end - today).days
    if left < 0:
        return "POSSIBLY EXPIRED", left
    if left <= 7:
        return "DANGER", left
    if left <= 30:
        return "WATCH", left
    return "SAFE", left


def parse_date(s):
    try:
        return dt.date.fromisoformat(s)
    except ValueError:
        sys.exit(f"error: '{s}' is not a date in YYYY-MM-DD form")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--trigger", required=True, help="trigger date YYYY-MM-DD")
    p.add_argument("--days", type=int, default=0)
    p.add_argument("--months", type=int, default=0)
    p.add_argument("--years", type=int, default=0)
    p.add_argument("--rule", choices=["exclude", "include", "both"], default="both",
                   help="exclude = trigger day not counted; include = trigger day is day 1; both = show both (default)")
    p.add_argument("--today", help="override today's date (YYYY-MM-DD)")
    p.add_argument("--forum", choices=["ESTABLISHED", "PRESUMED", "UNKNOWN"], default="UNKNOWN")
    p.add_argument("--closed-weekdays", default="", help="comma list, e.g. sat,sun")
    p.add_argument("--closed-dates", default="", help="comma list of YYYY-MM-DD when the forum was closed")
    p.add_argument("--label", default="")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()
    if not (a.days or a.months or a.years):
        sys.exit("error: give --days, --months or --years")
    trigger = parse_date(a.trigger)
    today = parse_date(a.today) if a.today else dt.date.today()
    cw = {w.strip().lower() for w in a.closed_weekdays.split(",") if w.strip()}
    bad = cw - set(WEEKDAYS)
    if bad:
        sys.exit(f"error: unknown weekday(s) {sorted(bad)}")
    cd = {parse_date(x.strip()) for x in a.closed_dates.split(",") if x.strip()}
    rules = ["exclude", "include"] if a.rule == "both" else [a.rule]
    results = []
    for r in rules:
        e = end_date(trigger, a.days, a.months, a.years, r)
        item = {"rule": r, "date": e.isoformat(), "weekday": WEEKDAYS[e.weekday()]}
        if WEEKDAYS[e.weekday()] in cw or e in cd:
            item["if_forum_closed_that_day_next_open_date"] = next_open(e, cw, cd).isoformat()
        results.append(item)
    earliest = min(dt.date.fromisoformat(x["date"]) for x in results)
    flag, left = risk(earliest, today)
    out = {
        "label": a.label, "trigger": trigger.isoformat(),
        "period": {"days": a.days, "months": a.months, "years": a.years},
        "results": results, "today": today.isoformat(),
        "risk_basis": "earliest of the computed dates (conservative)",
        "days_left_to_earliest": left, "risk_flag": flag,
        "forum_status": a.forum,
        "date_label": "PRESUMED-FORUM" if a.forum != "ESTABLISHED" else "forum ESTABLISHED",
        "advocate_check_required": "Y",
        "note": "Arithmetic only. Period, trigger, inclusion rule and any closure extension must come from the verified provision.",
    }
    if a.json:
        print(json.dumps(out, indent=2))
        return
    print(f"Deadline: {a.label or '(unlabelled)'} | trigger {out['trigger']} | period {a.years}y {a.months}m {a.days}d")
    for x in results:
        extra = f" | if closed that day, next open date {x['if_forum_closed_that_day_next_open_date']}" if "if_forum_closed_that_day_next_open_date" in x else ""
        print(f"  rule={x['rule']:7s} -> {x['date']} ({x['weekday']}){extra}")
    print(f"Today {out['today']}: {left} day(s) to the earliest date -> {flag}  [{out['date_label']}]")
    print("Advocate check required: Y. " + out["note"])


if __name__ == "__main__":
    main()

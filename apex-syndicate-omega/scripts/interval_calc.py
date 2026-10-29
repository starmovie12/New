#!/usr/bin/env python3
"""Clock arithmetic for the Master Timeline and GAP-GRAPH (Python standard library only).

Two jobs:
  1. The interval between two recorded date-times (handles AM/PM, 24-hour times and midnight).
  2. RECORD GAPs: from a list of recorded entries, every period longer than a threshold in which
     the list holds no entry.

It does not know medicine or law. A RECORD GAP means only that the entries given to it hold no
entry for that period; it is not proof that care was not given (medical-audit.md,
intervals_and_clocks). Times from different clocks are compared only after the clock note.

Date-times are YYYY-MM-DD HH:MM (24-hour) or YYYY-MM-DD hh:mm AM/PM. The date is always required,
so a time after midnight cannot be put on the wrong day.

  interval_calc.py --start "2026-03-05 11:50 PM" --end "2026-03-06 00:15"
  interval_calc.py --entries entries.csv --gap-minutes 60 --kind "vitals entries" --json

entries.csv has a header row with: time, event (optional), source (optional), clock (optional).
"""
import argparse, csv, datetime as dt, json, re, sys

DT_RE = re.compile(r"^\s*(\d{4}-\d{2}-\d{2})[ T]+(\d{1,2}):(\d{2})\s*([AaPp][Mm])?\s*$")


def parse_dt(s):
    m = DT_RE.match(s or "")
    if not m:
        raise ValueError(f"'{s}' is not 'YYYY-MM-DD HH:MM' or 'YYYY-MM-DD hh:mm AM/PM'")
    day, hh, mm, ampm = m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)
    try:
        date = dt.date.fromisoformat(day)
    except ValueError:
        raise ValueError(f"'{day}' is not a valid date")
    if mm > 59:
        raise ValueError(f"'{s}': minutes must be 00 to 59")
    if ampm:
        if not 1 <= hh <= 12:
            raise ValueError(f"'{s}': with AM/PM the hour must be 1 to 12")
        hh = (0 if hh == 12 else hh) + (12 if ampm.upper() == "PM" else 0)
    elif hh > 23:
        raise ValueError(f"'{s}': a 24-hour time must be 00:00 to 23:59")
    return dt.datetime.combine(date, dt.time(hh, mm))


def fmt(d):
    """Both forms, so 00:15 and 12:15 cannot be confused."""
    return f"{d:%Y-%m-%d %H:%M} ({d:%I:%M %p})"


def span(minutes):
    sign = "-" if minutes < 0 else ""
    h, m = divmod(abs(minutes), 60)
    return f"{sign}{h}h {m:02d}m"


def interval(start, end):
    minutes = int((end - start).total_seconds() // 60)
    days_crossed = (end.date() - start.date()).days
    steps = []
    if days_crossed > 0 and minutes > 0:
        to_midnight = int((dt.datetime.combine(start.date() + dt.timedelta(days=1), dt.time()) - start).total_seconds() // 60)
        after_last_midnight = end.hour * 60 + end.minute
        full_days = days_crossed - 1
        steps = [f"{fmt(start)} to midnight: {span(to_midnight)}"]
        if full_days:
            steps.append(f"{full_days} full day(s): {span(full_days * 1440)}")
        steps.append(f"midnight to {fmt(end)}: {span(after_last_midnight)}")
        steps.append(f"total: {span(minutes)}")
    return {
        "start": fmt(start), "end": fmt(end), "minutes": minutes, "interval": span(minutes),
        "crosses_midnight": days_crossed != 0, "step_table": steps,
        "flag": "END BEFORE START: check the dates, the AM/PM reading and the clock" if minutes < 0 else "",
    }


def load_entries(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    out, problems = [], []
    for i, r in enumerate(rows, 2):
        r = {(k or "").strip().lower(): (v or "").strip() for k, v in r.items()}
        try:
            t = parse_dt(r.get("time", ""))
        except ValueError as e:
            problems.append(f"line {i}: {e}")
            continue
        out.append({"line": i, "time": t, "event": r.get("event", ""), "source": r.get("source", ""),
                    "clock": r.get("clock", "")})
    return out, problems


def gaps(entries, threshold, kind="entries"):
    problems = []
    for a, b in zip(entries, entries[1:]):
        if b["time"] < a["time"]:
            problems.append(f"entries out of time order at lines {a['line']} and {b['line']} (sorted before checking)")
    ordered = sorted(entries, key=lambda e: e["time"])
    found = []
    for a, b in zip(ordered, ordered[1:]):
        minutes = int((b["time"] - a["time"]).total_seconds() // 60)
        if minutes > threshold:
            found.append({
                "from": fmt(a["time"]), "to": fmt(b["time"]), "minutes": minutes, "length": span(minutes),
                "after": f"{a['event']} [{a['source']}]".strip(), "before": f"{b['event']} [{b['source']}]".strip(),
                "clock_note_needed": bool(a["clock"] and b["clock"] and a["clock"] != b["clock"]),
                "label": f"RECORD GAP — {a['time']:%Y-%m-%d %H:%M} se {b['time']:%Y-%m-%d %H:%M} tak — {span(minutes)} — "
                         f"{kind} PADHE GAYE PAGES MEIN NAHI MILI",
            })
    return ordered, found, problems


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--start", help="start date-time")
    p.add_argument("--end", help="end date-time")
    p.add_argument("--entries", help="CSV of recorded entries (time, event, source, clock)")
    p.add_argument("--gap-minutes", type=int, default=60, help="report periods longer than this with no entry (default 60)")
    p.add_argument("--kind", default="entries", help="kind of entries in the list, for the RECORD GAP label (e.g. 'vitals entries')")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()
    note = "Arithmetic only. A RECORD GAP is a gap in the entries given, not proof that care was not given."
    if a.entries:
        if a.gap_minutes <= 0:
            sys.exit("error: --gap-minutes must be above 0")
        entries, problems = load_entries(a.entries)
        if len(entries) < 2:
            sys.exit("error: need at least two valid entries")
        ordered, found, more = gaps(entries, a.gap_minutes, a.kind)
        problems += more
        out = {"entries": len(ordered), "threshold_minutes": a.gap_minutes, "gaps": found,
               "problems": problems, "note": note}
        if a.json:
            print(json.dumps(out, indent=2, ensure_ascii=False))
        else:
            print(f"Entries: {len(ordered)} | first {fmt(ordered[0]['time'])} | last {fmt(ordered[-1]['time'])} | threshold {a.gap_minutes} min")
            for g in found:
                extra = " | CLOCK NOTE NEEDED: the two entries come from different clocks" if g["clock_note_needed"] else ""
                print(f"  {g['label']}{extra}")
                print(f"      after: {g['after']} | before: {g['before']}")
            if not found:
                print("  No period above the threshold without an entry.")
            for x in problems:
                print("FLAG: " + x)
            print(note)
        sys.exit(1 if problems else 0)
    if not (a.start and a.end):
        sys.exit("error: give --start and --end, or --entries")
    try:
        s, e = parse_dt(a.start), parse_dt(a.end)
    except ValueError as err:
        sys.exit(f"error: {err}")
    out = interval(s, e)
    out["note"] = note
    if a.json:
        print(json.dumps(out, indent=2, ensure_ascii=False))
    else:
        print(f"From {out['start']} to {out['end']}: {out['interval']} ({out['minutes']} minutes)")
        for step in out["step_table"]:
            print("  " + step)
        if out["flag"]:
            print("FLAG: " + out["flag"])
        print(note)
    sys.exit(1 if out["flag"] else 0)


if __name__ == "__main__":
    main()

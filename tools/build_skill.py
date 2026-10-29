#!/usr/bin/env python3
"""Validate the apex-syndicate-omega skill and build its .skill package.

Checks (any failure stops the build):
  1. SKILL.md frontmatter: YAML parses, allowed keys only, kebab-case name of at most 64
     characters, description of at most 1024 characters with no angle brackets (the limits
     claude.ai and the Skills API enforce on upload).
  2. No [PENDING:...] placeholder is left in the skill (CHANGELOG.md is history and is skipped).
  3. Every section name the text refers to (a snake_case name such as `audit_trail_table`) is
     defined somewhere in the skill as a heading or a bold key, and every file it names
     (references/x.md, scripts/x.py, a bare `x` that is a reference file) exists.
  4. tests/evals.json is valid JSON with ids 1..N and the required keys in every case.
  5. scripts/test_scripts.py passes.

Then it writes dist/<name>-v<version>.skill: a zip of the skill folder laid out as package_skill
does (<name>/SKILL.md, ...), skipping __pycache__, *.pyc, .DS_Store and a root evals/ folder.
Entries are sorted and time-stamped 1980-01-01 so the same sources give the same bytes.

  python3 tools/build_skill.py                 # validate and build
  python3 tools/build_skill.py --check         # validate only
  python3 tools/build_skill.py --verify-dist   # validate, then confirm dist/ holds exactly the sources
"""
import argparse, hashlib, json, re, subprocess, sys, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "apex-syndicate-omega"
if "--skill" in sys.argv:  # validate another copy (for example an older package), never build from it
    SKILL = Path(sys.argv[sys.argv.index("--skill") + 1]).resolve()
    ROOT = SKILL.parent
DIST = ROOT / "dist"
ALLOWED = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
SNAKE = re.compile(r"(?<![\w/.-])([a-z][a-z0-9]*(?:_[a-z0-9]+)+)(?![\w(])")
# snake_case words that are prose or file/field names, not section references
NOT_SECTIONS = {
    "test_scripts", "deadline_calc", "draft_lint", "ledger_total", "interval_calc",
    "proof_status", "double_count", "skill_name", "eval_name", "expected_output", "must_not",
}


def fail(msg):
    print("FAIL: " + msg)
    return False


def frontmatter():
    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return None, fail("SKILL.md has no frontmatter")
    try:
        import yaml
        fm = yaml.safe_load(m.group(1))
    except ImportError:
        return None, fail("PyYAML is needed for the frontmatter check (pip install pyyaml)")
    except Exception as e:  # yaml.YAMLError and friends
        return None, fail(f"frontmatter is not valid YAML: {e}")
    ok = True
    if not isinstance(fm, dict):
        return None, fail("frontmatter is not a mapping")
    extra = set(fm) - ALLOWED
    if extra:
        ok = fail(f"frontmatter keys not allowed: {sorted(extra)}")
    name = str(fm.get("name", "")).strip()
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        ok = fail(f"name '{name}' must be kebab-case and at most 64 characters")
    if name != SKILL.name:
        ok = fail(f"name '{name}' differs from the folder name '{SKILL.name}'")
    desc = str(fm.get("description", "")).strip()
    if not desc:
        ok = fail("description is missing")
    if len(desc) > 1024:
        ok = fail(f"description is {len(desc)} characters; the limit is 1024")
    if "<" in desc or ">" in desc:
        ok = fail("description contains an angle bracket")
    version = str((fm.get("metadata") or {}).get("version", "")).strip()
    if not version:
        ok = fail("metadata.version is missing")
    title = re.search(r"^# .*\(v([\d.]+)\)", text, re.M)
    if title and title.group(1) != version:
        ok = fail(f"title says v{title.group(1)} but metadata.version is {version}")
    print(f"frontmatter: name={name} version={version} description={len(desc)} chars")
    return fm, ok


def skill_texts():
    files = [SKILL / "SKILL.md"] + sorted((SKILL / "references").glob("*.md"))
    return {p: p.read_text(encoding="utf-8") for p in files}


def check_pending(texts):
    ok = True
    for p, t in texts.items():
        for n, line in enumerate(t.splitlines(), 1):
            if "[PENDING:" in line:
                ok = fail(f"{p.relative_to(ROOT)}:{n}: placeholder left: {line.strip()[:100]}")
    return ok


def defined_names(texts):
    names = set()
    for t in texts.values():
        for heading in re.findall(r"^#{2,4}\s+(.+)$", t, re.M):
            names.update(w for w in re.findall(r"[a-z][a-z0-9_]+", heading) if "_" in w or w == heading.strip())
        names.update(re.findall(r"^\s*-\s+\*\*([a-z][a-z0-9_]+)\*\*", t, re.M))
        names.update(re.findall(r"\*\*principle P\d+ — ([A-Z_]+)\*\*", t))
    return names


def check_references(texts):
    ok = True
    names = defined_names(texts)
    ref_files = {p.stem for p in (SKILL / "references").glob("*.md")}
    for p, t in texts.items():
        # blank out code blocks (templates) but keep their lines, so reported line numbers stay right
        body = re.sub(r"```.*?```", lambda m: "\n" * m.group(0).count("\n"), t, flags=re.S)
        for n, line in enumerate(body.splitlines(), 1):
            for tok in SNAKE.findall(line):
                if tok in NOT_SECTIONS or tok in names:
                    continue
                ok = fail(f"{p.relative_to(ROOT)}:{n}: '{tok}' is referred to but no section defines it")
            for f in re.findall(r"\b(references/[a-z-]+\.md|scripts/[a-z_]+\.py)\b", line):
                if not (SKILL / f).exists():
                    ok = fail(f"{p.relative_to(ROOT)}:{n}: file '{f}' does not exist")
            for f in re.findall(r"\b([a-z]+(?:-[a-z]+)+)\.md\b", line):
                if f not in ref_files:
                    ok = fail(f"{p.relative_to(ROOT)}:{n}: file '{f}.md' does not exist in references/")
            for f in re.findall(r"`([a-z]+(?:-[a-z]+)+)`", line):
                if f in {"apex-syndicate-omega"} or f in ref_files:
                    continue
                if re.fullmatch(r"[a-z]+-[a-z]+(?:-[a-z]+)*", f) and f.endswith(("-lines", "-gates", "-research", "-facts", "-audit", "-drafting", "-templates", "-routing", "-checklists", "-failures", "-interrogation")):
                    ok = fail(f"{p.relative_to(ROOT)}:{n}: reference file '{f}' does not exist")
    print(f"references: {len(names)} section names defined, every reference resolved" if ok else "references: problems above")
    return ok


def check_evals():
    p = SKILL / "tests" / "evals.json"
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
    except ValueError as e:
        return fail(f"tests/evals.json is not valid JSON: {e}")
    ok = True
    evals = d.get("evals", [])
    ids = [e.get("id") for e in evals]
    if ids != list(range(1, len(ids) + 1)):
        ok = fail("evals ids are not 1..N in order")
    for e in evals:
        missing = {"id", "eval_name", "prompt", "files", "expected_output", "must_not", "track"} - set(e)
        if missing:
            ok = fail(f"eval {e.get('id')}: missing {sorted(missing)}")
        if e.get("track") not in {"A", "B", "A+B"}:
            ok = fail(f"eval {e.get('id')}: track must be A, B or A+B")
    names = [e.get("eval_name") for e in evals]
    if len(set(names)) != len(names):
        ok = fail("two evals share an eval_name")
    print(f"evals: {len(evals)} cases")
    return ok


def check_scripts():
    r = subprocess.run([sys.executable, str(SKILL / "scripts" / "test_scripts.py")], capture_output=True, text=True)
    last = (r.stdout.strip().splitlines() or ["(no output)"])[-1]
    print(f"scripts self-test: {last}")
    if r.returncode != 0:
        print(r.stdout)
        return fail("scripts/test_scripts.py failed")
    return True


def build(version):
    DIST.mkdir(exist_ok=True)
    out = DIST / f"{SKILL.name}-v{version}.skill"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for arc, f in package_files().items():
            info = zipfile.ZipInfo(arc, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o755 if f.suffix == ".py" else 0o644) << 16
            z.writestr(info, f.read_bytes())
    with zipfile.ZipFile(out) as z:
        bad = z.testzip()
        if bad:
            sys.exit(f"FAIL: {bad} is corrupt in the package")
        print(f"package: {out.relative_to(ROOT)} ({out.stat().st_size} bytes, {len(z.namelist())} files)")
        for n in z.namelist():
            print(f"  {hashlib.sha256(z.read(n)).hexdigest()[:16]}  {n}")
    print(f"sha256: {hashlib.sha256(out.read_bytes()).hexdigest()}")


def package_files():
    files = {}
    for f in sorted(SKILL.rglob("*")):
        rel = f.relative_to(SKILL)
        if not f.is_file() or "__pycache__" in rel.parts or f.suffix == ".pyc" or f.name == ".DS_Store":
            continue
        if rel.parts and rel.parts[0] == "evals":
            continue
        files[f"{SKILL.name}/{rel.as_posix()}"] = f
    return files


def verify_dist(version):
    out = DIST / f"{SKILL.name}-v{version}.skill"
    if not out.exists():
        return fail(f"{out.relative_to(ROOT)} is missing: run python3 tools/build_skill.py")
    ok = True
    src = package_files()
    with zipfile.ZipFile(out) as z:
        names = set(z.namelist())
        for n in sorted(set(src) - names):
            ok = fail(f"{n} is in the sources but not in the package")
        for n in sorted(names - set(src)):
            ok = fail(f"{n} is in the package but not in the sources")
        for n in sorted(names & set(src)):
            if z.read(n) != src[n].read_bytes():
                ok = fail(f"{n} in the package differs from the source")
    others = sorted(p.name for p in DIST.glob("*.skill") if p != out)
    if others:
        ok = fail(f"stale packages in dist/: {others}")
    print(f"dist: {out.relative_to(ROOT)} matches the sources" if ok else "dist: rebuild with python3 tools/build_skill.py")
    return ok


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="validate only, do not build")
    ap.add_argument("--skill", help="path of another skill copy to validate (implies --check)")
    ap.add_argument("--verify-dist", action="store_true", help="validate, then check that dist/ holds exactly the sources")
    a = ap.parse_args()
    fm, ok = frontmatter()
    texts = skill_texts()
    ok &= check_pending(texts)
    ok &= check_references(texts)
    ok &= check_evals()
    ok &= check_scripts()
    if not ok:
        sys.exit("validation failed: fix the items above")
    print("validation: PASS")
    if a.verify_dist:
        if not verify_dist(str(fm["metadata"]["version"])):
            sys.exit("dist check failed")
        return
    if not (a.check or a.skill):
        build(str(fm["metadata"]["version"]))


if __name__ == "__main__":
    main()

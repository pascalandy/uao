"""Check docs/north-star. Print each problem, or `ok`, and exit 1 on any problem.

- Relative links and anchors resolve, so each linked file exists
- Cited repository paths exist
- Cited SHAs are commits and ancestors of HEAD, so the map cites no upstream commit that uao has not merged.
  The check does not read the snapshot: after a merge of upstream, move the snapshot before you cite a new commit
- Each index (bricks/README.md, decisions/README.md) links to each file in its folder

Usage: python3 docs/north-star/check_links.py [repository root]
"""
import re, subprocess, sys
from pathlib import Path

root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[2]
ns = root / "docs/north-star"
files = sorted(ns.rglob("*.md")) + [root / "AGENTS.md"]
top = {p.name for p in root.iterdir()} - {".git", "node_modules"}

LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)")
CODE = re.compile(r"`([^`\n]+)`")
SHA = re.compile(r"(?<![\w/.-])([0-9a-f]{7,40})(?![\w/-])")
FENCE = re.compile(r"^```.*?^```", re.S | re.M)


def slug(heading: str) -> str:
    s = re.sub(r"[`*_\[\]()]", "", heading.strip().lower())
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")


def anchors(md: Path) -> set[str]:
    return {slug(h) for h in re.findall(r"^#{1,6}\s+(.+)$", FENCE.sub("", md.read_text()), re.M)}


problems, shas = [], {}
for f in files:
    text = f.read_text()
    rel = f.relative_to(root)
    body = FENCE.sub("", text) if f.name != "AGENTS.md" else text
    for target in LINK.findall(body):
        if re.match(r"^[a-z]+:", target):
            continue
        path, _, anchor = target.partition("#")
        dest = (f.parent / path).resolve() if path else f
        if not dest.exists():
            problems.append(f"{rel}: broken link {target}")
        elif anchor and dest.suffix == ".md" and anchor not in anchors(dest):
            problems.append(f"{rel}: missing anchor {target}")
    if f.name == "AGENTS.md":
        continue
    for token in CODE.findall(body):
        cand = re.sub(r":\d+(-\d+)?$", "", token.strip()).rstrip("/")
        if any(c in cand for c in "<>*{} ") or cand.split("/")[0] not in top:
            continue
        if not (root / cand).exists():
            problems.append(f"{rel}: cited path does not exist: {token}")
    for token in CODE.findall(body):
        if re.fullmatch(r"[0-9a-f]{7,40}", token):
            shas.setdefault(token, rel)
    for sha in SHA.findall(body):
        if re.search(r"\d", sha) and re.search(r"[a-f]", sha):
            shas.setdefault(sha, rel)

for folder in ("bricks", "decisions"):
    index = ns / folder / "README.md"
    visible = CODE.sub("", re.sub(r"<!--.*?-->", "", FENCE.sub("", index.read_text()), flags=re.S))
    linked = {target.partition("#")[0] for target in LINK.findall(visible)}
    for md in sorted((ns / folder).glob("*.md")):
        if md.name != "README.md" and md.name not in linked:
            problems.append(f"{index.relative_to(root)}: index does not link {md.name}")

if shas:
    git = subprocess.run(["git", "-C", str(root), "cat-file", "--batch-check"],
                         input="".join(f"{s}^{{commit}}\n" for s in shas), capture_output=True, text=True)
    lines = git.stdout.splitlines()
    if git.returncode or len(lines) != len(shas):
        problems.append(f"git cat-file failed, so no SHA was checked: {git.stderr.strip() or 'wrong output'}")
        lines = []
    for sha, line in zip(shas, lines):
        if line.endswith("missing") or "ambiguous" in line:
            problems.append(f"{shas[sha]}: SHA is not a commit: {sha}")
        elif subprocess.run(["git", "-C", str(root), "merge-base", "--is-ancestor", line.split()[0], "HEAD"]).returncode:
            problems.append(f"{shas[sha]}: SHA is not an ancestor of HEAD: {sha}")

print("\n".join(problems) if problems else "ok")
sys.exit(1 if problems else 0)

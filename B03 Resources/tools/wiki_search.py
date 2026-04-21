#!/usr/bin/env python3
"""Search Markdown under B01/B03/B05 (wiki tree) for a substring. Stdlib only."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


WIKI_DIRS = ("B01 Projects", "B03 Resources", "B05 Systems")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Search markdown files under B01 Projects/, B03 Resources/, B05 Systems/.",
    )
    parser.add_argument("query", help="Substring to search (case-insensitive)")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent.parent.parent,
        help="Repository root (default: inferred from script at B03 Resources/tools/)",
    )
    parser.add_argument(
        "--max-matches",
        type=int,
        default=200,
        help="Stop after this many matching lines total (default: 200)",
    )
    parser.add_argument(
        "--context",
        type=int,
        default=60,
        help="Max characters per preview line (default: 60)",
    )
    args = parser.parse_args()

    roots = []
    for name in WIKI_DIRS:
        p = (args.root / name).resolve()
        if p.is_dir():
            roots.append(p)
    if not roots:
        print(f"No wiki dirs found under {args.root}", file=sys.stderr)
        return 2

    needle = args.query.casefold()
    total_lines = 0
    paths = sorted(
        q
        for r in roots
        for q in r.rglob("*.md")
        if q.is_file()
    )

    for path in paths:
        if total_lines >= args.max_matches:
            break
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            print(f"{path}: read error: {exc}", file=sys.stderr)
            continue

        rel = path.relative_to(args.root)
        for i, line in enumerate(text.splitlines(), start=1):
            if needle not in line.casefold():
                continue
            preview = line.strip()
            if len(preview) > args.context:
                preview = preview[: args.context].rstrip() + "…"
            print(f"{rel}:{i}:{preview}")
            total_lines += 1
            if total_lines >= args.max_matches:
                break

    if total_lines == 0:
        print("No matches.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

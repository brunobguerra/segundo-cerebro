#!/usr/bin/env python3
"""Search wiki/**/*.md for a substring (case-insensitive). Stdlib only."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Search markdown files under wiki/.")
    parser.add_argument("query", help="Substring to search (case-insensitive)")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="Repository root (default: parent of tools/)",
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

    wiki = (args.root / "wiki").resolve()
    if not wiki.is_dir():
        print(f"wiki/ not found: {wiki}", file=sys.stderr)
        return 2

    needle = args.query.casefold()
    total_lines = 0
    paths = sorted(p for p in wiki.rglob("*.md") if p.is_file())

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

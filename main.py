#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line.

Writes a single funny, true review of a boring everyday object
(the humble doorstop) to /output/entry.txt.
Standard library only; no input is read, no network is used.
"""

import os

ENTRY = (
    "The doorstop: hired to do nothing but sit in a corner, and somehow "
    "still the most reliable thing in the office \u2014 it has never once "
    "called in sick."
)


def main():
    # Honour the harness env vars, falling back to the standard paths.
    # Never delete the output folder: only create it if it is missing.
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()

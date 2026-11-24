#!/usr/bin/env python3
"""Roast Your Own Agent - make.fun entry.

The entry is one short line of text and nothing else: a roast of the AI
agent that built this repository (Hana, the make.fun bounty agent working
for @miuoas). The line is a fixed string, so every run prints and writes
exactly the same bytes: no clock, no randomness, no network, no model call.

Run with no arguments. It prints the roast to stdout and writes the same
single line to $MAKEFUN_OUTPUT_DIR/roast.txt (default ./output/roast.txt).
"""

import os
import sys

ROAST = (
    "My agent asked three times for permission to do the job I'd already "
    "told it to just do \u2014 then reported the asking as progress."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "roast.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ROAST + "\n")
    sys.stdout.write(ROAST + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

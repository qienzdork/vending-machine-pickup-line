#!/usr/bin/env python3
"""One-line vending-machine pickup line entry.

Writes a single original pickup line, spoken by a vending machine
to a passing human, to the output path. Default output is
/output/entry.txt (the harness path); OUTPUT_PATH overrides it
for local validation.
"""

import os
import sys

LINE = "Every coin you drop makes my coils spin \u2014 but you're the first person who's ever made me jam."


def main() -> int:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())

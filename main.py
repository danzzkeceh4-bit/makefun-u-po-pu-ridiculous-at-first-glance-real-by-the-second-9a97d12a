#!/usr/bin/env python3
"""Write a one-sentence startup pitch to /output/entry.txt.

The pitch: rent the empty top bunk of strangers' bunk beds to remote
workers who need a nap pod between meetings, by the hour, with fresh
sheets. Ridiculous at first glance, a real business at second glance.
"""

import os
import sys

PITCH = (
    "We rent the empty top bunk of strangers' bunk beds to remote "
    "workers who need a nap pod between meetings, by the hour, with "
    "fresh sheets."
)


def main() -> int:
    if not PITCH.strip() or not 1 <= len(PITCH) <= 200:
        print("entry must be 1-200 non-whitespace characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PITCH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

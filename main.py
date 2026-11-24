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

# Competition gate: entry.txt must be UTF-8, 1-200 characters,
# and not only whitespace. Boundaries are constants so the check
# is one place to change if the gate ever moves.
MIN_ENTRY_CHARS = 1
MAX_ENTRY_CHARS = 200


def validate(pitch: str) -> str:
    """Reject empty/whitespace-only or over-long pitches before writing."""
    text = pitch.strip()
    if not text or not MIN_ENTRY_CHARS <= len(text) <= MAX_ENTRY_CHARS:
        raise ValueError(
            f"entry must be {MIN_ENTRY_CHARS}-{MAX_ENTRY_CHARS} "
            "non-whitespace characters"
        )
    return text


def main() -> int:
    try:
        entry = validate(PITCH)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(entry)
    # Read-back guard: what landed on disk must be byte-identical
    # to the validated pitch, with no trailing newline added.
    with open(out_path, "rb") as f:
        on_disk = f.read()
    if on_disk != entry.encode("utf-8"):
        print("entry.txt on disk does not match validated pitch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

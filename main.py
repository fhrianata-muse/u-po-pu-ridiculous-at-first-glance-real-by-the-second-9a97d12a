#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second — entry program.

Writes one sentence (a bizarre startup pitch that holds up as a real
business) to /output/entry.txt. The sentence is kept as data; before
writing, the program re-checks the competition gate itself: plain text,
one line, 1 to 200 characters, not only white space, no leading or
trailing space, ending on terminal punctuation so the pitch reads complete.
"""

import sys
from pathlib import Path

ENTRY = "We hire retired football referees to settle couples' arguments, because partners pay $50 an hour for a neutral whistle and a red card ends the fight faster than therapy."

OUT = Path("/output/entry.txt")


def check(text):
    """Return a reason the text fails the gate, or None when it passes."""
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    if not 1 <= len(text) <= 200:
        return "entry must be 1 to 200 characters, got %d" % len(text)
    if not text.strip():
        return "entry must not be only white space"
    if text != text.strip():
        return "entry must not start or end with white space"
    if any(ord(ch) < 32 for ch in text):
        return "entry must not contain control characters"
    if "  " in text:
        return "entry must not contain double spaces"
    if text[-1] not in ".!?":
        return "entry must end with terminal punctuation"
    return None


def main():
    problem = check(ENTRY)
    if problem is not None:
        print("gate failed: " + problem, file=sys.stderr)
        raise SystemExit(1)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

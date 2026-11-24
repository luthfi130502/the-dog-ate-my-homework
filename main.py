#!/usr/bin/env python3
"""Entry for "The Dog Ate My Homework: Funniest Excuse".

Writes the dog's one-line defense to /output/entry.txt.
Pure standard library.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

LINE = (
    "It was on the floor, and by dog law everything on the floor is mine. "
    "I sniffed your answers first - three were wrong, so technically, I saved you."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, "line must fit the 1-200 char gate"
    assert LINE.strip(), "line must not be whitespace-only"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")
    print("wrote %d chars to %s" % (len(LINE), OUTPUT_PATH))


if __name__ == "__main__":
    main()

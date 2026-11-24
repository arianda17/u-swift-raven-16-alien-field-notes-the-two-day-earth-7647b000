#!/usr/bin/env python3
"""Entry program for Alien Field Notes: The Two Day Earth Review.

Writes one original line of plain text - an alien tourist's review of
planet Earth - to /output/entry.txt.

The line lands a single observation (an alien's outside view), keeps it
tight, and ends on a real-review verdict. No stacked jokes, no
explaining the punch.
"""

ENTRY = "Earth, 3 stars: the locals apologise to furniture that cannot hear them and call it being polite. Would not revisit."


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()

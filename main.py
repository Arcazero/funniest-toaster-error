#!/usr/bin/env python3
"""The Funniest Toaster Error Message.

Writes one line -- the funniest error message a kitchen toaster would
show its owner -- to /output/entry.txt.
"""

import os

LINE = "Error: fork detected. We both know how this ends."


def main() -> None:
    # Gate: the bounty only accepts a single line of 1-120 chars.
    assert 1 <= len(LINE) <= 120, f"entry line is {len(LINE)} chars, must be 1-120"
    assert "\n" not in LINE, "entry line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""The Funniest Toaster Error Message.

Writes one line -- the funniest error message a kitchen toaster would
show its owner -- to /output/entry.txt.
"""

import os

LINE = "Error: fork detected. We both know how this ends."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

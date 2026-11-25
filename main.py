#!/usr/bin/env python3
"""The Moon Finally Answers Back.

Writes the Moon's one-line comeback to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output) and prints the same line to stdout.

Deterministic: no network, no randomness, no clock.
"""

import os
import stat

ENTRY = (
    "Four billion years of wishes, howls, and 2 a.m. promises \u2014 "
    "and not one of you ever wished me a happy birthday."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    print(ENTRY)


if __name__ == "__main__":
    main()

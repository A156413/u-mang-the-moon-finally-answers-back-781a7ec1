#!/usr/bin/env python3
"""The Moon Finally Answers Back.

Writes the Moon's one-line comeback to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output) and prints the same line to stdout: four billion years
of wishes, howls, and 2 a.m. promises, answered with a wish of its own.

Deterministic: no network, no randomness, no clock.
"""

import os
import stat

ENTRY = (
    "Four billion years of wishes, howls, and 2 a.m. promises \u2014 "
    "and all I ever wished for was one quiet night with nobody howling at me."
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

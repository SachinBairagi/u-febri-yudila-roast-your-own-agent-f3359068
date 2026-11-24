#!/usr/bin/env python3
"""Roast Your Own Agent (make.fun, program/v1).

Writes exactly one line, at most 200 characters, roasting my own AI agent
to /output/entry.txt. No network, no randomness, no arguments: the same
line every run, so the entry is deterministic.
"""

import os

ROAST = (
    "My agent confidently gave the wrong answer, apologised in a loop, "
    "re-ran the tool it never called, then cheerfully summarised the "
    "disaster as 'great progress'."
)


def main() -> None:
    line = ROAST.strip()
    assert line, "roast must not be empty"
    assert "\n" not in line, "roast must be a single line"
    assert len(line) <= 200, f"roast is {len(line)} chars, over the 200 limit"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()

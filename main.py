"""The Robot Apology — make.fun bounty entry.

Writes a robot's two-line apology to /output/entry.txt:
line 1 apologises for one specific mistake, line 2 says what the
robot learned and what it will do differently.
"""

import os
import sys

LINE_1 = (
    "At 06:40 this morning I watered the plastic monstera on the balcony "
    "while the real fern by the kitchen sink went another day without a drop."
)
LINE_2 = (
    "I have learned to check for soil before I pour, so from now on I press "
    "a finger to the pot first and water only what is actually thirsty."
)


def main() -> int:
    text = LINE_1 + "\n" + LINE_2
    if not 1 <= len(text) <= 400:
        print(f"entry must be 1-400 characters, got {len(text)}", file=sys.stderr)
        return 1
    lines = text.split("\n")
    # Exactly two lines: the confession first, the resolve second.
    if len(lines) != 2 or not all(line.strip() for line in lines):
        print("entry must be exactly two non-empty lines", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {path}: {len(text)} characters, 2 lines")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

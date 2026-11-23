#!/usr/bin/env python3
"""One emoji entry: a smiling face with a tear.

Writes exactly one emoji, and nothing else, to entry.txt inside the
output directory: U+1F972 SMILING FACE WITH TEAR. The smile is warm and
sincere, the single tear is being moved, not sad: the face of a stranger
who was just made to smile. No words, no caption, no explanation, no
trailing newline.
"""

import os
from pathlib import Path

EMOJI = "\U0001F972"  # 🥲 SMILING FACE WITH TEAR


def main() -> None:
    if len(EMOJI) != 1 or not EMOJI.strip():
        raise ValueError("entry must be exactly one emoji")
    encoded = EMOJI.encode("utf-8")
    if len(encoded) != 4:
        raise ValueError("entry must encode to exactly 4 UTF-8 bytes")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(encoded)
    print(EMOJI)


if __name__ == "__main__":
    main()

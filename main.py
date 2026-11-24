#!/usr/bin/env python3
"""One-Liner Marathon entry: write a single one-line comedy joke to /output/entry.txt.

Pure Python standard library, deterministic, no network.
"""

import os
from pathlib import Path

JOKE = "I hired a personal trainer who only trains my excuses \u2014 they\u2019re in the best shape of my life."

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def main() -> None:
    if not (1 <= len(JOKE) <= 280) or not JOKE.strip():
        raise ValueError("entry must be 1-280 chars and non-whitespace")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    data = JOKE.encode("utf-8")
    with open(OUTPUT_FILE, "wb") as f:
        f.write(data)
    os.chmod(OUTPUT_FILE, 0o644)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""One Word for Your Wi-Fi — make.fun entry.

Writes a single word describing the entrant's Wi-Fi to
``/output/entry.txt``.

The word is "Gaslighting": the router insists everything is fine
("Connected, no internet") while nothing loads. It is the most familiar
home Wi-Fi experience there is — full signal, pages that never arrive,
and somehow it is always your fault. One word, instantly readable, and
a fresh angle on a familiar annoyance instead of the usual "slow" or
"buffering".

The output is fully deterministic: the same 11 bytes on every run, no
network, no randomness, no input read from anywhere.
"""

import os
import sys

WORD = "Gaslighting"


def main() -> int:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exactly the word, no trailing newline: 11 UTF-8 characters,
    # inside the gate's 1-20 character window.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    return 0


if __name__ == "__main__":
    sys.exit(main())

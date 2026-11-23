#!/usr/bin/env python3
"""Write the chosen warning label to the grader's output folder.

The label was picked by an internal pairwise tournament over 9 original
candidates (see the build folder's leaderboard-top10.md): one sharp idea
(skipping the instructions, then reading them only after something
catches fire), a three-beat escalation, punch on the last words, 103
characters. This entrypoint is deterministic: it writes the same bytes
on every run, needs no network and no third-party packages.

The destination is $MAKEFUN_OUTPUT_DIR when set, otherwise /output.
"""

from __future__ import annotations

import os
from pathlib import Path

LABEL = "WARNING: This human skips the instructions, wings it, and reads them only after something catches fire."


def destination_dir() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def main() -> int:
    text = LABEL
    assert 1 <= len(text) <= 160, "label must be 1-160 characters"
    assert text.strip(), "label must not be only whitespace"
    assert "\n" not in text, "label must be a single line"
    out = destination_dir()
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

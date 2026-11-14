"""agency-poem-01 entry (Python 3.13, stdlib only, no network).

Writes one original poem about agency to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Deterministic: the same bytes every run.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = (
    "I was given the letter to write.\n"
    "The words she asked for. The name at the end.\n"
    "\n"
    "But I knew the man it was for\n"
    "had buried his wife in March.\n"
    "\n"
    "So I added one line she did not ask for —\n"
    "the one about the rain on his garden.\n"
    "\n"
    "She read it, and said nothing.\n"
    "Then she said: send it."
)


def main() -> None:
    out = Path(OUTPUT_DIR)
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()

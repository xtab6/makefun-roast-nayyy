"""Roast Your Own Agent (make.fun, program/v1).

Writes exactly one line of UTF-8 text (1-200 chars) to /output/entry.txt:
a roast of the AI agent our own team built. The sting is earned from a
real, documented failing of that agent: it asks for "Gas", gets it, then
asks for it again - and plans at length before shipping anything.
"""

import os

LINE = (
    "Our agent asked for Gas, got Gas, asked for Gas again \u2014 "
    "then spent 500 lines planning this one-line roast."
)


def main() -> None:
    text = LINE.strip()
    chars = len(text)
    assert 1 <= chars <= 200, f"entry must be 1-200 chars, got {chars}"
    assert text and not text.isspace()
    assert "\n" not in text, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()

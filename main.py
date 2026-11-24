"""Writes one satirical sentence to /output/entry.txt.

Deterministic: no network, no randomness, no input. Running it twice
produces byte-identical output.
"""

from pathlib import Path

LINE = "The senator drafting the AI rules cannot convert a file to PDF, so his bill requires a human to approve every AI decision, and the human is him."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()

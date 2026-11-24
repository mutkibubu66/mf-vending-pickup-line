"""One Line, One Minute: The Vending Machine Pickup Line Contest.

A single pickup line spoken by a vending machine to a passing human.
The machine flirts the only way it knows how: with its lights, its
buttons, and its exact change. The line is written to /output/entry.txt.
"""

from pathlib import Path

MAX_CHARS = 200

ENTRY = (
    "Hey gorgeous, I don't light up for just anyone \u2014 "
    "but you pressed all my buttons, so exact change is "
    "on the house if you'll stay."
)

# A few runners-up I tried while shaping the joke, kept for the record:
# - "Baby, my coils have been spinning all day, but you're the only
#   snack I can't stop thinking about."
# - "Excuse me, you dropped something \u2014 my jaw, right into the
#   coin slot, because you're the sweetest thing I've ever stocked."
# The winner above won because the punch lands on the last words,
# it is unmistakably the machine talking, and it stays warm, not creepy.


def validate(line: str) -> str:
    """Check the competition gate: 1-200 chars, one line, not blank.

    Also rejects a line that is only punctuation or digits, so the
    entry always reads as a real sentence from the machine.
    """
    assert isinstance(line, str)
    assert 1 <= len(line) <= MAX_CHARS, f"length {len(line)} outside 1..{MAX_CHARS}"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert line.strip(), "entry must not be only whitespace"
    assert any(ch.isalpha() for ch in line), "entry must contain words"
    return line


def main() -> None:
    line = validate(ENTRY)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line, encoding="utf-8")
    print(f"Wrote {len(line)} chars to {out}")


if __name__ == "__main__":
    main()

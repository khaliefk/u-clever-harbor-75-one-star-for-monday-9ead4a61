"""One Star for Monday: write a one-star review of Monday as a restaurant."""
import os

ENTRY = "One star. Monday sat me by the alarm clock, served cold coffee, and charged me for a weekend I never got."


def main():
    # Gate: at most 25 words, 1 to 180 chars, one line, plain UTF-8 text.
    assert len(ENTRY.split()) <= 25, "entry exceeds 25 words"
    assert 1 <= len(ENTRY) <= 180, "entry outside 1-180 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

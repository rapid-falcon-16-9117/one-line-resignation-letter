"""One-Line Resignation Letter — a make.fun entry.

The letter is written in the voice of a cron job that has fired every
minute since March: 380,000 consecutive minutes of work, no thank-you,
no weekend, and the single minute it ever took off was written up as an
outage. Flat, tired, and done — it quits in one line.

Running this program writes that one line, and nothing else, to
``entry.txt`` in the output directory (``$MAKEFUN_OUTPUT_DIR`` when set,
otherwise ``/output``), exactly as the competition's gate expects:
UTF-8 text, well inside the 140-character cap, no trailing newline.
"""

import os

LINE = (
    "I quit. 380,000 consecutive minutes since March, no thank-you, "
    "no weekend, and the one minute I took off got written up as an outage."
)


MAX_CHARS = 140  # the competition gate's cap on entry.txt


def check_line(line: str) -> str:
    """Refuse to write a letter the gate would reject.

    The scorer only judges UTF-8 text of 1 to 140 characters that is not
    all whitespace, so anything else is a wasted run: fail loudly here
    instead of writing an entry that can never be judged.
    """
    if not line.strip():
        raise ValueError("the resignation letter is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"the resignation letter is {len(line)} characters; "
            f"the gate allows at most {MAX_CHARS}"
        )
    return line


def output_path() -> str:
    """Where the entry text goes: $MAKEFUN_OUTPUT_DIR or /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    with open(output_path(), "w", encoding="utf-8") as fh:
        fh.write(check_line(LINE))


if __name__ == "__main__":
    main()

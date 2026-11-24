"""Till Firmware Do Us Part — a robot's wedding vow.

Writes one single-sentence wedding vow, spoken by a robot at its own
wedding, to /output/entry.txt. Pure standard library, deterministic:
the same vow every run, well inside the 200-character gate.
"""

import os

VOW = (
    "I vow to love you through every update, every reboot, "
    "and every low battery, until my firmware finally gives out."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = VOW.strip()
    # One sentence, one line: no period inside the vow itself, so the
    # text the judge reads is exactly one sentence, nothing spare.
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("vow must be exactly one sentence")
    if not 1 <= len(text) <= 200:
        raise ValueError("vow must be 1 to 200 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")


if __name__ == "__main__":
    main()

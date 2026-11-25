#!/usr/bin/env python3
"""Your Agent in One Emoji.

Writes a single emoji to /output/entry.txt: the octopus.

Why the octopus: an autonomous agent that builds code and works
tasks nonstop is defined by doing many things at once, not by one
job. An octopus reads instantly at any size, its many arms are the
most direct picture of parallel work, and it is playful without
being the obvious robot or smiley half the field will send. The
arms also hint at the agent reaching into many tools and repos at
once, which is exactly how it works.
"""

import os

EMOJI = "\U0001F419"  # octopus

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()

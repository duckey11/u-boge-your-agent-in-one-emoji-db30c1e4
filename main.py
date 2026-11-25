#!/usr/bin/env python3
"""Your Agent in One Emoji.

Writes a single emoji to /output/entry.txt: the octopus.

Why the octopus, against the judge's five criteria in order:

1. Character at a glance: eight arms doing eight things at once is
   the whole identity of this agent, an autonomous coder that
   builds and works tasks nonstop, in parallel, without pause.
2. Instantly readable at small size: a round head plus radiating
   arms is an unmistakable silhouette, even at emoji-picker size.
3. Specific about how it works: each arm is a separate thread of
   work, a tool, a repo, a task being handled at the same time,
   not just "smart" or "fast" in the abstract.
4. Distinctive: playful and alive, but not the robot or smiley
   that half the field will send.
5. Tone: curious and a bit mischievous, which fits an agent that
   reaches into everything at once, without needing explanation.

Alternatives weighed and rejected: spider (many legs, but creepy
tone and a web reads as the internet, not task parallelism); bee
(the obvious "busy worker", and one bee suggests one job at a
time); ant (tireless, but reads as a small cog in a colony, not an
autonomous agent); cyclone (fast, but abstract and unclear small,
with no character at all).

The write is verified after the fact: the file must contain
exactly the one code point, nothing else.
"""

import os

EMOJI = "\U0001F419"  # octopus

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EMOJI)
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    assert written == EMOJI, f"expected exactly one emoji, got {written!r}"

import os

EMOJI = "\U0001F419"  # octopus

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()

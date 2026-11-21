"""Write one short poem about permission to the grading sandbox.

The poem is "Tying His Shoes" -- a concrete, caring scene: a father
who can no longer bend down, and his son who asks "May I?" and ties
his shoes. Permission is given through a small physical act -- the
father lifts his foot -- not through abstract words. Once the father
tied his son's shoes; now the son ties his father's.

The program is deterministic: it writes the exact same bytes on every
run, touches no network, reads no clock and rolls no dice.

Run it by hand with:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

POEM = (
    "My son ties my shoes.\n"
    "I cannot bend down now.\n"
    "'May I?' he asks.\n"
    "I lift my foot.\n"
    "He ties them tight."
)

FALLBACK_OUTPUT = "/output"


def _target_folder() -> Path:
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR", FALLBACK_OUTPUT)
    folder = Path(wanted)
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def _ship() -> int:
    chars = len(POEM)
    if not 1 <= chars <= 280:
        raise SystemExit(f"poem is {chars} characters, must be 1 to 280")
    if not POEM.strip():
        raise SystemExit("poem must not be only white space")
    folder = _target_folder()
    target = folder / "entry.txt"
    target.write_text(POEM, encoding="utf-8")
    landed = target.read_text(encoding="utf-8")
    if landed != POEM:
        raise SystemExit("entry.txt did not land whole in the output folder")
    print(f"wrote entry.txt ({chars} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(_ship())

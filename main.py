"""Write one short poem about permission to the grading sandbox.

The poem is "My Mother Is Everything" -- a concrete, caring scene:
a child in hospital, held by his mother. She asks "May I go and
sell?" because his brothers wait at home, hungry. She sells, buys
rice, and returns to his bedside. Permission is asked and given, and
she comes back. My mother is everything.

The program is deterministic: it writes the exact same bytes on every
run, touches no network, reads no clock and rolls no dice.

Run it by hand with:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

POEM = (
    "My mother holds my hand in the hospital.\n"
    "'May I go and sell?' she asks.\n"
    "My brothers wait at home, hungry.\n"
    "She sells, buys rice, and returns.\n"
    "Her hand finds mine again.\n"
    "My mother is everything."
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

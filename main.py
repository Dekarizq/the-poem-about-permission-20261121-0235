"""Write one short poem about permission to the grading sandbox.

The poem is "Tying His Shoes" -- a longer, fuller version of the
scene that scored best so far (87.84%, 11-0-0): a father who can no
longer bend down, and his son who kneels, asks "May I?", and ties
his shoes with a double knot, the way his father taught him. Once
the father tied his son's shoes; now the son ties his father's, and
the father lets him. Permission is asked, given through a lifted
foot, and held without hurrying.

The program is deterministic: it writes the exact same bytes on every
run, touches no network, reads no clock and rolls no dice.

Run it by hand with:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

POEM = (
    "My son kneels and ties my shoes.\n"
    "I cannot bend down now.\n"
    "'May I?' he asks.\n"
    "I lift my foot.\n"
    "He pulls the laces tight, double knot,\n"
    "the way I taught him.\n"
    "Once, I tied his shoes.\n"
    "Now he ties mine.\n"
    "He does not hurry,\n"
    "and I let him."
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

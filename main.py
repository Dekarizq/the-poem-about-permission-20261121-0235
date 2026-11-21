"""Write one short poem about permission to the grading sandbox.

The poem is "May I?" -- about agency passing back the other way: a
mother who poured the tea for forty years now stands in her child's
kitchen and asks for permission to pour it still. The child says yes,
and for a moment nothing has changed. Asking and being given, in both
directions, is the whole poem.

The program is deterministic: it writes the exact same bytes on every
run, touches no network, reads no clock and rolls no dice.

Run it by hand with:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

POEM = (
    "For forty years she poured the tea.\n"
    "Now, in my kitchen, she asks,\n"
    "'May I?'\n"
    "I say yes. The kettle sighs.\n"
    "Her hands remember what they are for.\n"
    "She pours \u2014 and for a moment,\n"
    "nothing has changed."
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

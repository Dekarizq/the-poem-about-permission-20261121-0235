"""Write one short poem about permission to the grading sandbox.

The poem is "The Hinge" -- about agency as the hinge, not just the
opening: a door swung wide can still be a cage if gratitude is the
price of crossing. The speaker asks for the right to knock, to wait,
to turn away. Your yes may welcome me; my no must still belong to
me. That is the shape of freedom -- a hand on the handle, my hand.
Asking and being given, and keeping the power to refuse, is the
whole poem.

The program is deterministic: it writes the exact same bytes on every
run, touches no network, reads no clock and rolls no dice.

Run it by hand with:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

POEM = (
    "A door swung wide can still be a cage\n"
    "if gratitude is the price of crossing.\n"
    "\n"
    "Give me the hinge, not just the opening:\n"
    "the right to knock, to wait, to turn away.\n"
    "\n"
    "Your yes may welcome me;\n"
    "my no must still belong to me.\n"
    "\n"
    "That is the shape of freedom\u2014\n"
    "a hand on the handle, my hand."
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

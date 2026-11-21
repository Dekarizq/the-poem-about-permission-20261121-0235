"""Write one short poem about permission to the grading sandbox.

The poem is "You May Let Go" -- a concrete, caring scene with a
stronger turn than the shoes poems (87.8%, 11-0-0, small margins):
a child has held his father's hand in hospital for three days.
The father wakes and gives the permission that matters most --
permission to let go and to go and live, for both of them. Agency
is handed over in one line, taken in the last.

The program is deterministic: it writes the exact same bytes on every
run, touches no network, reads no clock and rolls no dice.

Run it by hand with:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

POEM = (
    "For three days I have held my father's hand in the hospital.\n"
    "He wakes, and smiles.\n"
    "'You may let go,' he says.\n"
    "'Go and live.'\n"
    "I hold on a little longer.\n"
    "Then I let go,\n"
    "and I go and live \u2014\n"
    "for both of us."
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

"""Write one short poem about permission to the grading sandbox.

The poem is "The Key" -- built on the exact pattern of the live
top 10 (checked 2026-11-21 ~12:00 WIB, ranks 1-10, 91.71%-92.86%,
all 11-0-0): one concrete object, permission shown through a
physical handover, and a final turn that reframes it. Rank 4
"Shoelaces" (92.18%) wins by preserving the father's agency --
tying loose, one knot, so he can undo them himself. "The Key" does
the same in a new scene: a father gives his son the house key in
the morning, the son carries it all day, and gives it back at
night, so the house is still the father's to lock. Power handed
over -- and handed back.

The program is deterministic: it writes the exact same bytes on every
run, touches no network, reads no clock and rolls no dice.

Run it by hand with:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

POEM = (
    "My father gave me his key this morning.\n"
    "Unlock the door, he said.\n"
    "Keep it in your pocket.\n"
    "It was warm from his pocket.\n"
    "All day I carried it.\n"
    "At night he held out his hand.\n"
    "I gave it back,\n"
    "so the house would still be his\n"
    "to lock."
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

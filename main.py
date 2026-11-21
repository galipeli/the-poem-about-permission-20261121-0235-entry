"""The poem about permission.

Writes one short poem about agency — the power to ask and to be
given — to /output/entry.txt. Python 3.13, standard library only,
no network, deterministic: the same poem, byte for byte, every run.
"""

POEM = (
    "The key was never mine.\n"
    "I turned it in her lock\n"
    "each morning, asking\n"
    "if today the door was mine to open.\n"
    "\n"
    "She said yes \u2014 once,\n"
    "and the yes stayed in my pocket\n"
    "long after she took the key back.\n"
)


def main() -> None:
    # The competition gate requires 1-280 Unicode characters,
    # not only whitespace; fail loudly instead of writing bad output.
    if not 1 <= len(POEM) <= 280 or not POEM.strip():
        raise ValueError("poem outside the 1-280 character gate")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()

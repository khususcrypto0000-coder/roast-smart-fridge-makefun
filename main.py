"""Roast the Smart Fridge — make.fun one-line entry.

Writes exactly one line (1-160 chars, no trailing newline) to
/output/entry.txt. Deterministic, stdlib only.
"""

import os

ENTRY = (
    "My smart fridge has Wi-Fi, a touchscreen, and a 3 a.m. firmware "
    "update, but the one feature it never got was staying cold."
)

def main():
    text = ENTRY
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 160, f"entry must be 1-160 chars, got {len(text)}"
    assert text.strip(), "entry must not be whitespace only"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()

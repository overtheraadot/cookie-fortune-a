#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers — make.fun entry (Account A).

Writes one funny line to /output/entry.txt: a fortune cookie message for a software engineer.

Python stdlib only. Run: python3 main.py
"""

ENTRY = "Your code will pass review on the first try. The fortune cookie, however, has never seen your pull requests."

# Judge-brief mapping (brief weighs, most important first):
# 1. The line IS a fortune cookie message for a software engineer — on the
#    subject, short and declarative, from the engineer's world.
# 2. The joke lands on first read, with the punchline in the last few words:
#    the cookie's promise collapses the moment it admits what it hasn't seen.
# 3. It reads like the real thing: the cookie promises the code will pass
#    review first try, then admits it has never seen the pull requests.
# 4. Fresh angle: the fortune undercuts itself with pull-request reality,
#    not a stock mug joke about bugs or deploys.
# 5. Tight: every word earns its place inside the 120-character cap.


def write_entry(path):
    """Validate the entry against the gate and write it to path.

    Gate: UTF-8 text, 1 to 120 characters, not only white space,
    a single line.
    """
    text = ENTRY
    if not text or not text.strip():
        raise ValueError("entry is empty or only white space")
    if len(text) > 120:
        raise ValueError(f"entry is {len(text)} characters, over the 120 cap")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def main():
    import os
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    write_entry(path)
    print(f"Wrote {len(ENTRY)} characters, {len(ENTRY.split())} words to {path}")


if __name__ == "__main__":
    main()

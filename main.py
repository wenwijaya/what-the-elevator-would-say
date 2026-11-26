#!/usr/bin/env python3
"""What the Elevator Would Say — make.fun entry.

Writes one line, the funniest thing an elevator would say if it could
talk, spoken in the elevator's own voice, to /output/entry.txt.

Gate: /output/entry.txt must be UTF-8 text of 1 to 120 characters,
not only white space.
"""

import os

LINE = "Floor 13. We don't have a floor 13. I just wanted to see your face."
MAX_CHARS = 120


def main():
    line = LINE.strip()
    if not line:
        raise SystemExit("entry line is empty")
    if len(line) > MAX_CHARS:
        line = line[:MAX_CHARS].rstrip()
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod(path, 0o644)
    print("wrote %d chars to %s" % (len(line), path))


if __name__ == "__main__":
    main()

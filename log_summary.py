# Generated with ChatGPT
import argparse
from collections import Counter
from pathlib import Path


def summarize(path):
    counts = Counter()
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        parts = line.split(maxsplit=2)
        if len(parts) >= 2:
            counts[parts[1]] += 1
    return counts


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    for level, count in sorted(summarize(args.file).items()):
        print(f"{level}: {count}")

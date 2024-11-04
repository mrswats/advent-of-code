import argparse
import string
from collections.abc import Sequence


def parse_input(filename: str) -> list[str]:
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args(argv)
    raw_input = parse_input(args.filename)

    processed = []
    inner = []

    for index, line in enumerate(raw_input, start=1):
        inner.append(line)
        if index % 3 == 0:
            processed.append(inner)
            inner = []

    total_priority = 0

    for ruckstack in processed:
        bag1, bag2, bag3 = ruckstack
        common_item = set(bag1) & set(bag2) & set(bag3)
        total_priority += string.ascii_letters.find(common_item.pop()) + 1

    print(total_priority)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

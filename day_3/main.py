import argparse
import string
from typing import Sequence


def parse_input(filename: str) -> list[str]:
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args(argv)
    raw_input = parse_input(args.filename)

    total_priority = 0

    for ruckstack in raw_input:
        total_items = int(len(ruckstack) / 2)
        first_compartment, second_compartment = (
            set(ruckstack[:total_items]),
            set(ruckstack[total_items:]),
        )

        common_item = first_compartment & second_compartment
        total_priority += string.ascii_letters.find(common_item.pop()) + 1

    print(total_priority)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

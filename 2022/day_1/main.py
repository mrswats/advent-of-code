import argparse
import heapq
from typing import Sequence


def parse_input(filename: str) -> list[list[int]]:
    with open(filename) as f:
        return [
            [int(snack) for snack in elf.split("\n")]
            for elf in f.read().strip().split("\n\n")
        ]


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args(argv)
    raw_input = parse_input(args.filename)
    print(sum(heapq.nlargest(3, (sum(elf) for elf in raw_input))))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

import argparse
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

    top_three: list[int] = []

    for elf in raw_input:
        calories_per_elf = sum(elf)
        current_min = min(top_three) if top_three else 0

        if calories_per_elf > current_min:
            if current_min in top_three and len(top_three) == 3:
                top_three.remove(current_min)
            top_three.append(calories_per_elf)

    print(sum(top_three))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

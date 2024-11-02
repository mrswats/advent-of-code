from __future__ import annotations

import argparse
from typing import Any, Sequence

from itertools import permutations
from functools import reduce

INPUT = "input.txt"
TEST_INPUT = """\
2x3x4
1x1x10
"""


def solve_part1(parsed_data: list[tuple[int, int, int]]) -> int:
    total = 0
    for gift in parsed_data:
        for pair in permutations(gift, r=2):
            total += reduce(lambda a, b: a * b, pair)

        total += gift[0] * gift[1]

    return total


def solve_part2(parsed_data: list[tuple[int, int, int]]) -> int:
    total = 0
    for gift in parsed_data:
        total += 2 * (gift[0] + gift[1]) + reduce(lambda a, b: a * b, gift)

    return total


def parse_input(raw_input: str) -> Any:
    return [
        tuple(sorted(map(int, line.split("x")))) for line in raw_input.split("\n")[:-1]
    ]


def read_input_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--part2", action=argparse.BooleanOptionalAction, default=False)
    args = parser.parse_args(argv)
    raw_input = TEST_INPUT if args.test else read_input_file(INPUT)
    parsed_input = parse_input(raw_input)
    print(solve_part2(parsed_input) if args.part2 else solve_part1(parsed_input))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

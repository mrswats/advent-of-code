import argparse
import re
from typing import Sequence

INPUT = "input.txt"
TEST_INPUT = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

REGEX_PARSE = r"(\d+)-(\d+),(\d+)-(\d+)"


def solve(raw_input: str) -> str | int:
    all_pairs = [
        list(map(int, re.findall(REGEX_PARSE, line).pop()))
        for line in raw_input.splitlines()
    ]

    fully_contained = 0

    for pair in all_pairs:
        if pair[1] - pair[0] < pair[3] - pair[2]:
            first_set = set(range(pair[0], pair[1] + 1))
            second_set = set(range(pair[2], pair[3] + 1))
        else:
            second_set = set(range(pair[0], pair[1] + 1))
            first_set = set(range(pair[2], pair[3] + 1))

        if first_set & second_set:
            fully_contained += 1

    return fully_contained


def parse_input(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action=argparse.BooleanOptionalAction, default=True)
    args = parser.parse_args(argv)
    raw_input = TEST_INPUT if args.test else parse_input(INPUT)
    print(solve(raw_input))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

from __future__ import annotations

import argparse
import re
from collections.abc import Sequence
from typing import Any

INPUT = "input.txt"

# Test input part 1
TEST_INPUT = """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

TEST_INPUT = """\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

NUMBERS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}

everything = [*NUMBERS.keys(), *map(str, NUMBERS.values())]
reversed_everython = [
    *["".join(reversed(num)) for num in NUMBERS.keys()],
    *map(str, NUMBERS.values()),
]
NUMBER_PATTERN = re.compile(rf"({'|'.join(everything)})")
REVERSED_NUMBER_PATTERN = re.compile(rf"({'|'.join(reversed_everython)})")


def solve_part1(parsed_data: str) -> str | int:
    total = 0
    for line in parsed_data:
        for first_number in line:
            if first_number.isdigit():
                break

        for last_number in line[::-1]:
            if last_number.isdigit():
                break

        linenumber = int(first_number + last_number)
        total += linenumber

    return total


def solve_part2(parsed_data: str) -> str | int:
    total = 0
    for line in parsed_data:
        first_number = NUMBER_PATTERN.search(line).group(0)
        last_number = REVERSED_NUMBER_PATTERN.search(line[::-1]).group(0)[::-1]

        linenumber = int(f"{NUMBERS[first_number]}{NUMBERS[last_number]}")
        total += linenumber

    return total


def parse_input(raw_input: str) -> Any:
    return [line for line in raw_input.split("\n") if line]


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

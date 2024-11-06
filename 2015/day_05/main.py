from __future__ import annotations

import argparse
from collections import Counter
from collections.abc import Sequence
from typing import Any

INPUT = "input.txt"
TEST_INPUT = """\
ugknbfddgicrmopn
aaa
haegwjzuvuyypxyu
dvszwmarrgswjxmb
"""


def solve_part1(parsed_data: str) -> str | int:
    number_of_nice_strings = 0
    for line in parsed_data.split("\n"):
        counter = Counter(line)
        nice = 0

        if sum(counter.get(letter, 0) for letter in "aeiou") >= 3:
            nice += 1

        if any(a == b for a, b in zip(line, line[1:])):
            nice += 1

        if all(symb not in line for symb in ["ab", "cd", "pq", "xy"]):
            nice += 1

        if nice == 3:
            number_of_nice_strings += 1

    return number_of_nice_strings


def solve_part2(parsed_data: str) -> str | int:
    return len(parsed_data)


def parse_input(raw_input: str) -> Any:
    return raw_input


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

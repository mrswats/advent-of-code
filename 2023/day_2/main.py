from __future__ import annotations

import argparse
import re
from typing import Any
from typing import Sequence

INPUT = "input.txt"
TEST_INPUT = """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

PARSE_RE = re.compile(r"(Game \d+): (\d+\w+)+?")


def solve_part1(parsed_data: str) -> str | int:
    return len(parsed_data)


def solve_part2(parsed_data: str) -> str | int:
    return len(parsed_data)


def parse_input(raw_input: str) -> Any:
    for line in raw_input.split("\n"):
        print(PARSE_RE.findall(line))

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

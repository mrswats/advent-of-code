import argparse
import re
from collections import defaultdict
from typing import Sequence

CRATES_REGEX = re.compile(r"\w")
MOVEMENTS_REGEX = re.compile(r"move (\d+) from (\d+) to (\d+)")

INPUT = "input.txt"
TEST_INPUT = "test_input.txt"


def solve(raw_input: str) -> str | int:
    raw_crates, raw_movement = raw_input.split("\n\n")
    number_list = raw_crates.splitlines()[-1]
    crates = defaultdict(list)
    for line in raw_crates.splitlines()[:-1]:
        for match in CRATES_REGEX.finditer(line):
            column = number_list[match.start()]
            crates[int(column)].append(match.group())

    movements = [
        tuple(map(int, MOVEMENTS_REGEX.findall(line).pop()))
        for line in raw_movement.splitlines()
    ]

    for number_of_crates_to_move, origin_stack, destination_stack in movements:
        for _ in range(number_of_crates_to_move):
            crate_being_moved = crates[origin_stack].pop(0)
            crates[destination_stack] = [crate_being_moved] + crates[destination_stack]

    return "".join(crates[stack + 1][0] for stack in range(len(crates)))


def parse_input(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action=argparse.BooleanOptionalAction, default=True)
    args = parser.parse_args(argv)
    raw_input = parse_input(TEST_INPUT if args.test else INPUT)
    print(solve(raw_input))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

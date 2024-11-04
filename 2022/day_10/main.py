from __future__ import annotations

import argparse
from collections.abc import Sequence
from typing import Any

INPUT = "input.txt"
TEST_INPUT = """\
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""

NOOP = "noop"
ADDX = "addx"

SCREEEN_WIDTH = 40


def solve(parsed_data: str) -> str | int:
    registry_x = 1
    cycle = 1

    addx_cycle = True

    print()
    print("  ", end="")

    while True:
        if addx_cycle:
            instruction = parsed_data.pop(0)

        op = instruction[0]

        print(
            "#" if registry_x <= cycle % SCREEEN_WIDTH <= registry_x + 2 else ".",
            end="",
        )

        if op == NOOP:
            pass
        elif op == ADDX and addx_cycle:
            addx_cycle = False
        elif op == ADDX and not addx_cycle:
            addx_cycle = True
            registry_x += int(instruction[1])
        else:
            raise AssertionError("Unkwown instruction")

        if cycle % SCREEEN_WIDTH == 0:
            print()
            print("  ", end="")

        cycle += 1

        if not parsed_data:
            break

    return ""


def parse_input(raw_input: str) -> Any:
    return [line.split(" ") for line in raw_input.splitlines()]


def read_input_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action=argparse.BooleanOptionalAction, default=True)
    args = parser.parse_args(argv)
    raw_input = TEST_INPUT if args.test else read_input_file(INPUT)
    print(solve(parse_input(raw_input)))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

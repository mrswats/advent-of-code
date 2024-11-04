from __future__ import annotations

import argparse
from typing import Any, Sequence
from collections import defaultdict
import operator
from itertools import chain

INPUT = "input.txt"
TEST_INPUT = """\
^>v<
"""

DIRECTIONS: dict[str, tuple[int, int]] = {
    ">": (0, 1),
    "<": (0, -1),
    "v": (-1, 0),
    "^": (1, 0),
}


def solve_part1(parsed_data: str) -> str | int:
    visited: dict[tuple[int, int], int] = defaultdict(int)

    pos = (0, 0)
    visited[pos] = 1

    for symb in parsed_data.strip("\n"):
        dir = DIRECTIONS[symb]
        pos = dir[0] + pos[0], dir[1] + pos[1]
        visited[pos] += 1

    return len(visited)


def solve_part2(parsed_data: str) -> str | int:
    visited: dict[tuple[int, int], int] = defaultdict(int)
    visitedr: dict[tuple[int, int], int] = defaultdict(int)

    santa = (0, 0)
    robot = (0, 0)
    visited[santa] = 1
    visitedr[robot] = 1

    for index, symb in enumerate(parsed_data.strip("\n")):
        dir = DIRECTIONS[symb]
        if index % 2 == 0:
            santa = dir[0] + santa[0], dir[1] + santa[1]
            visited[santa] += 1
        else:
            robot = dir[0] + robot[0], dir[1] + robot[1]
            visitedr[robot] += 1

    return len(set(chain(visited.keys(), visitedr.keys())))


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

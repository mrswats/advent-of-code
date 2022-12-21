from __future__ import annotations

import argparse
import re
from collections import defaultdict
from typing import Any, Sequence, Tuple

INPUT = "input.txt"
TEST_INPUT = """\
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""

SEGMENTS_RE = re.compile(r"(\d+),(\d+)(?: -> )?")

Point = Tuple[int, int]


def print_cave(cave: dict[Point, str]) -> None:
    min_x = min(point[0] for point in cave.keys())
    max_x = max(point[0] for point in cave.keys())
    max_y = max(point[1] for point in cave.keys())
    for row in range(max_y + 1):
        for col in range(min_x, max_x + 1):
            print(cave[(col, row)], end="")
        print()


def build_cave(parsed_data: str) -> dict[Point, str]:
    cave = defaultdict(lambda: ".")

    cave[500, 0] = "+"

    for line in parsed_data:
        for index in range(len(line) - 1):
            x0, y0, xn, yn = (*line[index], *line[index + 1])

            path = []
            if x0 == xn:
                if y0 > yn:
                    (x0, y0), (xn, yn) = (xn, yn), (x0, y0)
                path = [(x0, y0 + lindex) for lindex in range(yn - y0 + 1)]

            elif y0 == yn:
                if x0 > xn:
                    (x0, y0), (xn, yn) = (xn, yn), (x0, y0)

                path = [(x0 + lindex, y0) for lindex in range(xn - x0 + 1)]

            for xcord, ycord in path:
                cave[(xcord, ycord)] = "#"

    return cave


def solve(parsed_data: str) -> str | int:
    cave = build_cave(parsed_data)
    max_y = max(point[1] for point in cave.keys())

    sand = 0
    no_more_sand_can_fall = False
    start_pos = (500, 0)

    while not no_more_sand_can_fall:
        sand += 1

        current_pos = start_pos

        while True:
            next_down = (current_pos[0], current_pos[1] + 1)
            next_down_left = (current_pos[0] - 1, current_pos[1] + 1)
            next_down_right = (current_pos[0] + 1, current_pos[1] + 1)

            if current_pos[1] > max_y:
                cave[current_pos] = "o"
                break
            elif next_down not in cave:
                current_pos = next_down
            elif next_down_left not in cave:
                current_pos = next_down_left
            elif next_down_right not in cave:
                current_pos = next_down_right
            else:
                cave[current_pos] = "o"
                break

        if cave[start_pos] == "o":
            no_more_sand_can_fall = True
            break

    return sand


def parse_input(raw_input: str) -> Any:
    return [
        [tuple(map(int, segment.groups())) for segment in SEGMENTS_RE.finditer(line)]
        for line in raw_input.splitlines()
    ]


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

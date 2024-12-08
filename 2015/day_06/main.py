from __future__ import annotations

import argparse
import re
from collections.abc import Sequence
from typing import NamedTuple


INPUT = "input.txt"
TEST_INPUT = """\
turn on 999,0 through 0,0
"""

GRID_SIZE = 1000

TURN_RE = re.compile(r"(turn) (on|off) (\d+,\d+) through (\d+,\d+)")
TOGGLE_RE = re.compile(r"(toggle) (\d+,\d+) through (\d+,\d+)")


class Line(NamedTuple):
    action: str
    state: str = ""
    start: str = "0,0"
    stop: str = "0,0"

    def t_start(self) -> tuple[int, int]:
        return tuple(map(int, self.start.split(",")))

    def t_stop(self) -> tuple[int, int]:
        return tuple(map(int, self.stop.split(",")))


def solve_part1(parsed_data: list[Line]) -> int:
    grid = {(x, y): 0 for x in range(GRID_SIZE) for y in range(GRID_SIZE)}

    for line in parsed_data:
        if line.t_start > line.t_stop:
            x1, y1 = line.t_stop
            x2, y2 = line.t_start
        else:
            x1, y1 = line.t_start
            x2, y2 = line.t_stop

        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                if line.action == "toggle":
                    grid[(x, y)] ^= 1
                elif line.action == "turn":
                    grid[(x, y)] = 1 if line.state == "on" else 0
                else:
                    raise AssertionError("unreachable")

    return list(grid.values()).count(1)


def solve_part2(parsed_data: list[Line]) -> int:
    return len(parsed_data)


def parse_input(raw_input: str) -> list[Line]:
    def _get_line(line: str) -> Line:
        try:
            if line.startswith("turn"):
                args = TURN_RE.findall(line).pop()
            else:
                args = TOGGLE_RE.findall(line).pop()
        except Exception:
            print(line)
            raise

        return Line(*args)

    return [_get_line(line) for line in raw_input.splitlines()]


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

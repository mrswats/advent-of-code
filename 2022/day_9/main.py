from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import floor, sqrt
from typing import Sequence

INPUT = "input.txt"
TEST_INPUT = """\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""


@dataclass
class Position:
    xpos: int = 0
    ypos: int = 0

    def __add__(self, other: Position) -> Position:
        return Position(xpos=self.xpos + other.xpos, ypos=self.ypos + other.ypos)

    def __iadd__(self, other: Position) -> Position:
        return self + other

    def __hash__(self):
        return hash((self.xpos, self.ypos))

    def __repr__(self) -> str:
        return f"({self.xpos}, {self.ypos})"

    def is_diagonal(self, other: Position) -> bool:
        return self.xpos != other.xpos and self.ypos != other.ypos


directions = {
    "R": Position(1, 0),
    "L": Position(-1, 0),
    "U": Position(0, 1),
    "D": Position(0, -1),
}


def distance(p_point: Position, q_point: Position) -> int:
    return floor(
        sqrt((p_point.xpos - q_point.xpos) ** 2 + (p_point.ypos - q_point.ypos) ** 2)
    )


def movement(direction: Position, quantity: int) -> Position:
    position = Position(0, 0)
    for _ in range(quantity):
        position += direction

    return position


def parse_input(raw_input: str) -> list[tuple[str, int]]:
    return [
        (splitline[0], int(splitline[1]))
        for line in raw_input.splitlines()
        if (splitline := line.split(" "))
    ]


def solve(parsed_input: list[tuple[str, int]]) -> str | int:
    head, tail = Position(0, 0), Position(0, 0)
    tail_visits = {tail}
    last_direction = None

    for direction, quantity in parsed_input:
        for _ in range(quantity):

            if direction == "D" and quantity == 2:
                breakpoint()

            head += directions[direction]

            if distance(head, tail) > 1:
                if head.is_diagonal(tail):
                    tail += last_direction

                tail += directions[direction]
                tail_visits.add(tail)

        assert distance(head, tail) < 2, (direction, quantity)
        last_direction = directions[direction]

    return len(tail_visits)


def read_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action=argparse.BooleanOptionalAction, default=True)
    args = parser.parse_args(argv)
    raw_input = TEST_INPUT if args.test else read_file(INPUT)
    print(solve(parse_input(raw_input)))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

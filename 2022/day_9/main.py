from __future__ import annotations

import argparse
from math import sqrt
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


D = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1),
}


def dist(p: tuple[int, int], q: tuple[int, int]) -> float:
    return sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


def move(position: tuple[int, int], direction: tuple[int, int]) -> tuple[int, int]:
    return (position[0] + direction[0], position[1] + direction[1])


def solve(parsed_input: list[tuple[str, int]]) -> str | int:
    head = tail = (0, 0)
    tail_visits = {tail}

    last_direction = None

    for dir_s, quantity in parsed_input:
        direction = D[dir_s]

        for _ in range(int(quantity)):
            head = move(head, direction)

            if dist(head, tail) > 1:
                if head[0] != tail[0] and head[1] != tail[1]:
                    tail = move(tail, last_direction)

                tail = move(tail, direction)
                tail_visits.add(tail)

        last_direction = direction

    return len(tail_visits)


def parse_input(raw_input: str) -> list[tuple[str, int]]:
    return [line.split(" ") for line in raw_input.splitlines()]


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

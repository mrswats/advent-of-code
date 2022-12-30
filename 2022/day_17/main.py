from __future__ import annotations

import argparse
import collections
import copy
import itertools
from typing import Any, Sequence, Tuple

INPUT = "input.txt"
TEST_INPUT = """\
>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
"""

TOTAL_PIECES_FALLEN = 2022
WIDTH = 7

moves = {
    ">": (1, 0),
    "^": (0, 1),
    "v": (0, -1),
    "<": (-1, 0),
}

pieces = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # _
    [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)],  # +
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],  # reversed L
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # |+
    [(0, 0), (1, 0), (0, 1), (1, 1)],  # cube
]

Point = Tuple[int, int]


def highest_point_in_the_cavern(cavern: dict[Point, str]) -> int:
    return max(point[1] for point in cavern.keys())


def print_cavern(cavern: dict[Point, str]) -> None:
    highest = highest_point_in_the_cavern(cavern) + 3

    print()

    for row in reversed(range(highest)):
        for column in range(-1, WIDTH + 1):
            if column in [-1, WIDTH]:
                if row == 0:
                    print("+", end="")
                else:
                    print("|", end="")
            else:
                print(cavern[(column, row)], end="")
        print()

    print()


def generate_cavern() -> dict[Point, str]:
    cavern = collections.defaultdict(lambda: ".")

    for col in range(WIDTH):
        cavern[(col, 0)] = "-"

    return cavern


def in_bounds(piece: list[Point]) -> bool:
    return all(0 <= x < WIDTH for x, _ in piece)


def push_piece(piece: list[Point], direction: Point) -> list[Point]:
    dx, dy = direction
    new_piece_position = [(x + dx, y + dy) for x, y in piece]
    return new_piece_position if in_bounds(new_piece_position) else piece


def collision(piece, cavern) -> bool:
    return any(piecepos in cavern for piecepos in piece)


def next_movement(jet_data: list[str]) -> Point:
    for index, direction in enumerate(itertools.cycle(jet_data)):
        if index % 2 != 0:
            yield moves["v"]
        else:
            yield moves[direction]


def solve_part1(parsed_data: str) -> str | int:

    pieces_fallen = 0

    cavern = generate_cavern()
    movements = next_movement(parsed_data)

    for piece in itertools.cycle(pieces):
        pieces_fallen += 1

        current_height = highest_point_in_the_cavern(cavern)
        piece = push_piece(piece, (0, current_height + 2))

        while True:
            direction = next(movements)
            piece = push_piece(piece, direction)

            if piece == push_piece(piece, moves["v"]) or collision(piece, cavern):
                for piecepos in push_piece(piece, moves["^"]):
                    cavern[piecepos] = "#"

                break

        # print_cavern(copy.copy(cavern))

        if pieces_fallen == TOTAL_PIECES_FALLEN:
            break

    return highest_point_in_the_cavern(cavern)


def solve_part2(parsed_data: str) -> str | int:
    return len(parsed_data)


def parse_input(raw_input: str) -> Any:
    return list(raw_input.strip())


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

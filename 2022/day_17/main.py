from __future__ import annotations

import argparse
import copy
import itertools
from typing import Any, Iterable, Sequence, Tuple

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
    [(2, 0), (3, 0), (4, 0), (5, 0)],  # _
    [(3, 1), (2, 1), (4, 1), (3, 2), (3, 0)],  # +
    [(2, 0), (3, 0), (4, 0), (4, 1), (4, 2)],  # reversed L
    [(2, 0), (2, 1), (2, 2), (2, 3)],  # |+
    [(2, 0), (3, 0), (2, 1), (3, 1)],  # cube
]

Point = Tuple[int, int]


def highest_point_in_the_cavern(cavern: dict[Point, str]) -> int:
    return max(point[1] for point in cavern.keys()) + 1


def print_cavern(cavern: dict[Point, str], piece: list[Point] | None = None) -> None:
    highest = highest_point_in_the_cavern(cavern) + 5
    cavern = copy.copy(cavern)

    if piece:
        for piecepos in piece:
            cavern[piecepos] = "@"

    print()

    for row in reversed(range(-1, highest)):
        for column in range(-1, WIDTH + 1):
            if column in [-1, WIDTH]:
                if row == -1:
                    print("+", end="")
                else:
                    print("|", end="")
            elif (column, row) not in cavern:
                print(".", end="")
            else:
                print(cavern[(column, row)], end="")

        print(f"{row: 7}")

    print()


def generate_cavern() -> dict[Point, str]:
    cavern = {}

    for col in range(WIDTH):
        cavern[(col, -1)] = "-"

    return cavern


def in_bounds(piece: list[Point]) -> bool:
    return all(0 <= x < WIDTH and 0 <= y for x, y in piece)


def push_piece(piece: list[Point], direction: Point) -> list[Point]:
    dx, dy = direction
    new_piece_position = [(x + dx, y + dy) for x, y in piece]
    return new_piece_position if in_bounds(new_piece_position) else piece


def collision(piece, cavern) -> bool:
    return any(piecepos in cavern for piecepos in piece)


def solve_part1(jet_data: str) -> str | int:

    pieces_fallen = 0

    cavern = generate_cavern()
    movements = itertools.cycle(jet_data)

    for piece in itertools.cycle(pieces):
        pieces_fallen += 1

        current_height = highest_point_in_the_cavern(cavern)
        piece = push_piece(piece, (0, current_height + 3))
        index = 0

        while True:
            movement = next(movements) if index % 2 == 0 else "v"
            direction = moves[movement]
            next_piece_position = push_piece(piece, direction)
            if not collision(next_piece_position, cavern) or not in_bounds(
                next_piece_position
            ):
                piece = next_piece_position

            index += 1

            next_piece_position = push_piece(piece, moves["v"])
            if movement in ["<", ">"] and (
                next_piece_position == piece or collision(next_piece_position, cavern)
            ):
                break

        for piecepos in piece:
            cavern[piecepos] = "#"

        if pieces_fallen == TOTAL_PIECES_FALLEN:
            break

    return highest_point_in_the_cavern(cavern)


def inner_loop(
    movements: Iterable[list[Point]],
    index: int,
    piece: list[Point],
    cavern: dict[Point, str],
) -> list[Point]:
    while True:
        movement = next(movements) if index % 2 == 0 else "v"
        direction = moves[movement]
        next_piece_position = push_piece(piece, direction)
        if not collision(next_piece_position, cavern) or not in_bounds(
            next_piece_position
        ):
            piece = next_piece_position

        index += 1

        next_piece_position = push_piece(piece, moves["v"])
        if movement in ["<", ">"] and (
            next_piece_position == piece or collision(next_piece_position, cavern)
        ):
            return piece


def solve_part2(jet_data: str) -> str | int:
    pieces_fallen = 0

    cavern = generate_cavern()
    movements = itertools.cycle(jet_data)

    repeat_pieces_fallen = 0

    for piece in itertools.cycle(pieces):
        pieces_fallen += 1
        current_height = highest_point_in_the_cavern(cavern)

        if current_height == 25:
            pieces_fallen_at_25 = pieces_fallen

        if 26 <= current_height <= 48:
            repeat_pieces_fallen += 1

        piece = inner_loop(
            movements,
            0,
            push_piece(piece, (0, current_height + 3)),
            cavern,
        )

        for piecepos in piece:
            cavern[piecepos] = "#"

        if pieces_fallen == TOTAL_PIECES_FALLEN:
            break

    print_cavern(cavern)

    total_number_of_pieces = 1_000_000_000_000

    return 12 * ((total_number_of_pieces - pieces_fallen_at_25) // repeat_pieces_fallen)


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

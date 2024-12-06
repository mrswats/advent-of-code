from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

import pytest

INPUT = "input.txt"

EXPECTED_RESULT = 41
TEST_INPUT = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    @classmethod
    def get_direction_by_int(cls, direction_index: int) -> Direction:
        for dir in [cls.UP, cls.RIGHT, cls.DOWN, cls.LEFT]:
            if dir.value == direction_index:
                return dir
        else:
            raise AssertionError("unreachable")


class GuardOut(Exception):
    pass


@dataclass
class Guard:
    grid: dict[tuple[int, int], str]
    visited_positions: set[tuple[int, int]]
    position: tuple[int, int]
    direction: Direction

    def move(self) -> None:
        if self.direction == Direction.UP:
            new_position = (self.position[0] - 1, self.position[1])
        if self.direction == Direction.RIGHT:
            new_position = (self.position[0], self.position[1] + 1)
        if self.direction == Direction.DOWN:
            new_position = (self.position[0] + 1, self.position[1])
        if self.direction == Direction.LEFT:
            new_position = (self.position[0], self.position[1] - 1)

        if new_position not in self.grid:
            raise GuardOut("Guard went out the map!")

        if self.grid[new_position] == "#":
            self.direction = Direction.get_direction_by_int(
                (self.direction.value + 1) % 4
            )
        else:  # no obstacle
            self.position = new_position
            self.visited_positions.add(new_position)

        return


def print_grid(grid: dict[tuple[int, int], str]) -> None:
    for index, obj in enumerate(grid.values()):
        if index % 10 == 0:
            print()
        else:
            print(obj, end=" ")
    print()


def solution(raw_input: str) -> int:
    grid = {
        (row_index, col_index): col
        for row_index, row in enumerate(raw_input.splitlines())
        for col_index, col in enumerate(row)
    }

    for position, obj in grid.items():
        if obj == "^":
            initial_position = position
            break
    else:
        raise AssertionError("unreachable")

    guard = Guard(
        grid,
        visited_positions={initial_position},
        position=initial_position,
        direction=Direction.UP,
    )

    while True:
        try:
            guard.move()
        except GuardOut:
            break

    visited_grid = grid.copy()
    for position in guard.visited_positions:
        visited_grid[position] = "X"

    return len(guard.visited_positions)


def read_input_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def main() -> int:
    raw_input = read_input_file(INPUT)

    print(solution(raw_input))

    return 0


@pytest.mark.parametrize(
    "test_input, expected_result",
    [
        (TEST_INPUT, EXPECTED_RESULT),
    ],
)
def test_solution(test_input, expected_result):
    assert solution(test_input) == expected_result


if __name__ == "__main__":
    raise SystemExit(main())

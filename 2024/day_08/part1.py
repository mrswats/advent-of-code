from __future__ import annotations

import pytest

INPUT = "input.txt"

EXPECTED_RESULT = 14
TEST_INPUT = """\
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""


def solution(raw_input: str) -> int:
    grid = {
        (row_index, col_index): col
        for row_index, row in enumerate(raw_input.splitlines())
        for col_index, col in enumerate(row)
    }

    return len(grid)


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

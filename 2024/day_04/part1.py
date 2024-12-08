from __future__ import annotations

import pytest

INPUT = "input.txt"

EXPECTED_RESULT = 18
TEST_INPUT = """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

TARGET = "XMAS"


def solution(raw_input: str) -> int:
    total_words = 0
    height = len(raw_input.split("\n")[0])
    width = len(raw_input.splitlines())

    rows = raw_input.splitlines()
    columns = ["".join(c[row] for c in rows) for row in range(height)]

    diagonals = ["".join(rows[i][j] for i in range(width) for j in range(i, height))]

    # TODO: The idea: calculate the rows, the columns and the diagonals
    # then count them all up backwards and forwards.

    return total_words


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

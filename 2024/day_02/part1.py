from __future__ import annotations

from itertools import pairwise
from math import fabs

import pytest

INPUT = "input.txt"

EXPECTED_RESULT = 2
TEST_INPUT = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


def is_report_safe(report: list[int]) -> bool:
    direction = ""
    prev_direction = ""

    for data1, data2 in pairwise(report):
        if data1 == data2:
            return False

        direction = "inc" if data1 < data2 else "dec"

        if prev_direction != direction and prev_direction != "":
            return False

        diff = int(fabs(data1 - data2))

        if diff > 3 or diff == 0:
            return False

        prev_direction = direction

    return True


def solution(raw_input: str) -> int:
    number_of_safe_reports = 0

    for line in raw_input.splitlines():
        sequence = list(map(int, line.split()))

        if is_report_safe(sequence):
            number_of_safe_reports += 1

    return number_of_safe_reports


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

from __future__ import annotations

import re
from math import fabs

import pytest

INPUT = "input.txt"

EXPECTED_RESULT = 11
TEST_INPUT = """\
3   4
4   3
2   5
1   3
3   9
3   3
"""

LINE_RE = re.compile(r"(\d+)\s+(\d+)")


def solution(raw_input: str) -> int:
    left: list[int] = []
    right: list[int] = []

    for line in raw_input.splitlines():
        leftn, rightn = LINE_RE.findall(line).pop()
        left.append(int(leftn))
        right.append(int(rightn))

    left.sort()
    right.sort()

    total_distance = 0

    for leftn, rightn in zip(left, right):
        total_distance += int(fabs(leftn - rightn))

    return total_distance


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

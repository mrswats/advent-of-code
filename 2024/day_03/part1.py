from __future__ import annotations

import re

import pytest

INPUT = "input.txt"

EXPECTED_RESULT = 161
TEST_INPUT = """\
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""

MUL_RE = re.compile(r"(mul\((\d+),(\d+)\))")


def solution(raw_input: str) -> int:
    total_sum = 0

    for line in raw_input.splitlines():
        for raw, mul1, mul2 in MUL_RE.findall(line):
            total_sum += int(mul1) * int(mul2)

    return total_sum


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

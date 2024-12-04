from __future__ import annotations

import re

import pytest

INPUT = "input.txt"

EXPECTED_RESULT = 48
TEST_INPUT = """\
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""

MUL_RE = re.compile(r"(do\(\)|don't\(\)|mul\((\d+),(\d+)\))")

MUL_INSTRUCTION = re.compile("mul(.+)")
ENABLE_INSTRUCTION = "do()"
DISABLE_INSTRUCTION = "don't()"


def solution(raw_input: str) -> int:
    total_sum = 0
    multiplications_enabled = True

    for line in raw_input.splitlines():
        for instruction, mul1, mul2 in MUL_RE.findall(line):
            if instruction == DISABLE_INSTRUCTION:
                multiplications_enabled = False
            elif instruction == ENABLE_INSTRUCTION:
                multiplications_enabled = True
            elif MUL_INSTRUCTION.match(instruction) and multiplications_enabled is True:
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

from __future__ import annotations

import pytest

INPUT = "input.txt"

EXPECTED_RESULT = 0
TEST_INPUT = """\
"""


def solution(raw_input: str) -> int:
    for line in raw_input.splitlines():
        pass

    return len(raw_input)


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

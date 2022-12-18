from __future__ import annotations

import argparse
import json
from typing import Any, Sequence

INPUT = "input.txt"
TEST_INPUT = """\
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""


def compare(left: int | list, right: int | list) -> bool | None:
    for left_signal, right_signal in zip(left, right):
        result = None

        if isinstance(left_signal, int) and isinstance(right_signal, int):
            if left_signal == right_signal:
                continue
            else:
                return left_signal < right_signal

        elif isinstance(left_signal, list) and isinstance(right_signal, list):
            result = compare(left_signal, right_signal)

        elif isinstance(left_signal, int) and isinstance(right_signal, list):
            result = compare([left_signal], right_signal)

        elif isinstance(left_signal, list) and isinstance(right_signal, int):
            result = compare(left_signal, [right_signal])

        if isinstance(result, bool):
            return result

    if len(left) != len(right):
        return len(left) < len(right)


def solve(parsed_data: str) -> int:
    indices = [
        index for index, block in enumerate(parsed_data, start=1) if compare(*block)
    ]

    return sum(indices)


def parse_input(raw_input: str) -> Any:
    return [
        [json.loads(line) for line in block.splitlines()]
        for block in raw_input.split("\n\n")
    ]


def read_input_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action=argparse.BooleanOptionalAction, default=True)
    args = parser.parse_args(argv)
    raw_input = TEST_INPUT if args.test else read_input_file(INPUT)
    print(solve(parse_input(raw_input)))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

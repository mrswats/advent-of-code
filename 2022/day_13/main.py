from __future__ import annotations

import argparse
import json
from pprint import pprint as print
from typing import Any, Callable, Iterable, Sequence

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


Signal = int | list


def bubble_sort(
    iterable: Iterable[Any],
    key: Callable[[Signal, Signal], bool],
) -> Iterable[Any]:
    ietrable_length = len(iterable)

    while True:
        swapped = False
        for i in range(1, ietrable_length):
            if key(iterable[i - 1], iterable[i]):
                iterable[i], iterable[i - 1] = iterable[i - 1], iterable[i]
                swapped = True
        ietrable_length = ietrable_length - 1

        if not swapped:
            break

    return iterable


def compare(left: Signal, right: Signal) -> bool | None:
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
    marker_1, marker_2 = [[2]], [[6]]
    signals = [*parsed_data, marker_1, marker_2]
    sorted_signals = bubble_sort(signals, key=lambda left, right: compare(right, left))

    return (sorted_signals.index(marker_1) + 1) * (sorted_signals.index(marker_2) + 1)


def parse_input(raw_input: str) -> Any:
    return [json.loads(line) for line in raw_input.splitlines() if line]


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

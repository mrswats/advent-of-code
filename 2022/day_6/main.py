import argparse
from typing import Sequence

INPUT = "input.txt"
TEST_INPUT = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

SLIDING_WINDOW_WIDTH_PART_1 = 4
SLIDING_WINDOW_WIDTH = 14


def solve(raw_input: str) -> str | int:
    slices = len(raw_input) - SLIDING_WINDOW_WIDTH
    for idx in range(slices + 1):
        if (
            len(set(raw_input[idx : idx + SLIDING_WINDOW_WIDTH]))
            == SLIDING_WINDOW_WIDTH
        ):
            break

    return idx + SLIDING_WINDOW_WIDTH


def parse_input(filename: str) -> str:
    with open(filename) as f:
        return f.read().strip()


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action=argparse.BooleanOptionalAction, default=True)
    args = parser.parse_args(argv)
    raw_input = TEST_INPUT if args.test else parse_input(INPUT)
    print(solve(raw_input))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

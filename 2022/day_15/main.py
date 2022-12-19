from __future__ import annotations

import argparse
from typing import Any, Sequence

INPUT = "input.txt"
TEST_INPUT = """\
"""


def solve(parsed_data: str) -> str | int:
    return len(parsed_data)


def parse_input(raw_input: str) -> Any:
    return raw_input


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

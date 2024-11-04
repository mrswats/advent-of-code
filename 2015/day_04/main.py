from __future__ import annotations

import argparse
from typing import Any, Sequence
import hashlib

INPUT = "input.txt"
TEST_INPUT = """\
pqrstuv
"""


def solve_part1(parsed_data: str) -> str | int:
    ans = 100_000

    while True:
        resp = hashlib.md5(f"{parsed_data.strip('\n')}{ans}".encode())
        if resp.hexdigest().startswith("00000"):
            return ans

        ans += 1

    raise AssertionError("Unreachable")


def solve_part2(parsed_data: str) -> str | int:
    return len(parsed_data)


def parse_input(raw_input: str) -> Any:
    return raw_input


def read_input_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--part2", action=argparse.BooleanOptionalAction, default=False)
    args = parser.parse_args(argv)
    raw_input = TEST_INPUT if args.test else read_input_file(INPUT)
    parsed_input = parse_input(raw_input)
    print(solve_part2(parsed_input) if args.part2 else solve_part1(parsed_input))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

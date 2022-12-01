import argparse
from typing import Sequence

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

OPENING = "([{<"
CLOSING = ")]}>"


def parse_input(filename: str) -> list[int]:
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args(argv)
    raw_input = parse_input(args.filename)

    total_score = 0

    for line in raw_input:
        stack = []
        for char in line:
            if char in OPENING:
                stack.append(char)

            if char in CLOSING:
                if (
                    (char == ")" and stack[-1] == "(")
                    or (char == "]" and stack[-1] == "[")
                    or (char == "}" and stack[-1] == "{")
                    or (char == ">" and stack[-1] == "<")
                ):
                    stack.pop()
                else:
                    total_score += points[char]
                    break

    print(total_score)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

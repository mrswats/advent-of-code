import argparse
from typing import Sequence

points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

symbols = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


def parse_input(filename: str) -> list[int]:
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args(argv)
    raw_input = parse_input(args.filename)

    total_scores = []

    for line in raw_input:
        stack = []
        for char in line:
            if char in symbols.keys():
                stack.append(char)

            if char in symbols.values():
                if (
                    (char == ")" and stack[-1] == "(")
                    or (char == "]" and stack[-1] == "[")
                    or (char == "}" and stack[-1] == "{")
                    or (char == ">" and stack[-1] == "<")
                ):
                    stack.pop()
                else:
                    break
        else:
            completion_score = 0
            for char in reversed(stack):
                symbol_to_score = symbols[char]
                completion_score *= 5
                completion_score += points[symbol_to_score]

            total_scores.append(completion_score)

    print(sorted(total_scores)[int((len(total_scores) - 1) / 2)])

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

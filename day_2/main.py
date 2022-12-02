import argparse
from typing import Sequence

"""
A, X: Rock -> 1
B, Y: Paper -> 2
C, Z: Scissors -> 3
"""

choice = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

points = {
    ("A", "X"): 3,
    ("A", "Y"): 6,
    ("A", "Z"): 0,
    ("B", "X"): 0,
    ("B", "Y"): 3,
    ("B", "Z"): 6,
    ("C", "X"): 6,
    ("C", "Y"): 0,
    ("C", "Z"): 3,
}


def parse_input(filename: str) -> list[str]:
    with open(filename) as f:
        return [tuple(line.strip().split(" ")) for line in f.readlines()]


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args(argv)
    raw_input = parse_input(args.filename)

    total_score = sum(points[round] + choice[round[1]] for round in raw_input)

    print(total_score)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

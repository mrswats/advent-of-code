import argparse
from typing import Sequence

ONE = 2
FOUR = 4
SEVEN = 3
EIGHT = 7


"""
Segment wise:

    7 - 1: top
    5 - 1: top right
    2 - 1: bottom right
    8 - 0: middle
    5 - 4 - 7: bottom
    2 - 3: bottom left
    9 - 2 - 1: top left
"""


def parse_input(filename: str) -> list[tuple[list[str]]]:
    with open(filename) as f:
        filecontents = f.readlines()

    parsed_input = []
    append_parsed_input = parsed_input.append

    for line in filecontents:
        raw_left, raw_right = line.split(" | ")
        left = raw_left.split(" ")
        right = raw_right.strip("\n").split(" ")
        append_parsed_input((left, right))

    return parsed_input


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args(argv)
    parsed_input = parse_input(args.filename)

    for entry in parsed_input:
        numbers, output = entry
        # with the numbers I can figure out what segments correspond
        # to each letter which change for each line

        # Then, with the dictionary, I can decode the output for each line

        # Finally, transform all outputs to integer and summ them all up

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

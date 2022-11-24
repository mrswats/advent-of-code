import argparse
from collections import Counter, defaultdict
from typing import Sequence

ONE = 2
FOUR = 4
SEVEN = 3
EIGHT = 7


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

    counter = defaultdict(int)

    for entry in parsed_input:
        _, output = entry
        for display in output:
            number_of_segments = len(display)

            if number_of_segments == ONE:
                counter[1] += 1
            elif number_of_segments == FOUR:
                counter[4] += 1
            elif number_of_segments == SEVEN:
                counter[7] += 1
            elif number_of_segments == EIGHT:
                counter[8] += 1
            else:
                pass

    print(Counter(counter).total())

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

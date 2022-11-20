import argparse
from typing import Sequence


def parse_input(filename: str) -> list[int]:
    with open(filename) as f:
        filecontents = f.read()

    return list(map(int, filecontents.split(",")))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args(argv)
    parsed_input = parse_input(args.filename)

    print(parsed_input)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

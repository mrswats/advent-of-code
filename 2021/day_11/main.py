import argparse
from typing import Sequence

TOTAL_STEPS = 100
SIZE = 10


def index(row: int, col: int) -> int:
    return col + row * SIZE


def parse_input(filename: str) -> list[int]:
    with open(filename) as f:
        return list(map(int, "".join(f.read().splitlines())))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args(argv)
    octopuses = parse_input(args.filename)

    total_flashes = 0

    for _ in range(TOTAL_STEPS):
        pass

    print(total_flashes)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

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
    crab_positions = parse_input(args.filename)

    max_coord = max(crab_positions)

    min_fuel = 10000000000000000000

    for position in range(max_coord):
        fuel = 0
        for crab in crab_positions:
            fuel += abs(crab - position)

        if fuel < min_fuel:
            min_fuel = fuel

    print(f"The calculated minimm amount of fuel is {min_fuel}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

import argparse
from collections.abc import Sequence


def parse_input(filename: str) -> list[int]:
    with open(filename) as f:
        filecontents = f.read()

    return list(map(int, filecontents.split(",")))


def triangle(n: int) -> int:
    return 0.5 * n * (n + 1)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args(argv)
    crab_positions = parse_input(args.filename)

    min_fuel = min(
        int(sum(triangle(abs(crab - position)) for crab in crab_positions))
        for position in range(max(crab_positions))
    )

    print(f"The calculated minimm amount of fuel is {min_fuel}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

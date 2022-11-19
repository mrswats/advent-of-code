import argparse
from typing import Sequence

TOTAL_DAYS = 80


def total_fish(population: list[int]) -> int:
    return len(population)


def pass_a_day(population: list[int]) -> list[int]:
    new_population = [fish - 1 for fish in population]
    new_fish = new_population.count(-1)
    new_population = [fish if fish >= 0 else 6 for fish in new_population]

    return new_population + [8] * new_fish


def parse_input(filename: str) -> list[int]:
    with open(filename) as f:
        filecontents = f.read()

    return list(map(int, filecontents.split(",")))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args(argv)
    population = parse_input(args.filename)

    for _ in range(TOTAL_DAYS):
        population = pass_a_day(population)

    print(f"Total fish after {TOTAL_DAYS} days: {total_fish(population)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

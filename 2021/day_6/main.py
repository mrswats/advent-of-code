import argparse
from collections import Counter
from collections.abc import Sequence

TOTAL_DAYS = 256


def total_fish(population: Counter[int, int]) -> int:
    return population.total()


def pass_a_day(population: Counter[int, int]) -> Counter[int, int]:
    new_population = {
        0: population[1],
        1: population[2],
        2: population[3],
        3: population[4],
        4: population[5],
        5: population[6],
        6: population[7] + population[0],
        7: population[8],
        8: population[0],
    }

    return Counter(new_population)


def parse_input(filename: str) -> Counter[int, int]:
    with open(filename) as f:
        filecontents = f.read()

    return Counter(map(int, filecontents.split(",")))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args(argv)
    population = parse_input(args.filename)

    for days_passed in range(TOTAL_DAYS):
        population = pass_a_day(population)

    print(f"Total fish after {days_passed+1} days: {total_fish(population)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

import argparse
from collections.abc import Sequence

TOTAL_STEPS = 100
SIZE = 9
TOP_EDGE = 0
BOTTOM_EDGE = SIZE
LEFT_EDGE = 0
RIGHT_EDGE = SIZE


def print_octopuses(octopuses) -> None:
    for idx, energy in enumerate(octopuses):
        print(energy, end=" ")
        if (idx + 1) % SIZE == 0:
            print()
    print()


def increase_energy(octopuses: list[int]) -> list[int]:
    return [energy + 1 for energy in octopuses]


def solve(octopuses: list[int]) -> int:
    total_flashes = 0

    for _ in range(TOTAL_STEPS):
        octopuses = increase_energy(octopuses)
        while any(octopus > 9 for octopus in octopuses):
            for row_idx in range(SIZE):
                for col_idx in range(SIZE):
                    if octopuses[index(row_idx, col_idx)] > 9:
                        for neighbour in neighbours(row_idx, col_idx):
                            octopuses[index(*neighbour)] += 1

        total_flashes += sum(octopus for octopus in octopuses if octopus > 9)
        octopuses = [0 if octopus > 9 else octopus for octopus in octopuses]
        if _ == 2:
            break

    return total_flashes


def neighbours(row_idx: int, col_idx: int) -> set[int]:
    if row_idx == TOP_EDGE and col_idx == LEFT_EDGE:
        return {
            (row_idx, col_idx + 1),
            (row_idx + 1, col_idx),
            (row_idx + 1, col_idx + 1),
        }
    elif row_idx == TOP_EDGE and col_idx == RIGHT_EDGE:
        return {
            (row_idx, col_idx - 1),
            (row_idx + 1, col_idx),
            (row_idx + 1, col_idx - 1),
        }
    elif row_idx == BOTTOM_EDGE and col_idx == LEFT_EDGE:
        return {
            (row_idx, col_idx + 1),
            (row_idx - 1, col_idx),
            (row_idx - 1, col_idx + 1),
        }
    elif row_idx == BOTTOM_EDGE and col_idx == RIGHT_EDGE:
        return {
            (row_idx, col_idx - 1),
            (row_idx - 1, col_idx),
            (row_idx - 1, col_idx - 1),
        }
    elif col_idx == LEFT_EDGE:
        return {
            (row_idx, col_idx + 1),
            (row_idx + 1, col_idx),
            (row_idx - 1, col_idx),
            (row_idx - 1, col_idx + 1),
            (row_idx + 1, col_idx + 1),
        }
    elif col_idx == RIGHT_EDGE:
        return {
            (row_idx, col_idx - 1),
            (row_idx + 1, col_idx),
            (row_idx - 1, col_idx),
            (row_idx + 1, col_idx - 1),
            (row_idx - 1, col_idx - 1),
        }
    elif row_idx == TOP_EDGE:
        return {
            (row_idx, col_idx - 1),
            (row_idx, col_idx + 1),
            (row_idx + 1, col_idx),
            (row_idx + 1, col_idx + 1),
            (row_idx + 1, col_idx - 1),
        }
    elif row_idx == BOTTOM_EDGE:
        return {
            (row_idx, col_idx - 1),
            (row_idx, col_idx + 1),
            (row_idx - 1, col_idx),
            (row_idx - 1, col_idx - 1),
            (row_idx - 1, col_idx + 1),
        }
    else:
        return {
            (row_idx, col_idx - 1),
            (row_idx, col_idx + 1),
            (row_idx - 1, col_idx),
            (row_idx + 1, col_idx),
            (row_idx - 1, col_idx - 1),
            (row_idx + 1, col_idx + 1),
            (row_idx - 1, col_idx + 1),
            (row_idx + 1, col_idx - 1),
        }


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

    print(solve(octopuses))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

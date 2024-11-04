import argparse
import re
from collections.abc import Sequence
from dataclasses import dataclass

LINE_REGEX = r"(\d+),(\d+) -> (\d+),(\d+)"

ROWS = 10
COLS = 10


@dataclass
class Vent:
    x1: int
    y1: int
    x2: int
    y2: int

    @property
    def is_diagonal(self) -> bool:
        return not (self.x1 == self.x2 or self.y1 == self.y2)

    @property
    def is_horizontal(self) -> bool:
        return self.y1 == self.y2

    @property
    def is_vertical(self) -> bool:
        return self.x1 == self.x2

    def vect(self):
        v1 = self.x1, self.y1
        v2 = self.x2, self.y2

        if self.is_horizontal:
            return (v1, v2) if self.x1 < self.x2 else (v2, v1)

        if self.is_vertical:
            return (v1, v2) if self.y1 < self.y2 else (v2, v1)

        if self.is_diagonal:
            return (
                (v1, v2)
                if (
                    ((self.x1 < self.x2) and (self.y1 < self.y2))
                    or ((self.x1 > self.x2) and (self.y1 < self.y2))
                )
                else (v2, v1)
            )

    def __repr__(self) -> str:
        return f"Vent(({self.x1},{self.y1}) -> ({self.x2},{self.y2}))"


def calculate_size(vents: list[Vent]) -> tuple[int, int]:
    max_x = max([vent.x1 for vent in vents] + [vent.x2 for vent in vents])
    max_y = max([vent.y1 for vent in vents] + [vent.y2 for vent in vents])

    return max_x + 1, max_y + 1


def populate_diagram(
    vents: list[Vent], rows: int, cols: int
) -> dict[tuple[int, int], int]:
    empty_diagram = {(j, i): 0 for i in range(rows) for j in range(cols)}

    for vent in vents:
        start, end = vent.vect()

        if vent.is_horizontal:
            x = start[0]
            while x <= end[0]:
                empty_diagram[(x, start[1])] += 1
                x += 1

        if vent.is_vertical:
            y = start[1]
            while y <= end[1]:
                empty_diagram[(start[0], y)] += 1
                y += 1

        if vent.is_diagonal:
            x, y = start

            if x < end[0] and y < end[1]:
                while x <= end[0] and y <= end[1]:
                    empty_diagram[(x, y)] += 1
                    x += 1
                    y += 1

            if x > end[0] and y < end[1]:
                while x >= end[0] and y <= end[1]:
                    empty_diagram[(x, y)] += 1
                    x -= 1
                    y += 1

    return empty_diagram


def print_diagram(diagram: dict[tuple[int, int], int], nrow=ROWS, mcol=COLS) -> None:
    for rowidx in range(nrow):
        for colidx in range(mcol):
            value = diagram[(colidx, rowidx)]
            if value:
                print(value, end=" ")
            else:
                print(".", end=" ")
        print()


def count_overlaps(diagram: dict[tuple[int, int], int]) -> int:
    return sum(1 for val in diagram.values() if val > 1)


def parse_input(filename: str) -> list[Vent]:
    with open(filename) as f:
        lines = f.readlines()

    return [
        Vent(*[int(coord) for coord in re.findall(LINE_REGEX, line).pop()])
        for line in lines
    ]


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args(argv)

    vents = parse_input(args.filename)
    rows, cols = calculate_size(vents)
    diagram = populate_diagram(vents, rows, cols)

    print_diagram(diagram, rows, cols)

    print(f"Overlaps: {count_overlaps(diagram)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass, field
from typing import Sequence, Tuple

INPUT = "input.txt"
TEST_INPUT = """\
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""

SENSOR_LOCATION_RE = re.compile(
    r"Sensor at x=([-\d]+), y=([-\d]+): closest beacon is at x=([-\d]+), y=([-\d]+)"
)


@dataclass
class Beacon:
    xpos: int
    ypos: int

    def mdist(self, otherx: int, othery: int) -> int:
        return abs(self.xpos - otherx) + abs(self.ypos - othery)


@dataclass
class Sensor(Beacon):
    closest: Beacon
    radius: int = field(init=False)

    def __post_init__(self) -> None:
        self.radius = abs(self.xpos - self.closest.xpos) + abs(
            self.ypos - self.closest.ypos
        )


Grid = dict[Tuple[int, int], Beacon | Sensor]


def solve(grid: Grid, yval: int) -> int:

    count = 0

    y = yval

    sensors = [sensor for sensor in grid.values() if isinstance(sensor, Sensor)]

    xmax = max(sensor.xpos + sensor.radius for sensor in sensors)
    xmin = min(sensor.xpos - sensor.radius for sensor in sensors)

    for x in range(xmin, xmax + 1):

        if (x, y) in grid:
            continue

        for sensor in sensors:
            if sensor.mdist(x, y) <= sensor.radius:
                count += 1
                break

    return count


def parse_input(raw_input: str) -> Grid:
    grid = {}
    for line in raw_input.splitlines():
        x, y, *closest = tuple(map(int, SENSOR_LOCATION_RE.findall(line).pop()))
        beacon = Beacon(*closest)
        grid[x, y] = Sensor(x, y, beacon)
        grid[tuple(closest)] = beacon

    return grid


def read_input_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action=argparse.BooleanOptionalAction, default=True)
    args = parser.parse_args(argv)
    raw_input = TEST_INPUT if args.test else read_input_file(INPUT)
    yval = 10 if args.test else 2000000
    print(solve(parse_input(raw_input), yval))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

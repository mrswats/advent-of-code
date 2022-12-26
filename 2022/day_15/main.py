from __future__ import annotations

import argparse
import re
from dataclasses import dataclass, field
from typing import Dict, Sequence, Tuple

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
        self.radius = self.mdist(self.closest.xpos, self.closest.ypos)


Point = Tuple[int, int]
Grid = Dict[Point, Beacon | Sensor]


def neighbours(x: int, y: int) -> Tuple[Point, ...]:
    return (
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    )


def tuning_freq(xpos: int, ypos: int) -> int:
    return xpos * 4000000 + ypos


def solve(grid: Grid, max_coord: int) -> int:
    sensors = [sensor for sensor in grid.values() if isinstance(sensor, Sensor)]
    beacons = [beacon for beacon in grid.values() if isinstance(beacon, Beacon)]

    xmin = ymin = 0
    xmax = max(sensor.xpos for sensor in sensors)
    ymax = max(sensor.ypos for sensor in sensors)

    def in_bounds(xpos: int, ypos: int) -> bool:
        return (xmin < xpos < xmax) and (ymin < ypos < ymax)

    print(f"Bounds {xmin, xmax}, {ymin, ymax}")

    candidate = None
    seen = set()

    for beacon in beacons:
        todo = [(beacon.xpos, beacon.ypos)]

        print(f"Checking around sensor: {beacon}")

        while todo:
            current = todo.pop(0)

            if current in seen or not in_bounds(*current):
                continue
            else:
                seen.add(current)

            todo.extend(
                [
                    next
                    for next in neighbours(*current)
                    if next not in seen or in_bounds(*next)
                ]
            )

            if all(
                sensor.radius < sensor.mdist(*current) for sensor in sensors
            ) and in_bounds(*current):
                print(f"possible candidate 👀: {current}")
                candidate = current
                break

        if candidate:
            break

    return tuning_freq(*candidate) if candidate else 0


def parse_input(raw_input: str) -> Grid:
    grid: Grid = {}

    for line in raw_input.splitlines():
        x, y, *closest = tuple(map(int, SENSOR_LOCATION_RE.findall(line).pop()))
        beacon = Beacon(*closest)
        grid[x, y] = Sensor(x, y, beacon)
        grid[beacon.xpos, beacon.ypos] = beacon

    return grid


def read_input_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action=argparse.BooleanOptionalAction, default=True)
    args = parser.parse_args(argv)
    raw_input = TEST_INPUT if args.test else read_input_file(INPUT)
    max_coord = 20 if args.test else 4000000
    print(solve(parse_input(raw_input), max_coord))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

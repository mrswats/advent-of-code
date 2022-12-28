from __future__ import annotations

import argparse
import re
from typing import Dict, List, NamedTuple, Sequence, Tuple

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


class Sensor(NamedTuple):
    xpos: int
    ypos: int
    x_beacon: int
    y_beacon: int

    @property
    def radius(self):
        return self.mdist(self.x_beacon, self.y_beacon)

    def mdist(self, otherx: int, othery: int) -> int:
        return abs(self.xpos - otherx) + abs(self.ypos - othery)


Point = Tuple[int, int]
Grid = List[Sensor]


def neighbours(xpos: int, ypos: int) -> Tuple[Point, ...]:
    return (
        (xpos + 1, ypos),
        (xpos - 1, ypos),
        (xpos, ypos + 1),
        (xpos, ypos - 1),
    )


def tuning_freq(xpos: int, ypos: int) -> int:
    return xpos * 4_000_000 + ypos


def solve(sensors: Grid, max_coord: int) -> int:
    xmin = ymin = 0
    xmax = ymax = max_coord

    def in_bounds(xpos: int, ypos: int) -> bool:
        return (xmin < xpos < xmax) and (ymin < ypos < ymax)

    ac, bc = set(), set()

    for sensor in sensors:
        x, y, *_ = sensor
        ac.add(y - x + sensor.radius + 1)
        ac.add(y - x + sensor.radius - 1)
        bc.add(y + x + sensor.radius + 1)
        bc.add(y + x + sensor.radius - 1)

    for a in ac:
        for b in bc:
            p = (b - a) // 2, (a + b) // 2
            if in_bounds(*p) and all(
                sensor.mdist(*p) > sensor.radius for sensor in sensors
            ):
                return tuning_freq(*p)

    raise AssertionError("unreachable?")


def parse_input(raw_input: str) -> Grid:
    return [
        Sensor(*tuple(map(int, SENSOR_LOCATION_RE.findall(line).pop())))
        for line in raw_input.splitlines()
    ]


def read_input_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action=argparse.BooleanOptionalAction, default=True)
    args = parser.parse_args(argv)
    raw_input = TEST_INPUT if args.test else read_input_file(INPUT)
    max_coord = 20 if args.test else 4_000_000
    print(solve(parse_input(raw_input), max_coord))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

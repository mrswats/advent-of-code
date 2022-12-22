from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from typing import Any, Sequence, Tuple

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
class Sensor:
    xpos: int
    ypos: int
    closest: Tuple[int, int]

    def mdist(self, other: Sensor) -> int:
        return abs(self.xpos - other.xpos) + abs(self.ypos - other.ypos)


def solve(parsed_data: str) -> str | int:
    print(parsed_data)
    return len(parsed_data)


def parse_input(raw_input: str) -> Any:
    sensors = []
    for line in raw_input.splitlines():
        x, y, *closest = SENSOR_LOCATION_RE.findall(line).pop()
        sensors.append(Sensor(int(x), int(y), tuple(map(int, closest))))

    return sensors


def read_input_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action=argparse.BooleanOptionalAction, default=True)
    args = parser.parse_args(argv)
    raw_input = TEST_INPUT if args.test else read_input_file(INPUT)
    print(solve(parse_input(raw_input)))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

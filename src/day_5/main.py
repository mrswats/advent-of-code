import argparse
import re
from dataclasses import dataclass
from pprint import pprint as print
from typing import Any, Sequence

LINE_REGEX = r"(\d+),(\d+) -> (\d+),(\d+)"


@dataclass
class Vent:
    x1: int
    y1: int
    x2: int
    y2: int

    @property
    def is_diagonal(self) -> bool:
        return not (self.x1 == self.x2 or self.y1 == self.y2)

    def __repr__(self) -> str:
        return f"Vent(({self.x1},{self.y1}) -> ({self.x2},{self.y2}))"


def parse_input(filename: str) -> Any:
    with open(filename) as f:
        lines = f.readlines()

    return [Vent(*re.findall(LINE_REGEX, line)[0]) for line in lines]


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args(argv)

    vents = parse_input(args.filename)

    print(vents)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

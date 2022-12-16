from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from typing import Any, Optional, Sequence

INPUT = "input.txt"
TEST_INPUT = """\
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
"""


PARSE_VALVE_RE = re.compile(
    r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.+)$"
)


@dataclass
class Valve:
    label: str
    flow_rae: int
    neighbours: tuple[str]


def find_by_id(valves: list[Valve], label: str) -> Optional[Valve]:
    for valve in valves:
        if valve.label == label:
            return valve

    return


def solve(valves: str) -> str | int:
    print(valves)
    return ""


def parse_input(raw_input: str) -> Any:
    valves = []

    for line in raw_input.splitlines():
        label, flow_rate, neighbours = PARSE_VALVE_RE.findall(line).pop()
        valves.append(Valve(label, int(flow_rate), tuple(neighbours.split(","))))

    return valves


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

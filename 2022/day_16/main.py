from __future__ import annotations

import argparse
import re
from typing import NamedTuple, Sequence, Tuple

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


class Valve(NamedTuple):
    label: str
    flow_rate: int
    neighbours: Tuple[str]


def solve(valves: dict[str, Valve]) -> int:
    remaining_time = 30
    cost = 0

    todo = [valves["AA"]]
    open = set()

    while todo:
        current = todo.pop(0)
        remaining_time -= 1
        cost += sum(valve.flow_rate for valve in open)
        todo = []

        for adj in current.neighbours:
            todo.append(valves[adj])

        todo.sort(key=lambda valve: valve.flow_rate * remaining_time, reverse=True)

        if current.flow_rate != 0:
            open.add(current)
            remaining_time -= 1

        cost += sum(valve.flow_rate for valve in open)

        print(current)

    return cost


def parse_input(raw_input: str) -> dict[str, Valve]:
    valves = {}

    for line in raw_input.splitlines():
        label, flow_rate, neighbours = PARSE_VALVE_RE.findall(line).pop()
        valves[label] = Valve(label, int(flow_rate), tuple(neighbours.split(", ")))

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

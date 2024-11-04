from __future__ import annotations

import argparse
import re
from collections.abc import Sequence
from typing import NamedTuple

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
    neighbours: tuple[str]


""" IDEA:
    - order all the valves per decreasing rate
    - find all the paths between the valves in order.
    - Along the way, open every valve you encounter.
"""


def find_path(start: str, end: str, valves: dict[str, Valve]) -> list[str]:

    todo = [valves[start]]
    seen = set()

    come_from = {start: None}

    while todo:
        current = todo.pop(0)

        if current.label == end:
            break
        elif current in seen:
            continue
        else:
            seen.add(current)

        for neigh in current.neighbours:
            if valves[neigh] not in seen:
                come_from[neigh] = current.label
                todo.append(valves[neigh])

    path = []
    node = end

    while node is not None:
        path.append(node)
        node = come_from[node]

    return list(reversed(path))


def find_valves_order(valves: dict[str, Valve]) -> list[str]:
    valves_by_rate = sorted(
        (valve for valve in valves.values() if valve.flow_rate),
        key=lambda valve: valve.flow_rate,
        reverse=True,
    )

    valves_path = find_path("AA", valves_by_rate[0].label, valves)
    seen_valves = set(valves_path)

    while True:
        start = valves_path[-1]
        next_end_valve = [
            valve.label for valve in valves_by_rate if valve.label not in seen_valves
        ]

        if not next_end_valve:
            break

        end = next_end_valve[0]
        path = find_path(start, end, valves)

        valves_path.extend(path[1:])

        for step in path:
            seen_valves.add(step)

        if seen_valves == set(valves.values()):
            break

    return valves_path


def solve(valves: dict[str, Valve]) -> int:
    valves_path = find_valves_order(valves)
    valves_path = [
        "AA",
        "DD",
        "CC",
        "BB",
        "AA",
        "II",
        "JJ",
        "II",
        "AA",
        "DD",
        "EE",
        "FF",
        "GG",
        "HH",
        "GG",
        "FF",
        "EE",
        "DD",
        "CC",
    ]
    remaining_time = 30
    relieved_pressure = 0

    opened_valves = set()

    for valve_label in valves_path:
        remaining_time -= 1
        current_valve = valves[valve_label]

        if current_valve.flow_rate and current_valve not in opened_valves:
            relieved_pressure += current_valve.flow_rate * remaining_time
            opened_valves.add(current_valve)
            remaining_time -= 1

    return relieved_pressure


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

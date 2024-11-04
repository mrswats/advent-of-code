from __future__ import annotations

import argparse
import re
from collections.abc import Sequence
from dataclasses import dataclass
from dataclasses import field

INPUT = "input.txt"
TEST_INPUT = """\
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""

NODE_REGEX = re.compile(r"(\w+)-(\w+)")

START_LABEL = "start"
END_LABEL = "end"


@dataclass
class Node:
    label: str
    prev: Node | None = None
    neighbours: list[Node] = field(default_factory=list)


def find_node_by_label(nodes: list[Node], label: str) -> Node | None:
    for node in nodes:
        if node.label == label:
            return node

    return None


def solve(raw_input: str) -> str | int:
    nodes = []
    for line in raw_input.splitlines():
        left, right = NODE_REGEX.findall(line).pop()
        left_node = Node(label=left)
        right_node = Node(label=right)
        left_node.neighbours.append(right_node)
        right_node.neighbours.append(left_node)
        nodes.extend([left_node, right_node])

    start = find_node_by_label(nodes, START_LABEL)

    visited = []
    to_visit = []
    current_node = start
    while True:
        visited.append(current_node)
        if current_node.label == END_LABEL:
            break

        for node in current_node.neighbours:
            if node not in to_visit:
                to_visit.append(node)

        current_node = to_visit.pop(0)

    return nodes


def parse_input(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action=argparse.BooleanOptionalAction, default=True)
    args = parser.parse_args(argv)
    raw_input = TEST_INPUT if args.test else parse_input(INPUT)
    print(solve(raw_input))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

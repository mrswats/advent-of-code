from __future__ import annotations

import argparse
from collections.abc import Sequence
from dataclasses import dataclass
from math import inf

Point = tuple[int, int]

INPUT = "input.txt"
TEST_INPUT = """\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""
LOWEST_POINT = "a"

END_LABEL = "E"
START_LABEL = "S"


@dataclass
class Node:
    node_id: int
    pos_x: int
    pos_y: int
    height: int
    label: str
    dist: int = inf
    visited = False
    prev: Node | None = None

    def mdist(self, other: Node) -> int:
        return abs(self.pos_x - other.pos_x) + abs(self.pos_y - other.pos_y)

    def __hash__(self) -> int:
        return hash((self.pos_x, self.pos_y))

    def __repr__(self) -> str:
        prev = self.prev.node_id if self.prev else None
        return f"Node({self.node_id}({self.label}), pos=({self.pos_x}, {self.pos_y}), prev={prev}, dist={self.dist})"


def neighbours(row_idx: int, col_idx: int):
    return (
        (row_idx + 1, col_idx),
        (row_idx - 1, col_idx),
        (row_idx, col_idx + 1),
        (row_idx, col_idx - 1),
    )


def solve(heightmap: str) -> int:
    nodes = {}
    end = None

    def node_id(row: int, col: int) -> int:
        return row * len(heightmap.splitlines()) + col

    for rowidx, row in enumerate(heightmap.splitlines()):
        for colidx, col in enumerate(row):
            node = Node(
                node_id=node_id(rowidx, colidx),
                pos_x=colidx,
                pos_y=rowidx,
                height=ord(col),
                label=col,
            )
            nodes[(colidx, rowidx)] = node
            if col == END_LABEL:
                end = node

    end.height = ord("z") + 1
    end.dist = 0

    visited_nodes = set()
    todo = [end]

    while todo:
        current_node = todo.pop(0)

        if current_node.label == "a":
            return current_node.dist
        elif current_node in visited_nodes:
            continue
        else:
            visited_nodes.add(current_node)

        for neighbour in neighbours(current_node.pos_x, current_node.pos_y):
            if neighbour not in nodes:
                continue

            neighbour_node = nodes[neighbour]

            if (
                neighbour_node not in visited_nodes
                and neighbour_node.height - current_node.height >= -1
            ):
                neighbour_node.prev = current_node
                neighbour_node.dist = current_node.dist + 1
                todo.append(neighbour_node)

        todo.sort(key=lambda node: node.dist)


def read_input_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action=argparse.BooleanOptionalAction, default=True)
    args = parser.parse_args(argv)
    raw_input = TEST_INPUT if args.test else read_input_file(INPUT)
    print(solve(raw_input))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

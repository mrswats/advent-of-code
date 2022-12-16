from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import inf
from pprint import pprint as print
from typing import Sequence, Set

INPUT = "input.txt"
TEST_INPUT = """\
aabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""
TOP_EDGE = 0
LEFT_EDGE = 0
BOTTOM_EDGE = 4
RIGHT_EDGE = 7
END_LABEL = "E"


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

    def __repr__(self) -> str:
        return (
            f"Node({self.node_id=}, pos=({self.pos_x}, {self.pos_y}), {self.height=})"
        )


def neighbours(row_idx: int, col_idx: int) -> Set[int]:
    if row_idx == TOP_EDGE and col_idx == LEFT_EDGE:
        return {
            (row_idx, col_idx + 1),
            (row_idx + 1, col_idx),
        }
    elif row_idx == TOP_EDGE and col_idx == RIGHT_EDGE:
        return {
            (row_idx, col_idx - 1),
            (row_idx + 1, col_idx),
        }
    elif row_idx == BOTTOM_EDGE and col_idx == LEFT_EDGE:
        return {
            (row_idx, col_idx + 1),
            (row_idx - 1, col_idx),
        }
    elif row_idx == BOTTOM_EDGE and col_idx == RIGHT_EDGE:
        return {
            (row_idx, col_idx - 1),
            (row_idx - 1, col_idx),
        }
    elif col_idx == LEFT_EDGE:
        return {
            (row_idx, col_idx + 1),
            (row_idx + 1, col_idx),
            (row_idx - 1, col_idx),
        }
    elif col_idx == RIGHT_EDGE:
        return {
            (row_idx, col_idx - 1),
            (row_idx + 1, col_idx),
            (row_idx - 1, col_idx),
        }
    elif row_idx == TOP_EDGE:
        return {
            (row_idx, col_idx - 1),
            (row_idx, col_idx + 1),
            (row_idx + 1, col_idx),
        }
    elif row_idx == BOTTOM_EDGE:
        return {
            (row_idx, col_idx - 1),
            (row_idx, col_idx + 1),
            (row_idx - 1, col_idx),
        }
    else:
        return {
            (row_idx, col_idx - 1),
            (row_idx, col_idx + 1),
            (row_idx - 1, col_idx),
            (row_idx + 1, col_idx),
        }


def mdist(node_a: Node, node_b: Node) -> int:
    return abs(node_a.pos_x - node_b.pos_x) + abs(node_a.pos_y - node_b.pos_y)


def find_destination(nodes: list[Node]) -> Node:
    for node in nodes:
        if node.label == END_LABEL:
            return node


def find_by_coordinates(nodes: list[Node], x_coord: int, y_coord: int) -> Node:
    for node in nodes:
        if not node.visited and node.pos_x == x_coord and node.pos_y == y_coord:
            return node


def solve(heightmap: str) -> str | int:
    nodes = []

    def node_id(row: int, col: int) -> int:
        return row * len(heightmap.splitlines()) + col

    for rowidx, row in enumerate(heightmap.splitlines()):
        for colidx, col in enumerate(row):
            nodes.append(
                Node(
                    node_id=node_id(rowidx, colidx),
                    pos_x=colidx,
                    pos_y=rowidx,
                    height=ord(col),
                    label=col,
                )
            )

    end_node = find_destination(nodes)
    start_node = nodes[0]
    start_node.visited = True
    assert start_node.node_id == 0, start_node.node_id

    neighbour_nodes = [start_node]

    while neighbour_nodes:
        current_node = neighbour_nodes.pop(0)

        print(current_node)

        if current_node == end_node:
            break

        for neighbour in neighbours(current_node.pos_x, current_node.pos_y):
            neighbour_node = find_by_coordinates(nodes, *neighbour)
            if (
                neighbour_node is not None
                and not neighbour_node.visited
                and 0 <= current_node.height - neighbour_node.height <= 1
            ):
                neighbour_node.visited = True
                neighbour_node.dist = mdist(neighbour_node, end_node)
                neighbour_node.prev = current_node
                neighbour_nodes.append(neighbour_node)

    return nodes


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

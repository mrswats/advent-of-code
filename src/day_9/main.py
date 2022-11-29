import argparse
from dataclasses import dataclass
from typing import Sequence, Set

WIDTH = 100
HEIGHT = 100

LEFT_EDGE = 0
RIGHT_EDGE = 99
TOP_EDGE = 0
BOTTOM_EDGE = 99

# test input
# WIDTH = 10
# HEIGHT = 5
# RIGHT_EDGE = 9
# BOTTOM_EDGE = 4


def parse_input(filename: str) -> list[int]:
    with open(filename) as f:
        filecontents = f.read()

    return [int(num) for num in filecontents.replace("\n", "")]


def index(row: int, col: int) -> int:
    return col + row * WIDTH


def neighbours(row_idx: int, col_idx: int) -> Set[int]:
    if row_idx == TOP_EDGE and col_idx == LEFT_EDGE:
        return {
            index(row_idx, col_idx + 1),
            index(row_idx + 1, col_idx),
        }
    elif row_idx == TOP_EDGE and col_idx == RIGHT_EDGE:
        return {
            index(row_idx, col_idx - 1),
            index(row_idx + 1, col_idx),
        }
    elif row_idx == BOTTOM_EDGE and col_idx == LEFT_EDGE:
        return {
            index(row_idx, col_idx + 1),
            index(row_idx - 1, col_idx),
        }
    elif row_idx == BOTTOM_EDGE and col_idx == RIGHT_EDGE:
        return {
            index(row_idx, col_idx - 1),
            index(row_idx - 1, col_idx),
        }
    elif col_idx == LEFT_EDGE:
        return {
            index(row_idx, col_idx + 1),
            index(row_idx + 1, col_idx),
            index(row_idx - 1, col_idx),
        }
    elif col_idx == RIGHT_EDGE:
        return {
            index(row_idx, col_idx - 1),
            index(row_idx + 1, col_idx),
            index(row_idx - 1, col_idx),
        }
    elif row_idx == TOP_EDGE:
        return {
            index(row_idx, col_idx - 1),
            index(row_idx, col_idx + 1),
            index(row_idx + 1, col_idx),
        }
    elif row_idx == BOTTOM_EDGE:
        return {
            index(row_idx, col_idx - 1),
            index(row_idx, col_idx + 1),
            index(row_idx - 1, col_idx),
        }
    else:
        return {
            index(row_idx, col_idx - 1),
            index(row_idx, col_idx + 1),
            index(row_idx - 1, col_idx),
            index(row_idx + 1, col_idx),
        }


def is_minima(height: int, *height_adjacent_edges: int) -> bool:
    return all(height < adjacent for adjacent in height_adjacent_edges)


def find_minimal_heights(heatmap: list[int]) -> list[int]:
    return [
        index(row_idx, col_idx)
        for row_idx in range(HEIGHT)
        for col_idx in range(WIDTH)
        if is_minima(
            heatmap[index(row_idx, col_idx)],
            *(heatmap[idx] for idx in neighbours(row_idx, col_idx)),
        )
    ]


def search(heatmap: list[int]):
    starting_nodes = find_minimal_heights(heatmap)
    all_nodes = [
        (row_idx, col_idx)
        for row_idx in range(HEIGHT)
        for col_idx in range(WIDTH)
        if index(row_idx, col_idx) not in starting_nodes
    ]

    visited_nodes = []

    current_node = starting_nodes[0]

    while True:
        visited_nodes.append(current_node)
        neighs = [
            index(node[0], node[1])
            for node in neighbours(current_node[0], current_node[1])
        ]

        for neighbour in neighs:
            pass


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args(argv)
    heatmap = parse_input(args.filename)

    minimal_heights = find_minimal_heights(heatmap)

    print(sum(heatmap[index] + 1 for index in minimal_heights))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

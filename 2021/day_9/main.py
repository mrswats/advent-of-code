import argparse
from collections.abc import Sequence
from functools import reduce

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


def neighbours(row_idx: int, col_idx: int) -> set[tuple[int, int]]:
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


def is_minima(height: int, *height_adjacent_edges: int) -> bool:
    return all(height < adjacent for adjacent in height_adjacent_edges)


def find_minimal_heights(heatmap: list[int]) -> list[int]:
    return [
        (row_idx, col_idx)
        for row_idx in range(HEIGHT)
        for col_idx in range(WIDTH)
        if is_minima(
            heatmap[index(row_idx, col_idx)],
            *(heatmap[index(row, col)] for row, col in neighbours(row_idx, col_idx)),
        )
    ]


def search(heatmap: list[int]):
    starting_nodes = find_minimal_heights(heatmap)

    biggest_basins_len = []

    for starting_node in starting_nodes:
        nodes_to_visit = [starting_node]
        visited_nodes = []

        while True:
            if not nodes_to_visit:
                break

            current_node = nodes_to_visit.pop(0)
            visited_nodes.append(current_node)

            for node in neighbours(current_node[0], current_node[1]):
                if (
                    node not in visited_nodes
                    and node not in nodes_to_visit
                    and heatmap[index(node[0], node[1])] < 9
                ):
                    nodes_to_visit.append(node)

        current_min = min(biggest_basins_len) if biggest_basins_len else 0
        basin_size = len(visited_nodes)
        if current_min < basin_size:
            if current_min in biggest_basins_len and len(biggest_basins_len) == 3:
                biggest_basins_len.remove(current_min)

            biggest_basins_len.append(basin_size)

    return biggest_basins_len


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args(argv)
    heatmap = parse_input(args.filename)

    biggest_basins = search(heatmap)

    print(reduce(lambda a, b: a * b, biggest_basins))

    # minimal_heights = find_minimal_heights(heatmap)

    # print(sum(heatmap[index] + 1 for index in minimal_heights))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

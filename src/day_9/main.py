import argparse
from typing import Sequence

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


def is_minima(height: int, *adjacent_edges: int) -> bool:
    return all(height < adjacent for adjacent in adjacent_edges)


def index(row: int, col: int) -> int:
    return col + row * WIDTH


def find_minimal_heights(heatmap: list[(int, int)]):
    minimal_heights = []
    for row_idx in range(HEIGHT):
        for col_idx in range(WIDTH):
            current_index = index(row_idx, col_idx)
            height = heatmap[current_index]
            if row_idx == TOP_EDGE and col_idx == LEFT_EDGE:
                if is_minima(
                    height,
                    heatmap[index(row_idx, col_idx + 1)],
                    heatmap[index(row_idx + 1, col_idx)],
                ):
                    minimal_heights.append((current_index, height + 1))
            elif row_idx == TOP_EDGE and col_idx == RIGHT_EDGE:
                if is_minima(
                    height,
                    heatmap[index(row_idx, col_idx - 1)],
                    heatmap[index(row_idx + 1, col_idx)],
                ):
                    minimal_heights.append((current_index, height + 1))
            elif row_idx == BOTTOM_EDGE and col_idx == LEFT_EDGE:
                if is_minima(
                    height,
                    heatmap[index(row_idx, col_idx + 1)],
                    heatmap[index(row_idx - 1, col_idx)],
                ):
                    minimal_heights.append((current_index, height + 1))
            elif row_idx == BOTTOM_EDGE and col_idx == RIGHT_EDGE:
                if is_minima(
                    height,
                    heatmap[index(row_idx, col_idx - 1)],
                    heatmap[index(row_idx - 1, col_idx)],
                ):
                    minimal_heights.append((current_index, height + 1))
            elif col_idx == LEFT_EDGE:
                if is_minima(
                    height,
                    heatmap[index(row_idx, col_idx + 1)],
                    heatmap[index(row_idx + 1, col_idx)],
                    heatmap[index(row_idx - 1, col_idx)],
                ):
                    minimal_heights.append((current_index, height + 1))
            elif col_idx == RIGHT_EDGE:
                if is_minima(
                    height,
                    heatmap[index(row_idx, col_idx - 1)],
                    heatmap[index(row_idx + 1, col_idx)],
                    heatmap[index(row_idx - 1, col_idx)],
                ):
                    minimal_heights.append((current_index, height + 1))
            elif row_idx == TOP_EDGE:
                if is_minima(
                    height,
                    heatmap[index(row_idx, col_idx - 1)],
                    heatmap[index(row_idx, col_idx + 1)],
                    heatmap[index(row_idx + 1, col_idx)],
                ):
                    minimal_heights.append((current_index, height + 1))
            elif row_idx == BOTTOM_EDGE:
                if is_minima(
                    height,
                    heatmap[index(row_idx, col_idx - 1)],
                    heatmap[index(row_idx, col_idx + 1)],
                    heatmap[index(row_idx - 1, col_idx)],
                ):
                    minimal_heights.append((current_index, height + 1))
            else:
                if is_minima(
                    height,
                    heatmap[index(row_idx, col_idx - 1)],
                    heatmap[index(row_idx, col_idx + 1)],
                    heatmap[index(row_idx - 1, col_idx)],
                    heatmap[index(row_idx + 1, col_idx)],
                ):
                    minimal_heights.append((current_index, height + 1))
    return minimal_heights


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args(argv)
    heatmap = parse_input(args.filename)

    minimal_heights = find_minimal_heights(heatmap)

    print(sum(pos[1] for pos in minimal_heights))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

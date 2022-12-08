import argparse
from typing import Sequence

INPUT = "input.txt"
TEST_INPUT = """\
30373
25512
65332
33549
35390
"""


def solve(raw_input: str) -> str | int:
    """Parse the input into a matrix.

    The firs tindex of the array represent ROWS.
    The second index represent COLUMNS
    """
    trees = [list(map(int, line)) for line in raw_input.strip().split("\n")]
    perimeter_trees = 2 * (len(trees[0]) + len(trees) - 2)

    visible_trees = 0
    width = len(trees[0]) - 1
    height = len(trees) - 1

    for row in range(1, height):
        for column in range(1, width):
            current_tree_heigt = trees[row][column]
            to_the_left = trees[row][:column]
            to_the_right = trees[row][column + 1 :]
            to_the_top = [trees[i][column] for i in range(0, row)]
            to_the_bottom = [trees[i][column] for i in range(row + 1, height + 1)]

            if (
                all(current_tree_heigt > tree_height for tree_height in to_the_left)
                or all(current_tree_heigt > tree_height for tree_height in to_the_right)
                or all(current_tree_heigt > tree_height for tree_height in to_the_top)
                or all(
                    current_tree_heigt > tree_height for tree_height in to_the_bottom
                )
            ):
                visible_trees += 1

    return visible_trees + perimeter_trees


def read_input(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action=argparse.BooleanOptionalAction, default=True)
    args = parser.parse_args(argv)
    raw_input = TEST_INPUT if args.test else read_input(INPUT)
    print(solve(raw_input))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

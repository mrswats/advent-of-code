import argparse
import functools
from collections.abc import Sequence

INPUT = "input.txt"
TEST_INPUT = """\
30373
25512
65332
33549
35390
"""


def find_first_higher_tree(trees: list[int], tree_height: int) -> int:
    for index, tree in enumerate(trees, start=1):
        if tree >= tree_height:
            return index

    return len(trees)


def solve(raw_input: str) -> str | int:
    """Parse the input into a matrix.

    The firs tindex of the array represent ROWS.
    The second index represent COLUMNS
    """
    trees = [list(map(int, line)) for line in raw_input.strip().split("\n")]
    width = len(trees[0]) - 1
    height = len(trees) - 1

    max_scenic_score = 0

    for row in range(1, height):
        for column in range(1, width):
            current_tree_heigt = trees[row][column]
            to_the_left = trees[row][:column]
            to_the_left.reverse()
            to_the_right = trees[row][column + 1 :]
            to_the_top = [trees[i][column] for i in range(0, row)]
            to_the_top.reverse()
            to_the_bottom = [trees[i][column] for i in range(row + 1, height + 1)]

            scenic_score = [
                find_first_higher_tree(iterable, current_tree_heigt)
                for iterable in (to_the_left, to_the_right, to_the_top, to_the_bottom)
            ]

            computed_scenic_score = functools.reduce(lambda a, b: a * b, scenic_score)

            if max_scenic_score < computed_scenic_score:
                max_scenic_score = computed_scenic_score

    return max_scenic_score


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

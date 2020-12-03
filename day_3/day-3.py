import functools


def read_input() -> list:
    with open("puzzle_input.txt") as fp:
        return fp.read().split("\n")[:-1]


def tree_counter(treemap: list, right_step: int, skip_row: int = 1) -> int:
    """Given a map (as described in the readme) return the number of trees you encounter.

    Parameters:
        - treemap is a list where each row is a string with . and #
        - right_step is the numbers of steps to the right you take each step
        - skip_row is the number of rows you skip at each loop. 1 means no skip.

    Note:
        - Since the map repeats itself into the right (and left too) to
          calculate the next position we must take into account the length of
          each row. Hence the `% len(row)`.
    """

    tree_symbol = "#"
    pos = 0
    counter = 0

    for idx, row in enumerate(treemap):
        if idx % skip_row != 0:
            continue

        if row[pos] == tree_symbol:
            counter += 1

        pos = (pos + right_step) % len(row)

    return counter


def main():
    tree_map = read_input()

    print(
        functools.reduce(
            lambda a, b: a * b,
            (tree_counter(tree_map, step, skip) for step, skip in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]),
        )
    )


if __name__ == "__main__":
    main()

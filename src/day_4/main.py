import re

COLS = 5
ROWS = 5


def parse_file(raw_input: list[str]) -> tuple[tuple[int], tuple[int]]:
    bingo_numbers = [int(num) for num in raw_input[0].split(",")]
    boards = tuple(
        tuple(
            {int(num): False for num in re.findall(r"(\d+)", row)}
            for row in board.split("\n")
        )
        for board in raw_input[1:]
    )

    return bingo_numbers, boards


def check_rows():
    pass


def check_cols():
    pass


def calculate_scores(boards):
    pass


def main() -> int:
    with open("./input.txt") as fo:
        raw_input = fo.read().split("\n\n")

    bingo_numbers, boards = parse_file(raw_input)

    for drawn_number in bingo_numbers:
        for board in boards:
            for row in board:
                if drawn_number in row:
                    row[drawn_number] = True

        if check_rows() or check_cols():
            print("BINGOOO!!!!!")
            break

    calculate_scores(boards)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

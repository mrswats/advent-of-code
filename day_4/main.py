import re
from collections import OrderedDict

COLS = 5
ROWS = 5

FILENAME = "input.txt"


def parse_file(raw_input: list[str]) -> tuple[tuple[int], tuple[int]]:
    bingo_numbers = [int(num) for num in raw_input[0].split(",")]
    boards = tuple(
        tuple(
            OrderedDict((int(num), False) for num in re.findall(r"(\d+)", row))
            for row in board.split("\n")
            if row
        )
        for board in raw_input[1:]
    )

    return bingo_numbers, boards


def check_rows(board) -> bool:
    for row in board:
        if row and all(value for value in row.values()):
            return True
    else:
        return False


def check_cols(board) -> bool:
    for ith in range(COLS):
        if all(row[list(row.keys())[ith]] for row in board):
            return True
    else:
        False


def calculate_score(board, drawn_number):
    return drawn_number * sum(
        key for row in board for key, value in row.items() if not value
    )


def main() -> int:
    with open(FILENAME) as fo:
        raw_input = fo.read().split("\n\n")

    bingo_numbers, boards = parse_file(raw_input)

    boards_which_have_won = []

    for drawn_number in bingo_numbers:
        for index, board in enumerate(boards):
            for row in board:
                if drawn_number in row:
                    row[drawn_number] = True

            if (
                check_cols(board) or check_rows(board)
            ) and board not in boards_which_have_won:
                if len(boards_which_have_won) == len(boards) - 1:
                    remaining_board = [
                        board2
                        for board2 in boards
                        if board2 not in boards_which_have_won
                    ]

                    assert len(remaining_board) == 1

                    last_winning_index = boards.index(remaining_board[0])
                    score = calculate_score(remaining_board[0], drawn_number)
                    print(
                        f"Last board (number {last_winning_index}) has score of {score}"
                    )

                print(f"Board number {index} has won!")
                boards_which_have_won.append(board)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

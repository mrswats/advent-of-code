import re


def parse_file(raw_input: list[str]) -> tuple[list[int], list[int]]:
    bingo_numbers = [int(num) for num in raw_input[0].split(",")]
    boards = [
        [[int(num) for num in re.findall(r"(\d+)", row)] for row in board.split("\n")]
        for board in raw_input[1:]
    ]

    return bingo_numbers, boards


def check_rows(board: list[list[int]]):
    pass


def check_cols(board: list[list[int]]):
    pass


def main() -> int:
    with open("./input.txt") as fo:
        raw_input = fo.read().split("\n\n")

    bingo_numbers, boards = parse_file(raw_input)

    for drawn_number in bingo_numbers:
        for board in boards:
            for row in board:
                if drawn_number in row:
                    row.remove(drawn_number)

            check_rows(board)
            check_cols(board)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

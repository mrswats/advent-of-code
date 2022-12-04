def read_input():
    with open("puzzle_input.txt") as fp:
        return fp.read().split("\n")[:-1]


def process_input(input_data: list) -> list:
    """Read each line and transform from BF to 10 and RL to 10 ass well.

    Return a list of tuples with the encoded row, col.
    """

    transformations = [("B", "1"), ("F", "0"), ("R", "1"), ("L", "0")]

    processed_data = []

    for boarding_pass in input_data:
        for transformation in transformations:
            boarding_pass = boarding_pass.replace(*transformation)

        processed_data.append((boarding_pass[:7][::-1], boarding_pass[7:][::-1]))

    return processed_data


def binary_to_decimal(binary_number: str) -> int:
    """Given a string representation of a binary number return the integer counterpart."""

    return sum(int(digit) * 2 ** index for index, digit in enumerate(binary_number))


def boarding_pass_id(row: int, col: int) -> int:
    """Every seat also has a unique seat ID: multiply the row by 8, then add the column.

    In this example, the seat has ID 44 * 8 + 5 = 357.
    """

    return row * 8 + col


def calculite_row_col(processed_input: list):
    return [(binary_to_decimal(row), binary_to_decimal(col)) for row, col in processed_input]


def calculate_pass_id(clean_boarding_passes: list) -> list:
    return [boarding_pass_id(plane_row, plane_col) for plane_row, plane_col in clean_boarding_passes]


def main():
    raw_input_data = read_input()
    processed_data = process_input(raw_input_data)
    boarding_row_cols = calculite_row_col(processed_data)
    boarding_pasees_id = calculate_pass_id(boarding_row_cols)
    print(f"Max ID on the Boarding Passes List: {max(boarding_pasees_id)}")

    # Part two
    all_possible_seats = set(range(99, 975))
    print(f"The unoccupied seat is: {all_possible_seats - set(boarding_pasees_id)}")


if __name__ == "__main__":
    main()

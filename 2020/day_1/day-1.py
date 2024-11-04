def read_input() -> list:
    """Read the provided input and return a list of integers from that."""
    with open("puzzle_input.txt") as fp:
        data = fp.read()

    return list(map(int, data.split("\n")[:-1]))


def main(expense_report: list) -> int | None:
    """Find two numbers in the list that sum up to 2020 and return their product.

    So, iterating over all numbers, we subtract the current number to the target, 2020 in this case, and check if the
    number is in the list. If so, we found our solution and we return the product.
    """

    target = 2020

    for entry in expense_report:
        rest = target - entry
        if rest in expense_report:
            return entry * rest

    return None


def part_two(expense_report: list) -> int | None:
    """This time, do the same but with three numbers.

    Now, we have to iterate twice over the list to find all possible combinations until we find our solution.
    This could probably be optimised to not iterate twice over the same list or find a clever way of choosing two
    candidates.

    Maybe we can sort the numbers and check the first number against the next until we surpass the target number
    until we find a solution. This way we are guaranteed (?) to find our numbers + not have to iterate over all the
    list if not necessary.
    """

    target = 2020

    for lentry in expense_report:
        for rentry in expense_report:
            rest = target - (lentry + rentry)
            if rest in expense_report:
                return rest * lentry * rentry

    return None


if __name__ == "__main__":
    expense_report = read_input()

    print("Part one solution: ", main(expense_report))
    print("Part two solution: ", part_two(expense_report))

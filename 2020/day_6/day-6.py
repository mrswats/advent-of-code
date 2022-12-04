import functools


def read_input() -> list:
    """Split the data into different groups by a blank line."""
    with open("puzzle_input.txt") as fp:
        return fp.read().split("\n\n")


def parse_answers_v1(raw_data: list) -> list:
    """Here we just want all the different answers in a group."""
    return [set(group.replace("\n", "")) for group in raw_data]


def parse_answers_v2(raw_data: list) -> list:
    """For each group keep the unique answers but cast it to sets for later use."""
    return [[set(answer) for answer in group.split("\n") if answer] for group in raw_data]


def positive_answers_per_group(answers_list: list) -> list:
    """Each element is a set, so count he length of each set."""
    return [len(answer) for answer in answers_list]


def positive_common_ansers_per_group(answers_list: list) -> list:
    """Here each answer per group is a list of sets.

    Since we just want the common answers among them, use the disjoint operator among them and count the resulting
    length.
    """
    return [len(functools.reduce(lambda A, B: A & B, answer)) for answer in answers_list]


def main():
    raw_data = read_input()
    parsed_data_v1 = parse_answers_v1(raw_data)
    positive_answers = positive_answers_per_group(parsed_data_v1)
    print(f"Amount of total positive answers per group, sumemd all up: {sum(positive_answers)}")

    parsed_data_v2 = parse_answers_v2(raw_data)
    unique_answers = positive_common_ansers_per_group(parsed_data_v2)
    print(f"Amount of total common positive answers per grop summd: {sum(unique_answers)}")


if __name__ == "__main__":
    main()

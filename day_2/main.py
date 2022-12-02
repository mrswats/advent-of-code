import argparse
from typing import Sequence

"""
A: Rock -> 1
B: Paper -> 2
C: Scissors -> 3

X: LOSE
Y: DRAW
Z: WIN
"""

possible_choices = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSORS",
}

possible_outcomes = {
    "X": "LOSE",
    "Y": "DRAW",
    "Z": "WIN",
}

outcome_table = {
    "WIN": {
        "A": "B",
        "B": "C",
        "C": "A",
    },
    "LOSE": {
        "A": "C",
        "B": "A",
        "C": "B",
    },
}

choice = {
    "A": 1,
    "B": 2,
    "C": 3,
}

points = {
    "WIN": 6,
    "DRAW": 3,
    "LOSE": 0,
}


def parse_input(filename: str) -> list[str]:
    with open(filename) as f:
        return [tuple(line.strip().split(" ")) for line in f.readlines()]


def select_choice(outcome: str, opponent: str) -> str:
    if outcome == "DRAW":
        return opponent
    elif outcome == "WIN" or outcome == "LOSE":
        return outcome_table[outcome][opponent]

    raise AssertionError(f"Something went wrong, cant deal with outcome {outcome}")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("--debug", action=argparse.BooleanOptionalAction, default=False)
    args = parser.parse_args(argv)
    raw_input = parse_input(args.filename)

    total_score = 0
    for round in raw_input:
        opponent, expected_outcome = round
        my_choice = select_choice(possible_outcomes[expected_outcome], opponent)
        if args.debug:
            print(
                "Desired outcome: {}, opponent choice: {}, my choice: {} "
                "score: {} + {}".format(
                    possible_outcomes[expected_outcome],
                    possible_choices[opponent],
                    possible_choices[my_choice],
                    choice[my_choice],
                    points[possible_outcomes[expected_outcome]],
                )
            )
        total_score += points[possible_outcomes[expected_outcome]] + choice[my_choice]

    print(total_score)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

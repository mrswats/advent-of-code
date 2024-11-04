from __future__ import annotations

import argparse
import heapq
import math
import re
from collections.abc import Sequence
from dataclasses import dataclass

NUMBER_OF_ROUNDS = 10_000


MONKEY_ID_RE = re.compile(r"Monkey (\d+):")
STARTING_ITEMS_RE = re.compile(r"Starting items: (.+)")
OPERATION_RE = re.compile(r"Operation: new = (.+)")
DIVISIBILITY_TEST_RE = re.compile(r"Test: divisible by (\d+)")
RESULT_TEST_RE = re.compile(r"If (true|false): throw to monkey (\d+)")


@dataclass
class Monkey:
    monkey_id: int
    starting_items: list[int]
    operation: str
    divisibility_test: int
    pass_onto: dict[bool, int]
    monkey_business: int = 0


def solve(monkeys: list[Monkey]) -> str | int:
    common_factor = math.prod(monkey.divisibility_test for monkey in monkeys)

    operations = {
        "*": lambda a, b: a * b,
        "+": lambda a, b: a + b,
    }

    for _roundno in range(NUMBER_OF_ROUNDS):
        for monkey in monkeys:
            lhs, operation, rhs = monkey.operation.split()

            for item in monkey.starting_items:
                lhs_val = item if lhs == "old" else int(lhs)
                rhs_val = item if rhs == "old" else int(rhs)
                new_worry_level = (
                    operations[operation](lhs_val, rhs_val) % common_factor
                )
                new_monkey = monkeys[
                    monkey.pass_onto[new_worry_level % monkey.divisibility_test == 0]
                ]
                new_monkey.starting_items.append(new_worry_level)

            monkey.monkey_business += len(monkey.starting_items)
            monkey.starting_items = []

    sorted_monkeys = heapq.nlargest(
        2, monkeys, key=lambda monkey: monkey.monkey_business
    )

    return math.prod(monkey.monkey_business for monkey in sorted_monkeys)


def parse_input(raw_input: str) -> list[Monkey]:
    monkeys = []

    for line in raw_input.split("\n\n"):
        monkey_id = MONKEY_ID_RE.findall(line).pop()
        starting_items = STARTING_ITEMS_RE.findall(line).pop()
        operation = OPERATION_RE.findall(line).pop()
        divisibility_test = DIVISIBILITY_TEST_RE.findall(line).pop()
        pass_onto = RESULT_TEST_RE.findall(line)

        monkey = Monkey(
            monkey_id=int(monkey_id),
            starting_items=[int(elem) for elem in starting_items.split(",")],
            operation=operation,
            divisibility_test=int(divisibility_test),
            pass_onto={
                (True if key == "true" else False): int(val) for key, val in pass_onto
            },
        )

        monkeys.append(monkey)

    return monkeys


def read_input_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()


INPUT = "input.txt"
TEST_INPUT = """\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action=argparse.BooleanOptionalAction, default=True)
    args = parser.parse_args(argv)
    raw_input = TEST_INPUT if args.test else read_input_file(INPUT)
    print(solve(parse_input(raw_input)))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

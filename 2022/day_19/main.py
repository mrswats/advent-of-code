from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from typing import NamedTuple, Sequence

INPUT = "input.txt"
TEST_INPUT = """\
Blueprint 1: \
Each ore robot costs 4 ore. \
Each clay robot costs 2 ore. \
Each obsidian robot costs 3 ore and 14 clay. \
Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: \
Each ore robot costs 2 ore. \
Each clay robot costs 3 ore. \
Each obsidian robot costs 3 ore and 8 clay. \
Each geode robot costs 3 ore and 12 obsidian.
"""

TOTAL_TIME = 24

BLUEPRINT_RE = re.compile(
    r"Blueprint (\d+).+ore robot costs (\d+) ore.+"
    r"clay robot costs (\d+) ore.+"
    r"obsidian robot costs (\d+) ore and (\d+) clay.+"
    r"geode robot costs (\d+) ore and (\d+) obsidian"
)


class Robot(NamedTuple):
    cost_ore: int = 0
    cost_clay: int = 0
    cost_obsidian: int = 0


class Blueprint(NamedTuple):
    ore_robot: Robot
    clay_robot: Robot
    obsidian_robot: Robot
    geode_robot: Robot


@dataclass
class Resources:
    ore: int = 0
    clay: int = 0
    obsidian: int = 0
    geode: int = 0


@dataclass
class RobotTypes:
    ore: int = 1
    clay: int = 0
    obsidian: int = 0
    geode: int = 0


def solve_part1(blueprints: dict[int, Blueprint]) -> int:

    quality_levels = {}

    for blueprint_id, blueprint in blueprints.items():
        resources = Resources()
        robot_types = RobotTypes()

        for minute in range(1, TOTAL_TIME + 1):
            print(f"----- Minute {minute} ----")

            if (
                resources.obsidian >= blueprint.geode_robot.cost_obsidian
                and resources.ore >= blueprint.geode_robot.cost_ore
            ):
                robot_types.geode += 1
                resources.ore -= blueprint.geode_robot.cost_ore
                resources.obsidian -= blueprint.geode_robot.cost_obsidian

            elif (
                resources.clay >= blueprint.obsidian_robot.cost_clay
                and resources.ore >= blueprint.obsidian_robot.cost_ore
                and robot_types.obsidian <= 2
            ):
                robot_types.obsidian += 1
                resources.ore -= blueprint.obsidian_robot.cost_ore
                resources.clay -= blueprint.obsidian_robot.cost_clay

            elif (
                resources.ore >= blueprint.clay_robot.cost_ore and robot_types.clay <= 4
            ):
                robot_types.clay += 1
                resources.ore -= blueprint.clay_robot.cost_ore

            elif resources.ore >= blueprint.ore_robot.cost_ore and robot_types != 1:
                robot_types.ore += 1
                resources.ore -= blueprint.ore_robot.cost_ore

            resources.ore += robot_types.ore
            resources.clay += robot_types.clay
            resources.obsidian += robot_types.obsidian
            resources.geode += robot_types.geode

            print(f"{resources=}")
            print(f"{robot_types=}")
            print()

        quality_levels[blueprint_id] = blueprint_id * resources.geode
        print("#" * 80, end="\n\n")
        break

    print(f"{quality_levels=}")

    return 0


def solve_part2(parsed_data: str) -> str | int:
    return len(parsed_data)


def parse_input(raw_input: str) -> dict[int, Blueprint]:
    blueprints = {}

    for blueprint in raw_input.splitlines():
        (
            bid,
            ore_robot,
            clay_robot,
            obsidian_robot_1,
            obsidian_robot_2,
            geode_robot_1,
            geode_robot_2,
        ) = tuple(map(int, BLUEPRINT_RE.findall(blueprint).pop()))
        ore_robot = Robot(cost_ore=ore_robot)
        clay_robot = Robot(cost_ore=clay_robot)
        obsidian_robot = Robot(cost_ore=obsidian_robot_1, cost_clay=obsidian_robot_2)
        geode_robot = Robot(cost_ore=geode_robot_1, cost_obsidian=geode_robot_2)

        blueprints[bid] = Blueprint(
            ore_robot,
            clay_robot,
            obsidian_robot,
            geode_robot,
        )

    return blueprints


def read_input_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--part2", action=argparse.BooleanOptionalAction, default=False)
    args = parser.parse_args(argv)
    raw_input = TEST_INPUT if args.test else read_input_file(INPUT)
    parsed_input = parse_input(raw_input)
    print(solve_part2(parsed_input) if args.part2 else solve_part1(parsed_input))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

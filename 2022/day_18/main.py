from __future__ import annotations

import argparse
import heapq
from collections.abc import Sequence

INPUT = "input.txt"
TEST_INPUT = """\
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
"""


Droplet = set[tuple[int, ...], str]


def draw_droplet(droplet: Droplet) -> None:
    max_x = max(x for x, *_ in droplet)
    max_y = max(y for _, y, _ in droplet)
    max_z = max(z for *_, z in droplet)

    z_plane = {(x, y) for x, y, _ in droplet}
    y_plane = {(x, z) for x, _, z in droplet}
    x_plane = {(y, z) for _, y, z in droplet}

    for plane, max_1, max_2 in [
        (x_plane, max_y, max_z),
        (y_plane, max_x, max_z),
        (z_plane, max_y, max_x),
    ]:
        for qcoord in range(-1, max_2 + 3):
            for pcoord in range(-1, max_1 + 3):
                print("#" if (pcoord, qcoord) in plane else ".", end="")
            print()
        print()


def solve_part1(droplet: Droplet) -> int:
    x_plane = sum(1 for x, y, z in droplet if (x + 1, y, z) not in droplet)
    mx_plane = sum(1 for x, y, z in droplet if (x - 1, y, z) not in droplet)
    y_plane = sum(1 for x, y, z in droplet if (x, y + 1, z) not in droplet)
    my_plane = sum(1 for x, y, z in droplet if (x, y - 1, z) not in droplet)
    z_plane = sum(1 for x, y, z in droplet if (x, y, z + 1) not in droplet)
    mz_plane = sum(1 for x, y, z in droplet if (x, y, z - 1) not in droplet)

    draw_droplet(droplet)

    return sum((x_plane, mx_plane, y_plane, my_plane, z_plane, mz_plane))


def neighbours_of(x: int, y: int, z: int) -> set[tuple[int, ...]]:
    return {
        (x + 1, y, z),
        (x - 1, y, z),
        (x, y + 1, z),
        (x, y - 1, z),
        (x, y, z + 1),
        (x, y, z - 1),
    }


def find_surface(droplet: Droplet) -> set[tuple[int, ...]]:
    max_x = max(x for x, *_ in droplet)
    max_y = max(y for _, y, _ in droplet)
    max_z = max(z for *_, z in droplet)

    def in_bounds(x: int, y: int, z: int) -> bool:
        return 0 <= x <= max_x and 0 <= y <= max_y and 0 <= z <= max_z

    root = (0, 0, 0)
    todo = [root]
    seen = set()
    surface = set()

    while todo:
        current = heapq.heappop(todo)

        if current in seen:
            continue
        else:
            seen.add(current)

        if current in droplet:
            surface.add(current)
            continue

        for neighbour in neighbours_of(*current):
            if in_bounds(*neighbour):
                heapq.heappush(todo, neighbour)

    return surface


def solve_part2(droplet: Droplet) -> int:
    surface = find_surface(droplet)

    def inside_shell(x: int, y: int, z: int) -> bool:
        return any(
            xp1 < x < xp2 and yp1 < y < yp2 and zp1 < z < zp2
            for xp1, yp1, zp1 in surface
            for xp2, yp2, zp2 in surface
        )

    return 0


def parse_input(raw_input: str) -> Droplet:
    return {tuple(map(int, line.split(","))) for line in raw_input.splitlines()}


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

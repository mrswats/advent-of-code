import argparse
from collections import defaultdict
from typing import Sequence

INPUT = "input.txt"
TEST_INPUT = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

MAX_FILE_SIZE = 100000
TOTAL_DISK_SIZE = 70000000
MINIMUM_DISK_SIZE = 30000000


def printdir(current_dir: list[str]) -> str:
    return "".join(current_dir)


def parse_input(raw_input: str) -> dict[str, list[int | str]]:
    current_dir = ["/"]
    directory = defaultdict(list)
    for line in raw_input.splitlines()[1:]:
        if line.startswith("$"):
            command = line[2:].split(" ")
            if command[0] == "cd":
                if command[1] == "..":
                    current_dir.pop()
                else:
                    current_dir.append(command[1] + "/")
            elif command[0] == "ls":
                continue
        else:
            output = line.split(" ")
            if output[0].isdigit():
                output = [int(output[0]), output[1]]
            directory[printdir(current_dir)].append(output)

    return directory


def solve(raw_input: str) -> str | int:
    data = parse_input(raw_input)
    total_sizes = defaultdict(int)

    for current_dir in sorted(data.keys(), key=len, reverse=True):
        for current_file in data[current_dir]:
            total_sizes[current_dir] += (
                current_file[0]
                if isinstance(current_file[0], int)
                else total_sizes[printdir(f"{current_dir}{current_file[1]}/")]
            )

    unused_disk_space = TOTAL_DISK_SIZE - total_sizes["/"]

    smallest_dir_size = TOTAL_DISK_SIZE
    for current_dir_size in total_sizes.values():
        if (
            unused_disk_space + current_dir_size > MINIMUM_DISK_SIZE
            and current_dir_size < smallest_dir_size
        ):
            smallest_dir_size = current_dir_size

    return smallest_dir_size


def read_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action=argparse.BooleanOptionalAction, default=True)
    args = parser.parse_args(argv)
    raw_input = TEST_INPUT if args.test else read_file(INPUT)
    print(solve(raw_input))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

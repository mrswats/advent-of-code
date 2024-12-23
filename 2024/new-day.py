#!/usr/bin/env python3
import argparse
import functools
import os
import re
import shutil
from collections.abc import Sequence
from datetime import datetime

import httpx
import markdownify

PARSE_STATEMENT_REGEX = r'<article\s+class="day-desc">[\s\S]*?</article>'


@functools.cache
def get_headers() -> dict:
    with open("./.env") as f:
        return {
            "Cookie": f.read().strip(),
            "User-Agent": (
                "gitlab.com/mrswats/advent-of-code by @mswats <ferran@jovell.dev>"
            ),
        }


def download_problem_statement(year: int, day: int) -> str:
    response = httpx.get(
        f"https://adventofcode.com/{year}/day/{day}",
    )
    parsed = re.search(PARSE_STATEMENT_REGEX, response.content.decode())
    return markdownify.markdownify(parsed.group()) if parsed else ""


def download_input(year: int, day: int) -> str:
    response = httpx.get(
        f"https://adventofcode.com/{year}/day/{day}/input",
        headers=get_headers(),
    )
    return response.content.decode()


def create_new_dir(dirname: str) -> bool:
    if not os.path.exists(dirname):
        os.mkdir(dirname)
        print(f"Created {dirname}")
        return True
    else:
        print("Folder already exists. Not overriding.")
        return False


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    today = datetime.now()
    parser.add_argument("--day", type=int, default=today.day)
    parser.add_argument("--year", type=int, default=today.year)
    args = parser.parse_args(argv)

    folder_name = f"day_{args.day:02}"
    current_dir = os.getcwd()
    new_dir = f"{current_dir}/{folder_name}/"

    if not create_new_dir(new_dir):
        return 1

    shutil.copy(f"{current_dir}/template.py", f"{new_dir}/part1.py")
    print(f"Copied `template.py` into ./{folder_name}/part1.py")

    raw_statement = download_problem_statement(args.year, args.day)
    with open(f"{new_dir}/README.md", "w") as f:
        f.write(raw_statement)

    print(f"Dwoloading input for day {args.day}/{args.year}")
    raw_input = download_input(args.year, args.day)
    with open(f"{new_dir}/input.txt", "w") as f:
        f.write(raw_input)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

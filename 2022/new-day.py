#!/usr/bin/env python3
import argparse
import os
import re
import shutil
import urllib.request
from collections.abc import Sequence
from datetime import datetime

import markdownify

PARSE_STATEMENT_REGEX = r'<article\s+class="day-desc">[\s\S]*?</article>'


def get_headers() -> dict:
    with open("./.env") as f:
        return {
            "Cookie": f.read().strip(),
            "User-Agent": (
                "gitlab.com/mrswats/advent-of-code by @mswats <ferran@jovell.dev>"
            ),
        }


def download_problem_statement(year: int, day: int) -> str:
    request = urllib.request.Request(
        f"https://adventofcode.com/{year}/day/{day}",
        method="GET",
        headers=get_headers(),
    )
    response = urllib.request.urlopen(request)
    raw_content = response.read().decode()
    parsed = re.search(PARSE_STATEMENT_REGEX, raw_content)
    return markdownify.markdownify(parsed.group()) if parsed else ""


def download_input(year: int, day: int) -> str:
    request = urllib.request.Request(
        f"https://adventofcode.com/{year}/day/{day}/input",
        method="GET",
        headers=get_headers(),
    )
    response = urllib.request.urlopen(request)
    return response.read().decode()


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

    folder_name = f"day_{args.day}"
    current_dir = os.getcwd()
    new_dir = f"{current_dir}/{folder_name}/"

    if not create_new_dir(new_dir):
        return 1

    shutil.copy(f"{current_dir}/template.py", f"{new_dir}/main.py")
    print(f"Copied `template.py` into ./{folder_name}/main.py")

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

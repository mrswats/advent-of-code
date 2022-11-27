import argparse
import os
import shutil
from datetime import datetime
from typing import Sequence


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
    parser.add_argument("--day", type=int, default=datetime.now().day)
    args = parser.parse_args(argv)

    folder_name = f"day_{args.day}"
    current_dir = os.getcwd()
    new_dir = f"{current_dir}/{folder_name}/"

    if not create_new_dir(new_dir):
        return 1

    shutil.copy(f"{current_dir}/template.py", f"{new_dir}/main.py")
    print(f"Copied `template.py` into ./{folder_name}/main.py")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

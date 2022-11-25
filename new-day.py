import argparse
import os
import shutil
from typing import Sequence

FOLDER_TEMPLATE = "day_{dayno}"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int)
    args = parser.parse_args(argv)

    dayno = args.day

    folder_name = FOLDER_TEMPLATE.format(dayno=dayno)

    current_dir = os.getcwd()

    new_dir = f"{current_dir}/{folder_name}/"

    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
        print(f"Created {new_dir}")
    else:
        print("Folder already exists. Not overriding.")
        return 1

    shutil.copy(f"{current_dir}/template.py", f"{new_dir}/main.py")
    print(f"Copied `template.py` into ./{folder_name}/main.py")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

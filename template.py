import argparse
from typing import Sequence


def parse_input(filename: str) -> list[str]:
    with open(filename) as f:
        return f.readlines()


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args(argv)
    raw_input = parse_input(args.filename)

    print(raw_input)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

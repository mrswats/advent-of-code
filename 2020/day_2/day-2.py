import collections
import operator
import re

parse_regex = re.compile(r"(\d+)-(\d+)\s*(\w+):\s* (\w+)$")


def read_input() -> list[str]:
    with open("puzzle_input.txt") as fp:
        return fp.read().split("\n")[:-1]


def check_password_v1(string: str) -> bool:
    if parsed := parse_regex:
        lower, higher, token, passwd = parsed.match(string).groups()
        counter = collections.Counter(passwd)

        return int(counter[token]) >= int(lower) and int(counter[token]) <= int(higher)

    return False


def check_password_v2(string: str) -> bool:
    if parsed := parse_regex:
        lower, higher, token, passwd = parsed.match(string).groups()

        return operator.xor(
            passwd[int(lower) - 1] == token, passwd[int(higher) - 1] == token
        )

    return False


def main():
    print(
        "Correct passwords (v1): ",
        [check_password_v1(string) for string in read_input()].count(True),
    )
    print(
        "Correct passwords (v2): ",
        [check_password_v2(string) for string in read_input()].count(True),
    )


if __name__ == "__main__":
    main()

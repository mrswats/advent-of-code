def read_input(filename: str) -> list:
    with open(filename) as fp:
        return fp.read().split("\n")[:-1]


def main():
    raw_input_data = read_input("example_input.txt")

    print(raw_input_data)


if __name__ == "__main__":
    main()

import re
import sys

this = sys.modules[__name__]

batch_parser = re.compile(r"((?:ecl|pid|eyr|hcl|byr|iyr|cid|hgt):[\w#]+)")


def read_input():
    # with open("example_input.txt") as fp:
    with open("puzzle_input.txt") as fp:
        raw_data = fp.read()

    return [
        dict([tuple(field.split(":")) for field in batch_parser.findall(pssprt)]) for pssprt in raw_data.split("\n\n")
    ]


def validate_byr(field: str) -> bool:
    """byr (Birth Year) - four digits; at least 1920 and at most 2002."""

    return bool(re.match(r"^\d{4}$", field)) and 1920 <= int(field) <= 2002


def validate_iyr(field: str) -> bool:
    """iyr (Issue Year) - four digits; at least 2010 and at most 2020."""

    return bool(re.match(r"^\d{4}$", field)) and 2010 <= int(field) <= 2020


def validate_eyr(field: str) -> bool:
    """eyr (Expiration Year) - four digits; at least 2020 and at most 2030."""

    return bool(re.match(r"^\d{4}$", field)) and 2020 <= int(field) <= 2030


def validate_hgt(field: str) -> bool:
    """Validate height

    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    """

    if (match := re.match(r"^(\d+)(in|cm)$", field)) :
        hgt, unit = match.groups()

        if unit == "cm":
            return 150 <= float(hgt) <= 193

        if unit == "in":
            return 59 <= float(hgt) <= 76

    return False


def validate_hcl(field: str) -> bool:
    """hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f."""

    return bool(re.match(r"^#[0-9a-f]{6}$", field))


def validate_ecl(field: str) -> bool:
    """ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth."""

    return field in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def validate_pid(field: str) -> bool:
    """pid (Passport ID) - a nine-digit number, including leading zeroes."""

    return bool(re.match(r"^\d{9}$", field))


def validate_cid(field: str) -> bool:
    """cid (Country ID) - ignored, missing or not."""

    return True


def validate_passport_data_v2(passport: dict) -> bool:
    """Check if all fields are present in the passport dictionary."""

    # if all(field in passport for field in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]):
    #     validicity = []
    #     for field, value in passport.items():
    #         validator = getattr(this, f"validate_{field}")
    #         validicity.append(validator(value))

    #     return all(validicity)
    # return False

    return (
        all(getattr(this, f"validate_{field}")(val) for field, val in passport.items())
        if all(field in passport for field in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
        else False
    )


def validate_passport_data_v1(passport: dict) -> bool:
    """Check if all fields are present in the passport dictionary."""
    return all(field in passport for field in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


def main():
    batch_file = read_input()

    valids_count = [validate_passport_data_v1(passport) for passport in batch_file].count(True)
    print(f"Valid passports (v1): {valids_count}")

    valids_count = [validate_passport_data_v2(passport) for passport in batch_file].count(True)
    print(f"Valid passports (v2): {valids_count}")


if __name__ == "__main__":
    main()

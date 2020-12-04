"""Day 4 logic."""
from pathlib import Path
import re

CRITERIA = {
    "byr": range(1920, 2003),
    "iyr": range(2010, 2021),
    "eyr": range(2020, 2031),
    "hgt": {
        "cm": range(150, 194),
        "in": range(59, 77)
    },
    "hcl": r"#[0-9a-f]{6}",
    "ecl": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": 9,
}


def get_passports():
    """Get the passports from the .dat file.

    Returns:
        list: List of passports as dictionaries.
    """
    passports = []
    data_file = Path("./data_4.dat")
    with open(data_file, "r") as read_file:
        passport_strs = read_file.read().split("\n\n")

    for passport_str in passport_strs:
        fields = re.split(" |\n", passport_str)
        passport = {}
        for field in fields:
            split = field.split(":")
            passport[split[0]] = split[1]
        passports.append(passport)

    return passports


def check_range_criteria(passport):
    """Check the criterion with ranges are valid or not.

    Args:
        passport (dict): The passport to check

    Returns:
        bool: True if the criterion are valid.
    """
    checks = []
    for key in ["byr", "iyr", "eyr"]:
        try:
            if int(passport[key]) not in CRITERIA[key]:
                checks.append(False)
        except ValueError:
            checks.append(False)
    return all(checks)


def check_height_criteria(passport):
    """Check the height criteria is valid or not.

    Args:
        passport (dict): The passport to check

    Returns:
        bool: True if the height criteria is valid.
    """
    checks = []
    try:
        unit = passport["hgt"][-2:]
        if unit not in CRITERIA["hgt"].keys():
            checks.append(False)
        if int(passport["hgt"][:-2]) not in CRITERIA["hgt"][unit]:
            checks.append(False)
    except (KeyError, ValueError):
        checks.append(False)
    return all(checks)


def is_valid_passport(passport, criteria=True):
    """Return whether passport is valid or not.

    Args:
        passport (dict): The passport dict to check.
        criteria (bool): Whether to validate criteria data. (default: {True})

    Returns:
        bool: True if passport is valid, false if invalid passport.
    """
    valid = []
    required_keys = [
        "byr",
        "ecl",
        "eyr",
        "hcl",
        "hgt",
        "iyr",
        "pid",
    ]

    passport_keys = passport.keys()

    common_keys = set(passport_keys).intersection(required_keys)

    if set(common_keys) == set(required_keys):
        if criteria:
            valid.append(check_range_criteria(passport))

            valid.append(passport["ecl"] in CRITERIA["ecl"])

            valid.append(re.search(CRITERIA["hcl"], passport["hcl"]))

            valid.append(all([
                passport["pid"].isnumeric(),
                len(passport["pid"]) == CRITERIA["pid"]
            ]))

            valid.append(check_height_criteria(passport))
        else:
            valid = [True]
    else:
        valid = [False]

    return all(valid)


def get_number_of_valid_passports(passports, criteria=True):
    """Get the number of valid passports in given list of passports.

    Args:
        passports (list): list of dictionary objects.
        criteria (bool): Whether to validate criteria data. (default: {True})

    Returns:
        int: Number of valid passports.
    """
    valid_passports = 0
    for passport in passports:
        valid_passports += is_valid_passport(passport, criteria)

    return valid_passports


def main():
    """Print results for day 4."""
    passports = get_passports()
    print(get_number_of_valid_passports(passports))


if __name__ == '__main__':
    main()

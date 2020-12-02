"""Day 2 logic."""
from pathlib import Path


def get_passwords():
    """Get the passwords from .dat file.

    Returns:
        dict: Policy criteria as key and passwords in a list as value.
    """
    passwords = {}
    data_file = Path("./data_1.dat")
    with open(data_file, "r") as read_file:
        values = read_file.read().splitlines()
    for value in values:
        split = value.split(": ")
        if split[0] in passwords:
            passwords[split[0]].append(split[1])
        else:
            passwords[split[0]] = [split[1]]

    return passwords


def get_valid_passwords_policy_one(passwords):
    """Get valid passwords.

    A valid password is one that contains the letter in the critera for
    at least the minumum amount and no more than the maximum amount.
    The min and max amounts are also definied in the criteria.

    The criteria is the key, the passwords with that criteria
    are in a list as the value.

    Args:
        passwords: Dictionary of passwords, policy criteria as key
            and passwords in a list as value.

    Returns:
        int: The amount of valid passwords for this policy.
    """
    valid_passwords = 0
    for criteria, values in passwords.items():
        for password in values:
            minimum = int(criteria.split("-")[0])
            maximum = int(criteria.split("-")[1].split(" ")[0])
            letter = criteria.split("-")[1].split(" ")[1]
            if minimum <= password.count(letter) <= maximum:
                valid_passwords += 1

    return valid_passwords


def get_valid_passwords_policy_two(passwords):
    """Get valid passwords.

    A valid password is one that contains the letter in the critera at
    either the first position or the second position, not both.
    The positions are also definied in the criteria. These policies have
    no concept of index zero so position 1 would be the first position,
    not the second.

    The criteria is the key, the passwords with that criteria
    are in a list as the value.

    Args:
        passwords: Dictionary of passwords, policy criteria as key
            and passwords in a list as value.

    Returns:
        int: The amount of valid passwords for this policy.
    """
    valid_passwords = 0
    for criteria, values in passwords.items():
        for password in values:
            first_position = int(criteria.split("-")[0]) - 1
            second_position = int(criteria.split("-")[1].split(" ")[0]) - 1
            letter = criteria.split("-")[1].split(" ")[1]
            conditions = [
                password[first_position] == letter,
                password[second_position] == letter,
            ]
            if any(conditions) and not all(conditions):
                valid_passwords += 1

    return valid_passwords


def main():
    """Print results for day 2."""
    passwords = get_passwords()
    print(get_valid_passwords_policy_one(passwords))
    print(get_valid_passwords_policy_two(passwords))


if __name__ == '__main__':
    main()

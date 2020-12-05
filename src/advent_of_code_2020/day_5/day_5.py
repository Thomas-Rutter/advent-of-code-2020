"""Day 5 logic."""
from pathlib import Path
import re


def get_boarding_passes(path):
    """Get the boarding passes from the .dat file.

    Args:
        path (str): The path to the file to open.

    Returns:
        list: List of boarding passes as strings.
    """
    with open(Path(f"{path}"), "r") as read_file:
        return read_file.readlines()


def get_seat_id(boarding_pass):
    """Return the seat id from the boarding pass.

    This works by replacing F + L into 0s and B + R into 1s.
    Then it's converting that string into a binary using int with the
    base code of 2.

    Args:
        boarding_pass (str): The boarding pass to get the seat id for.

    Returns:
        int: The seat id of the boarding pass.
    """
    return int(re.sub("[FL]", "0", re.sub("[BR]", "1", boarding_pass)), 2)


def get_seat_ids(boarding_passes):
    """Get the seat ids from the bordering passes.

    Args:
        boarding_passes (list): Each bording pass is a string.

    Returns:
        list: The seating ids from the boarding passes.
    """
    return list(map(get_seat_id, boarding_passes))


def get_highest_seat_id(seat_ids):
    """Get the highest seat id in the given boarding passes.

    Args:
        seat_ids (list): List of seat ids.

    Returns:
        int: Highest seat id.
    """

    return max(seat_ids)


def get_missing_seat_id(seat_ids):
    """Get missing seat id in list of boarding passes.

    Args:
        seat_ids (list): List of seat ids.

    Returns:
        int: The missing seat id.
    """
    minimum, maximum = min(seat_ids), max(seat_ids)

    missing = [s for s in range(minimum, maximum) if s not in seat_ids]
    return missing[0]


def main():
    """Print results for day 5."""
    boarding_passes = get_boarding_passes("./data_5.dat")
    seat_ids = get_seat_ids(boarding_passes)
    print(get_highest_seat_id(seat_ids))
    print(get_missing_seat_id(seat_ids))


if __name__ == '__main__':
    main()

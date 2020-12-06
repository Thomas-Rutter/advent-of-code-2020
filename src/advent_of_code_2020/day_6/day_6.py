"""Day 6 logic."""
from pathlib import Path


def get_groups(path):
    """Get the questionaire answers from the .dat file.

    Args:
        path (str): The path to the file to open.

    Returns:
        list: List of questionaries.
    """
    with open(Path(f"{path}"), "r") as read_file:
        return read_file.read().split("\n\n")


def get_count_of_group(group, any=True):
    """Get the count of answers from the group.

    If any is True then the total "different" chars will be counted.
    If any is False then the common characters that appear in all answers
    from the group will be counted.

    Args:
        group (str): The group to get the count of. Different people will be
            seperated by newlines.
        any (bool): Whether to count for anyone's answer or everyone's common
            answer. (default: {True})

    Returns:
        int: The count of the group.
    """
    if any:
        chars = set(group.replace("\n", ""))
    else:
        chars = set.intersection(*map(set, group.split("\n")))
    return len(chars)


def get_sum_of_counts(groups, any=True):
    """Get the sum count of all the groups.

    Args:
        groups (list): The list of groups, each group is a string.
        any (bool): Whether to count for anyone's answer or everyone's common
            answer. (default: {True})

    Returns:
        int: The sum count of the groups.
    """
    counts = []
    for group in groups:
        counts.append(get_count_of_group(group, any))
    return sum(counts)


def main():
    """Print results for day 6."""
    groups = get_groups("./data_6.dat")
    print(get_sum_of_counts(groups))
    print(get_sum_of_counts(groups, any=False))


if __name__ == '__main__':
    main()

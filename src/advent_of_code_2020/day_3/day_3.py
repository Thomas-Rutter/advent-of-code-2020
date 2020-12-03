"""Day 3 logic."""
from pathlib import Path


SLOPES = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


def get_geology():
    """Get the local geology from the .dat file.

    Returns:
        str: The geology of the open squares and trees.
    """
    data_file = Path("./data_3.dat")
    with open(data_file, "r") as read_file:
        geology = read_file.read()

    return geology


def get_number_of_encountered_trees(geology, right, down):
    """Get the number of trees we would encounter in the given geology.

    The right and down parameters state how we are moving through the geology.

    Args:
        geology (str): Geology of area.
        right (int): The amount to move right.
        down (int): The amount to move down.

    Returns:
        int: The amount of trees we encounter.
    """
    encountered_trees = 0
    lines = geology.splitlines()
    line_length = len(lines[0])
    x_pos, y_pos = 0, 0
    while y_pos < len(lines):
        current_line = lines[y_pos]
        encountered_trees += current_line[x_pos % line_length] == "#"

        x_pos += right
        y_pos += down

    return encountered_trees


def get_multiplied_number_of_encountered_trees(geology, slopes):
    """Get the total number of trees we would encounter in the given geology.

    Args:
        geology (str): Geology of area.
        slopes (list): tuples of the right and down parameters to use.

    Returns:
        int: The total amount of possible trees we encounter.
    """
    results = []
    for slope in slopes:
        encountered_trees = get_number_of_encountered_trees(
            geology, slope[0], slope[1]
        )
        results.append(encountered_trees)

    multiplied_trees = 1
    for result in results:
        multiplied_trees = multiplied_trees * result

    return multiplied_trees


def main():
    """Print results for day 3."""
    geology = get_geology()
    print(get_number_of_encountered_trees(geology, 3, 1))
    print(get_multiplied_number_of_encountered_trees(geology, SLOPES))


if __name__ == '__main__':
    main()

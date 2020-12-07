"""Day 6 logic."""
import networkx as nx
from pathlib import Path


def get_rules(path):
    """Get the rules from the .dat file.

    Args:
        path (str): The path to the file to open.

    Returns:
        dict: dictionary of rules.
    """
    with open(Path(f"{path}"), "r") as read_file:
        rules_list = [line.strip().split() for line in read_file.readlines()]
    rules = {}
    for rule in rules_list:
        parent = f"{rule[0]}_{rule[1]}"
        index = 4
        contains = []
        while index < len(rule) and rule[index] != "no":
            count = int(rule[index])
            child = f"{rule[index + 1]}_{rule[index + 2]}"
            contains.append((count, child))
            index += 4
        rules[parent] = contains
    return rules


def get_number_of_bags_eventually_containing(rules):
    """Get the number of bags that will eventually contain "shiny_gold".

    This is done by creating a networkx graph.

    We iterate over the rules and for each bag the rule is for we get the
    "child" bags for that rule and create an edge between the "parent" bag
    and the "child" bag. This makes sure there is a node for all the bags
    and that the bags have all the connections for that bag.

    Then we use networkx.predecessor() to find all the bags that will
    eventually have "shiny_gold" as a child. We minus from this as the
    "shiny_gold" bag itself will be included.

    Args:
        rules (dict): The rules to graph.

    Returns:
        int: The number of bags that will eventually contain "shiny_gold".
    """
    graph = nx.DiGraph()
    for parent, contains in rules.items():
        for _, child in contains:
            graph.add_edge(child, parent)

    return len(nx.predecessor(graph, "shiny_gold")) - 1


def get_bags(rules, colour):
    """Get the number of bags that will be inside the given colour bag.

    This recursive function works by getting the count of the parent bag,
    then for each of the children bags, running this function to get their
    count and so on. One will be added to this sum to make sure the given
    bag is also counted.

    Args:
        rules (dict): The rules to iterate over.
        colour (str): The bag to check the contents of.

    Returns:
        int: The number of bags inside the given bag.
    """
    return sum([
        1,
        sum(
            count * get_bags(rules, child) for count, child in rules[colour]
        )
    ])


def main():
    """Print results for day 6."""
    rules = get_rules("./data_7.dat")
    print(get_number_of_bags_eventually_containing(rules))
    # print(get_bags(rules, "shiny_gold") - 1)


if __name__ == '__main__':
    main()

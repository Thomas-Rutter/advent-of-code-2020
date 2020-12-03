"""Day 1 logic."""
from pathlib import Path


def get_expense_report():
    """Get the expense report from the .dat file.

    Returns:
        list: Expense report.
    """
    expense_report = []
    data_file = Path("./data_1.dat")
    with open(data_file, "r") as read_file:
        values = read_file.readlines()
    for value in values:
        expense_report.append(int(value))

    return expense_report


def expense_report_multiplier_2_numbers(expense_report):
    """Find multiple of two numbers that add up to 2020.

    Args:
        expense_report (list): The expense report

    Returns:
        int: The numbers multiplied together.
    """
    for index, number_1 in enumerate(expense_report):
        for number_2 in expense_report[index+1:]:
            if (number_1 + number_2) == 2020:
                result = (number_1 * number_2)
                return result


def expense_report_multiplier_3_numbers(expense_report):
    """Find multiple of three numbers that add up to 2020.

    Args:
        expense_report (list): The expense report

    Returns:
        int: The numbers multiplied together.
    """
    for index, number_1 in enumerate(expense_report):
        for second_index, number_2 in enumerate(expense_report[index+1:]):
            for number_3 in expense_report[second_index+1:]:
                if (number_1 + number_2 + number_3) == 2020:
                    result = (number_1 * number_2 * number_3)
                    return result


def main():
    """Print results for day 1."""
    expense_report = get_expense_report()
    two_numbers_results = expense_report_multiplier_2_numbers(expense_report)
    three_numbers_results = expense_report_multiplier_3_numbers(expense_report)
    print(two_numbers_results)
    print(three_numbers_results)


if __name__ == '__main__':
    main()

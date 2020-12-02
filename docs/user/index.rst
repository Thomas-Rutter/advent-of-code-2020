Advent of Code 2020 User Documentation
======================================

Overview
--------

Repo for Advent of Code 2020

https://adventofcode.com/2020

Day 1
-----

The issue to solve on this day was:

.. code-block:: text

    In a given list, find the two entries that sum to 2020 and then multiply those two numbers together.

The story behind this the accountant elves need you to sort out the expense report.

Step 1 was just saving the list as a data_1.dat file, and reading that in.

.. code-block:: python

    def get_expense_report():
        """Get the expense report from .dat file.

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


So for this I just used a nested for loop setup. For Loop 1, we'll name him Terry,
enumerated over the list. This gave us a value (number 1) and the index of that value.

Then in the second for loop, we'll name him Jim, I just used the index so Jim
would loop over the list as well but not use numbers that Terry had already used.#
And Jim went over the list to give use number_2.

Then it was just a case of adding number_1 and number_2, if they equal 2020
then return the value of them being multiplied together.

This seemed to do the trick and made sure that we didn't do any unnecessary
loops, which is always nice.

.. code-block:: python

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

Then there was a second part to the issue, which was:

.. code:: text

    In a given list, find the three entries that sum to 2020 and then multiply those two numbers together.

So yeah doesn't that sound oddly familiar?

Well for this I just made Jim use enumerate, created a third for loop (Phil) to
give use number_3, and made the code add the three numbers together and see if
they sum up to 2020.

.. code-block:: python

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

Was a pretty fun little challenge, admittedly spent more time setting up the
repo structure and the tests setup!

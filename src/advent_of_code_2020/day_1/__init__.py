"""Day 1 of advent of code."""
import unittest

from advent_of_code_2020.day_1 import day_1

TEST_LIST = [
    1721,
    979,
    366,
    299,
    675,
    1456,
]


class TestDay1(unittest.TestCase):
    """Test Class for advent_of_code_2020."""

    def test_part_1(self):
        """Test part 1 of day 1."""
        self.assertEqual(
            day_1.expense_report_multiplier_2_numbers(TEST_LIST),
            514579
        )

    def test_part_2(self):
        """Test part 2 of day 1."""
        self.assertEqual(
            day_1.expense_report_multiplier_3_numbers(TEST_LIST),
            241861950
        )


if __name__ == '__main__':
    unittest.main()

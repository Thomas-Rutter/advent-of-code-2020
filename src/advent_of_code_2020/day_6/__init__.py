"""Day 6 of advent of code."""
import unittest

from advent_of_code_2020.day_6 import day_6


TEST_LIST = ['abc', 'a\nb\nc', 'ab\nac', 'a\na\na\na', 'b']


class TestDay6(unittest.TestCase):
    """Test Class for advent_of_code_2020 day 6."""

    def test_part_1(self):
        """Test part 1 of day 6."""
        self.assertEqual(
            day_6.get_sum_of_counts(TEST_LIST),
            11
        )

    def test_part_2(self):
        """Test part 2 of day 6."""
        self.assertEqual(
            day_6.get_sum_of_counts(TEST_LIST, any=False),
            6
        )


if __name__ == '__main__':
    unittest.main()

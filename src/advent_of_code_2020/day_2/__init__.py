"""Day 1 of advent of code."""
import unittest

from advent_of_code_2020.day_2 import day_2

TEST_DICT = {
    "1-3 a": ["abcde"],
    "1-3 b": ["cdefg"],
    "2-9 c": ["ccccccccc"]
}


class TestDay1(unittest.TestCase):
    """Test Class for advent_of_code_2020."""

    def test_part_1(self):
        """Test part 1 of day 1."""
        self.assertEqual(
            day_2.get_valid_passwords_policy_one(TEST_DICT),
            2
        )

    def test_part_2(self):
        """Test part 1 of day 1."""
        self.assertEqual(
            day_2.get_valid_passwords_policy_two(TEST_DICT),
            1
        )


if __name__ == '__main__':
    unittest.main()

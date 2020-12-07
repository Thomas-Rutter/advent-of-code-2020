"""Day 7 of advent of code."""
import unittest
from unittest import mock

from advent_of_code_2020.day_7 import day_7


TEST_STR_1 = (
    "light red bags contain 1 bright white bag, 2 muted yellow bags.\n" +
    "dark orange bags contain 3 bright white bags, 4 muted yellow bags.\n" +
    "bright white bags contain 1 shiny gold bag.\n" +
    "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.\n" +
    "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.\n" +
    "dark olive bags contain 3 faded blue bags, 4 dotted black bags.\n" +
    "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.\n" +
    "faded blue bags contain no other bags.\n" +
    "dotted black bags contain no other bags.\n"
)

TEST_STR_2 = (
    "shiny gold bags contain 2 dark red bags.\n" +
    "dark red bags contain 2 dark orange bags.\n" +
    "dark orange bags contain 2 dark yellow bags.\n" +
    "dark yellow bags contain 2 dark green bags.\n" +
    "dark green bags contain 2 dark blue bags.\n" +
    "dark blue bags contain 2 dark violet bags.\n" +
    "dark violet bags contain no other bags.\n"
)


class TestDay7(unittest.TestCase):
    """Test Class for advent_of_code_2020 day 7."""

    def get_rules(self, TEST_STR):
        read_data = TEST_STR
        mock_open = mock.mock_open(read_data=read_data)
        with mock.patch("builtins.open", mock_open):
            rules = day_7.get_rules("blah")
        return rules

    def test_part_1(self):
        """Test part 1 of day 7."""
        rules = self.get_rules(TEST_STR_1)
        self.assertEqual(
            day_7.get_number_of_bags_eventually_containing(rules),
            4
        )

    def test_part_2(self):
        """Test part 2 of day 7."""
        rules = self.get_rules(TEST_STR_2)
        self.assertEqual(
            day_7.get_bags(rules, "shiny_gold") - 1,
            126
        )


if __name__ == '__main__':
    unittest.main()

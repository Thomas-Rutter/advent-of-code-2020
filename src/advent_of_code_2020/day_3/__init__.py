"""Day 3 of advent of code."""
import unittest

from advent_of_code_2020.day_3 import day_3

TEST_TREES = (
    "..##.......\n" +
    "#...#...#..\n" +
    ".#....#..#.\n" +
    "..#.#...#.#\n" +
    ".#...##..#.\n" +
    "..#.##.....\n" +
    ".#.#.#....#\n" +
    ".#........#\n" +
    "#.##...#...\n" +
    "#...##....#\n" +
    ".#..#...#.#\n"
)

SLOPES = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2],
]


class TestDay3(unittest.TestCase):
    """Test Class for advent_of_code_2020 day 3."""

    def test_part_1(self):
        """Test part 1 of day 3."""
        self.assertEqual(
            day_3.get_number_of_encountered_trees(TEST_TREES, 3, 1),
            7
        )

    def test_part_2(self):
        """Test part 2 of day 3."""
        self.assertEqual(
            day_3.get_multiplied_number_of_encountered_trees(
                TEST_TREES, SLOPES
            ),
            336
        )


if __name__ == '__main__':
    unittest.main()

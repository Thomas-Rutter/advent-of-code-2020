"""Day 5 of advent of code."""
import unittest

from advent_of_code_2020.day_5 import day_5


TEST_LIST = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]


class TestDay5(unittest.TestCase):
    """Test Class for advent_of_code_2020 day 5."""

    def test_part_1(self):
        """Test part 1 of day 5."""
        seat_ids = day_5.get_seat_ids(TEST_LIST)
        self.assertEqual(
            day_5.get_highest_seat_id(seat_ids),
            820
        )

    def test_part_2(self):
        """Test part 2 of day 5."""
        boarding_passes = day_5.get_boarding_passes(
            "src/advent_of_code_2020/day_5/data_5.dat"
        )
        seat_ids = day_5.get_seat_ids(boarding_passes)
        self.assertEqual(
            day_5.get_missing_seat_id(seat_ids),
            711
        )


if __name__ == '__main__':
    unittest.main()

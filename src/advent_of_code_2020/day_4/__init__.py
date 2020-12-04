"""Day 4 of advent of code."""
import unittest

from advent_of_code_2020.day_4 import day_4


TEST_PASSPORTS = [
    {
        'byr': '1937',
        'cid': '147',
        'ecl': 'gry',
        'eyr': '2020',
        'hcl': '#fffffd',
        'hgt': '183cm',
        'iyr': '2017',
        'pid': '860033327',
    },
    {
        'byr': '1929',
        'cid': '350',
        'ecl': 'amb',
        'eyr': '2023',
        'hcl': '#cfa07d',
        'iyr': '2013',
        'pid': '028048884',
    },
    {
        'byr': '1931',
        'ecl': 'brn',
        'eyr': '2024',
        'hcl': '#ae17e1',
        'hgt': '179mm',
        'iyr': '2013',
        'pid': '760753108',
    },
    {
        'ecl': 'brn',
        'eyr': '2025',
        'hcl': '#cfa07d',
        'hgt': '59in',
        'iyr': '2011',
        'pid': '166559648',
    }
]


class TestDay4(unittest.TestCase):
    """Test Class for advent_of_code_2020 day 4."""

    def test_part_1(self):
        """Test part 1 of day 4."""
        self.assertEqual(
            day_4.get_number_of_valid_passports(
                TEST_PASSPORTS, criteria=False),
            2
        )

    def test_part_2(self):
        """Test part 2 of day 4."""
        self.assertEqual(
            day_4.get_number_of_valid_passports(TEST_PASSPORTS),
            1
        )


if __name__ == '__main__':
    unittest.main()

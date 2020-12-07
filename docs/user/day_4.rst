Day 4
=====

So we are hacking an airports security system and making changes just because
we don't have a passport apparently.

We are given a giant file that is a list of passports. The passports are
seperated by a blank line, then I just seperate the fields using regex to split
on newlines or spaces. Then I just construct the passport dictionary with the
fields. All the criteria will be strings in the dict as I can't be bothered
doing validation at the "get the puzzle input into the script" stage.

.. code-block:: python

    def get_passports():
        """Get the passports from the .dat file.

        Returns:
            list: List of passports as dictionaries.
        """
        passports = []
        data_file = Path("./data_4.dat")
        with open(data_file, "r") as read_file:
            passport_strs = read_file.read().split("\n\n")

        for passport_str in passport_strs:
            fields = re.split(" |\n", passport_str)
            passport = {}
            for field in fields:
                split = field.split(":")
                passport[split[0]] = split[1]
            passports.append(passport)

        return passports

Now we've got the list of dictionaries, it's a case of creating a validation
system so that the passport dictionaries have the required keys.

Part 1
------
This was super easy, which was nice. It was just a case of getting the keys
of the passport, get the keys that appear in both the required_keys list and
the list of passport keys. Then check those common_keys are the same are the
required keys. This makes sure the optional key "cid" can stil yield a valid
result.

.. code-block:: python

    def is_valid_passport(passport):
        """Return whether passport is valid or not.

        Args:
            passport (dict): The passport dict to check.

        Returns:
            bool: True if passport is valid, false if invalid passport.
        """
        required_keys = [
            "byr",
            "ecl",
            "eyr",
            "hcl",
            "hgt",
            "iyr",
            "pid",
        ]

        passport_keys = passport.keys()

        common_keys = set(passport_keys).intersection(required_keys)

        if set(common_keys) == set(required_keys):
            valid = True
        else:
            valid = False

        return valid

Part 2
------

As soon as this challenge started I guessed the second part would be making
some kind of validation for the different fields.

I specified the criteria for each key in a "CRITERIA" constant.

For the "byr", "iyr", and "eyr" fields, it was just making sure they are in the
correct range.

For the "hgt" field it was a case of parsing the string to get the unit
type and then making sure the measurement was in the right range for that unit.
Using try and except to stop any really invalid measurements from breaking the
script.

For the "ecl" field it was just checking the passport's "ecl" value was in the
list of valid eye colours.

For the "hcl" field it was just checking the the value against a regex pattern.

For the "pid" field it was making sure the value was numeric and it's length
was the length specified in the criteria.


.. code-block:: python

    CRITERIA = {
        "byr": range(1920, 2003),
        "iyr": range(2010, 2021),
        "eyr": range(2020, 2031),
        "hgt": {
            "cm": range(150, 194),
            "in": range(59, 77)
        },
        "hcl": r"#[0-9a-f]{6}",
        "ecl": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
        "pid": 9,
    }

    def check_range_criteria(passport):
        """Check the criterion with ranges are valid or not.

        Args:
            passport (dict): The passport to check

        Returns:
            bool: True if the criterion are valid.
        """
        checks = []
        for key in ["byr", "iyr", "eyr"]:
            try:
                if int(passport[key]) not in CRITERIA[key]:
                    checks.append(False)
            except ValueError:
                checks.append(False)
        return all(checks)


    def check_height_criteria(passport):
        """Check the height criteria is valid or not.

        Args:
            passport (dict): The passport to check

        Returns:
            bool: True if the height criteria is valid.
        """
        checks = []
        try:
            unit = passport["hgt"][-2:]
            if unit not in CRITERIA["hgt"].keys():
                checks.append(False)
            if int(passport["hgt"][:-2]) not in CRITERIA["hgt"][unit]:
                checks.append(False)
        except (KeyError, ValueError):
            checks.append(False)
        return all(checks)


    def is_valid_passport(passport, criteria=True):
        """Return whether passport is valid or not.

        Args:
            passport (dict): The passport dict to check.
            criteria (bool): Whether to validate criteria data. (default: {True})

        Returns:
            bool: True if passport is valid, false if invalid passport.
        """
        valid = []
        required_keys = [
            "byr",
            "ecl",
            "eyr",
            "hcl",
            "hgt",
            "iyr",
            "pid",
        ]

        passport_keys = passport.keys()

        common_keys = set(passport_keys).intersection(required_keys)

        if set(common_keys) == set(required_keys):
            if criteria:
                valid.append(check_range_criteria(passport))

                valid.append(passport["ecl"] in CRITERIA["ecl"])

                valid.append(re.search(CRITERIA["hcl"], passport["hcl"]))

                valid.append(all([
                    passport["pid"].isnumeric(),
                    len(passport["pid"]) == CRITERIA["pid"]
                ]))

                valid.append(check_height_criteria(passport))
            else:
                valid = [True]
        else:
            valid = [False]

        return all(valid)

The main thing I learnt from this was a way of organising the different checks
in a way that I think still looks clear and concise.
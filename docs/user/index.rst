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

    In a given list, find the two entries that sum to 2020 and then multiply
    those two numbers together.

The story behind this is that the accountant elves need you to sort out
the expense report. You'd think as accountants they would be able to sort
it out themselves but I guess not.

Step 1 was just saving the list as a data_1.dat file, and reading that in.

.. code-block:: python

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

Part 1
******

So for this I just used a nested for loop setup. For Loop 1, we'll
name him Terry, enumerated over the list. This gave us a value (number 1)
and the index of that value.

Then in the second for loop, we'll name him Jim, I just used the index so Jim
would loop over the list as well but not use numbers that Terry
had already used. And Jim went over the list to give use number_2.

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

Part 2
******

Then there was a second part to the issue, which was:

.. code:: text

    In a given list, find the three entries that sum to 2020 and
    then multiply those three numbers together.

So yeah doesn't that sound oddly familiar?

Well for this I just made Jim use enumerate, created a third for loop (Phil) to
give us number_3, and made the code add the three numbers together and see if
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


Day 2
-----

Another day, another set of issues to solve.
First up:

.. code-block:: text

    In a list of passwords, find the amount of "valid" passwords.
    Each item in the list has two parts, the criteria and the password itself.
    The criteria indicates the lowest and highest number of times a given
    letter must appear for the password to be valid.

    A password item would look like:
    1-3 a: abcde

And the story behind this is the shopkeeper at the "North Pole Toboggan
Rental Shop" is having a bad day and their password database is corrupt.
So we have to figure out how many passwords are valid in the list they
have given us.

So step one was bring in the list! Now I don't know about you, but that
password item looks A LOT like a dictionary item, so I decided to format
the passwords into a dictionary, with the criteria as the key
and the passwords with that criteria in a list as the value.

.. code-block:: python

    def get_passwords():
        """Get the passwords from the .dat file.

        Returns:
            dict: Policy criteria as key and passwords in a list as value.
        """
        passwords = {}
        data_file = Path("./data_1.dat")
        with open(data_file, "r") as read_file:
            values = read_file.read().splitlines()
        for value in values:
            split = value.split(": ")
            if split[0] in passwords:
                passwords[split[0]].append(split[1])
            else:
                passwords[split[0]] = [split[1]]

        return passwords

Cool now that we have the passwords, let's figure out how many valid
passwords we have!

Part 1
******

So for iterating over the passwords I just did a for loop over the
dictionary's items, then a for loop over the values list to check all
passwords for a certain criteria.

Next step was parsing the criteria string, for this I just used split() to
format the string. Then it was just an if statement to see if the password
was valid based on the criteria. If it was valid then just add 1 to an
int variable I created at the start of the function.

.. code-block:: python

    def get_valid_passwords_policy_one(passwords):
        """Get valid passwords.

        A valid password is one that contains the letter in the criteria for
        at least the minimum amount and no more than the maximum amount.
        The min and max amounts are also defined in the criteria.

        The criteria is the key, the passwords with that criteria
        are in a list as the value.

        Args:
            passwords: Dictionary of passwords, policy criteria as key
                and passwords in a list as value.

        Returns:
            int: The amount of valid passwords for this policy.
        """
        valid_passwords = 0
        for criteria, values in passwords.items():
            for password in values:
                minimum = int(criteria.split("-")[0])
                maximum = int(criteria.split("-")[1].split(" ")[0])
                letter = criteria.split("-")[1].split(" ")[1]
                if minimum <= password.count(letter) <= maximum:
                    valid_passwords += 1

        return valid_passwords

This seemed to work well, I'm gonna assume there is a more visually pleasing
way of doing the criteria parsing BUT this does the trick and it's pretty
explicit about what's happening.

Part 2
******

So this shopkeeper is clearly not the sharpest tool in the shed as apparently
that password policy was for the sled rental place he used to work at!

The correct policy is:

.. code-block:: text

    Each policy actually describes two positions in the password,
    where 1 means the first character, 2 means the second character,
    and so on. (Be careful; Toboggan Corporate Policies have no concept of
    "index zero"!) Exactly one of these positions must contain the given
    letter. Other occurrences of the letter are irrelevant for the purposes
    of policy enforcement.

So this doesn't really require much change from the first function,
step one is rename the variables, minimum will now be "first_position"
and maximum will now be "second_position". Then it's a case of subtracting
1 from the int variables so they work with having index zero be a thing.

Then it's just making a conditions list and setting up an if statement
to accept if only one of the conditions is met. Then it's the same adding
to the valid_passwords int var if that if statement is met.

.. code-block:: python

    def get_valid_passwords_policy_two(passwords):
        """Get valid passwords.

        A valid password is one that contains the letter in the criteria at
        either the first position or the second position, not both.
        The positions are also defined in the criteria. These policies have
        no concept of index zero so position 1 would be the first position,
        not the second.

        The criteria is the key, the passwords with that criteria
        are in a list as the value.

        Args:
            passwords: Dictionary of passwords, policy criteria as key
                and passwords in a list as value.

        Returns:
            int: The amount of valid passwords for this policy.
        """
        valid_passwords = 0
        for criteria, values in passwords.items():
            for password in values:
                first_position = int(criteria.split("-")[0]) - 1
                second_position = int(criteria.split("-")[1].split(" ")[0]) - 1
                letter = criteria.split("-")[1].split(" ")[1]
                conditions = [
                    password[first_position] == letter,
                    password[second_position] == letter,
                ]
                if any(conditions) and not all(conditions):
                    valid_passwords += 1

        return valid_passwords

And that's day 2 done! This was a nice little challenge and woo I got two
more gold stars!


Day 3
-----

The one that made me learn about modulo.
First up:

.. code-block:: text

    In a given "geology", with trees represented by "#"s and open squares
    represented by "."s, figure out how many trees you'll encounter with the
    path you are taking. You are only able to move in the same repeating
    pattern, like 3 to the right and 1 down. The geology repeats to the right
    many times.

    The geology would look like:
    ..##.......
    #...#...#..
    .#....#..#.
    ..#.#...#.#
    .#...##..#.
    ..#.##.....

And the story behind this is you are on ya cheap toboggan which has just
the weirdest steering and you don't want to hit that many trees.

As the geology is just a big string, I didn't need to do anything fancy
when reading it into the script.

Part 1
******

For the first part we were told that our movement is 3 to the right and 1 down,
then we had to figure out how many trees we'd encounter (land on) by the time
we reach the end of the geology.

So step 1 was setting up a while loop so when our y position was greater than
the amount of lines we'd be done. Before that loop I split the geology into
lines, set the encountered_trees, x_pos and y_pos variables to 0, and got the
length of the lines.

Then, in the loop, it was a case of setting the current_line using the y_pos
and seeing if we landed on a tree. If we landed on a tree we add that to the
encountered_trees int.

I used modulo to make sure if the x_pos went pass the line_length it would
loop back around, then it was just does that index on the
current_line equal "#"

.. code-block:: python

    def get_number_of_encountered_trees(geology, right, down):
        """Get the number of trees we would encounter in the given geology.

        The right and down parameters state how we are moving through the geology.

        Args:
            geology (str): Geology of area, "#" are trees.
            right (int): The amount to move right.
            down (int): The amount to move down.

        Returns:
            int: The amount of trees we encounter.
        """
        encountered_trees = 0
        lines = geology.splitlines()
        line_length = len(lines[0])
        x_pos, y_pos = 0, 0
        while y_pos < len(lines):
            current_line = lines[y_pos]
            encountered_trees += current_line[x_pos % line_length] == "#"

            x_pos += right
            y_pos += down

        return encountered_trees

Was pretty happy with this and learning how to use modulo was handy!
Totally didn't do some stupid "if x_pos is greater than line_length then x_pos
now equals x_pos minus line_lenght" logic before finding out I can just use %.

Part 2
******

So despite the naming making very little sense, we know we need to
check all "slopes". Each slope is just the movement pattern we take.
Again the naming makes no sense. The slopes (patterns) are:

.. code-block:: text

    Right 1, down 1.
    Right 3, down 1. (This is the slope from part 1.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.

So for each slope, we want to get the amount of trees we'd encounter
and then multiple the trees together. So in the example geology, using
those slopes we encountered: 2, 7, 3, 4, and 2 trees, we then multiplied those numbers together to get 336.

So to calculate this it was just a case of for each slope, I pass the
pattern to the get_number_of_encountered_trees() function and append
the result into a list.

Once we've got all the results, it's just a case of multiplying them together and boom our 6th gold star!

.. code-block:: python

    def get_multiplied_number_of_encountered_trees(geology, slopes):
        """Get the total number of trees we would encounter in the given geology.

        Args:
            geology (str): Geology of area.
            slopes (list): tuples of the right and down parameters to use.

        Returns:
            int: The total amount of possible trees we encounter.
        """
        results = []
        for slope in slopes:
            encountered_trees = get_number_of_encountered_trees(
                geology, slope[0], slope[1]
            )
            results.append(encountered_trees)

        multiplied_trees = 1
        for result in results:
            multiplied_trees = multiplied_trees * result

        return multiplied_trees

This was the first time I've dealt with grid stuff and using the modulo
operator in python so I'm pretty happy with how it turned out!

Day 4
-----

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
******
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
******

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


Day 5
-----

So we are now on our plane but apparently we have dropped our boarding
pass. Due to not having our boarding pass, we have no idea which seat
is ours. Luckily though we are able to quickly scan everyone else's
boarding passes, so we can figure out our seat by the process of
elimination.

Now here's the real kicker, clearly whoever decided on this boarding
pass format was a giant nerd who was taking the piss but somehow
their idea got used. So instead of the boarding pass saying something
like "46A" it says "FBFBBFFRLR", told you it was clearly a
stupid format.

.. code-block:: text

    The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.

    For example, consider just the first seven characters of FBFBBFFRLR:

    - Start by considering the whole range, rows 0 through 127.
    - F means to take the lower half, keeping rows 0 through 63.
    - B means to take the upper half, keeping rows 32 through 63.
    - F means to take the lower half, keeping rows 32 through 47.
    - B means to take the upper half, keeping rows 40 through 47.
    - B keeps rows 44 through 47.
    - F keeps rows 44 through 45.
    The final F keeps the lower of the two, row 44.
    The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half.

    For example, consider just the last 3 characters of FBFBBFFRLR:

    - Start by considering the whole range, columns 0 through 7.
    - R means to take the upper half, keeping columns 4 through 7.
    - L means to take the lower half, keeping columns 4 through 5.
    - The final R keeps the upper of the two, column 5.
    So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

    Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.

So we are given a huge list of these boarding passes. It was just a
case of using readlines() to create the list of boarding passes.

Part 1
******

So for the first part it's just a case of making it so I can
actually get the seat ids from the boarding passes. Then getting the
highest seat id.

So step 1 was get the seat id from a single boarding pass. Now my first process
was just going through the string and spliting a range based on the character.

But then I found out that if you replace F + L with 0 and B + R with 1 then
you actually just get the seat id in binary form, then it's just converting
that binary to decimal using int(binary_number, 2). This was shockingly easy
and I imagine this is what I was meant to realise when it said the seat_id was
the row * 8 + the column. But very new to binary to I only came across this
when on the subreddit. Relatively sure I understand it but little confused on
how the column * 8 + row bit shows how it's just binary...

But once we have the function to get the seat_id from a boarding pass, it's
just using the map() function to get all the seat_ids from the boarding passes.
Then I just ran max() on that list to get the highest seat_id.

.. code-block:: python

    def get_seat_id(boarding_pass):
        """Return the seat id from the boarding pass.

        This works by replacing F + L into 0s and B + R into 1s.
        Then it's converting that string into a binary using int with the
        base code of 2.

        Args:
            boarding_pass (str): The boarding pass to get the seat id for.

        Returns:
            int: The seat id of the boarding pass.
        """
        return int(re.sub("[FL]", "0", re.sub("[BR]", "1", boarding_pass)), 2)


    def get_seat_ids(boarding_passes):
        """Get the seat ids from the bordering passes.

        Args:
            boarding_passes (list): Each bording pass is a string.

        Returns:
            list: The seating ids from the boarding passes.
        """
        return list(map(get_seat_id, boarding_passes))


    def get_highest_seat_id(seat_ids):
        """Get the highest seat id in the given boarding passes.

        Args:
            seat_ids (list): List of seat ids.

        Returns:
            int: Highest seat id.
        """

        return max(seat_ids)

Honestly that "discovery" of the binary thing really made this a super easy
task.

Part 2
******

Now we have all the seat ids, it's just a case of finding the missing seat_id!

For this I just got the minimum seat_id and the maximum seat_id in the list,
and then did a list comprehension to go through all the seat_ids in that range
and if any id wasn't in the list of seat_ids then that's our seat!

.. code-block:: python

    def get_missing_seat_id(seat_ids):
        """Get missing seat id in list of boarding passes.

        Args:
            seat_ids (list): List of seat ids.

        Returns:
            int: The missing seat id.
        """
        minimum, maximum = min(seat_ids), max(seat_ids)

        missing = [s for s in range(minimum, maximum) if s not in seat_ids]
        return missing[0]

When I first read this challenge I was a bit like "Oh God this is gonna be a
lot of if statements isn't it?", I am very pleased that it turned out to just
be a binary conversion for the most part as it showed me that if the
description mentions "binary space partitioning" then converting things
to binary is probably gonna yield the most simple solution.

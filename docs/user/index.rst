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

Day 2
=====

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
------

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
------

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
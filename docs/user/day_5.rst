Day 5
=====

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
------

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
------

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

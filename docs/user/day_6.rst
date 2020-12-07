Day 6
=====

So first we scanned everyone's boarding passes and now we are going through
everyone's customs declaration forms, I really think people shouldn't be so
freely giving us all their information...

So yeah we now have every group's answers to their forms. The forms have 26
yes-or-no questions marked `a` though `z`. If a letter appears in the answers
then it means that person has answered "yes" to that question. The answers
for each person will be on one line and groups are separated by a blank line.

.. code-block:: text

    abc

    a
    b
    c

    ab
    ac

    a
    a
    a
    a

    b

I just read this and split on the blank line (\n\n) to get a list
of the groups, which each group just being a string.

Now we just need to evaluate these answers!

Part 1
------

So part 1 requires us to count the answers for each group and get the sum
total for all groups. We are only counting the first instance of an answer,
so duplicate answers in a group don't count.

So this sounds like an ideal use case for sets if you ask me! So all I did
for this was remove the newline characters in the group's string and then
set-ify that string so each character became and item and any duplicate
items were removed, then it was just using len() to get the count for that
set. Then I just returned that count to a list and once we had "counted"
all the groups, I just ran sum() on that count list to get the total!

.. code-block:: python

    def get_count_of_group(group):
        """Get the count of answers from the group.

        Args:
            group (str): The group to get the count of. Different people will be
                seperated by newlines.

        Returns:
            int: The count of the group.
        """
        return len(set(group.replace("\n", "")))


    def get_sum_of_counts(groups):
        """Get the sum count of all the groups.

        Args:
            groups (list): The list of groups, each group is a string.

        Returns:
            int: The sum count of the groups.
        """
        counts = []
        for group in groups:
            counts.append(get_count_of_group(group, any))
        return sum(counts)

Part 2
------

So for part 2, it's the same count thing as part 1 but we need to count all
the common answers in a group, not just every answer. For this it was a case
of splitting the group up so we had a string per person, I used map() to turn
each person's string into a set in the group, then used set.intersection()
to get the common answers that appeared in that group.

.. code-block:: python

    def get_count_of_group(group, any=True):
        """Get the count of answers from the group.

        If any is True then the total "different" chars will be counted.
        If any is False then the common characters that appear in all answers
        from the group will be counted.

        Args:
            group (str): The group to get the count of. Different people will be
                seperated by newlines.
            any (bool): Whether to count for anyone's answer or everyone's common
                answer. (default: {True})

        Returns:
            int: The count of the group.
        """
        if any:
            chars = set(group.replace("\n", ""))
        else:
            chars = set.intersection(*map(set, group.split("\n")))
        return len(chars)


    def get_sum_of_counts(groups, any=True):
        """Get the sum count of all the groups.

        Args:
            groups (list): The list of groups, each group is a string.
            any (bool): Whether to count for anyone's answer or everyone's common
                answer. (default: {True})

        Returns:
            int: The sum count of the groups.
        """
        counts = []
        for group in groups:
            counts.append(get_count_of_group(group, any))
        return sum(counts)

This was a nice change of pace from the yesterday's challenge, was just using
sets and map, which I already knew about so no having to look up binary stuff
today!

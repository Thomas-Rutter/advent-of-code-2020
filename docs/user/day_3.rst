Day 4
=====

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
------

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
------

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

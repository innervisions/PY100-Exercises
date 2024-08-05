def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

find_first_nonzero_among([0, 0, 1, 0, 2, 0])
find_first_nonzero_among([1])

# Line 6 raises an error because find_first_nonzero_among
# expects a single argument, yet is invoked with 6. We can fix this
# by changing the arguments to a single list argument.

# On line 7 a different error is raised because the integer argument
# is not iterable. This can be fixed by changing to a single element list.

""" Python program for implementation of different types of recursion."""


def recursive(input):
    """ Apply n of steps corresponding to the argument input.
    Replace return with print to output the steps.
    Time Complexity O(n)"""

    # Base Case: Argument input greater than 0.
    if input <= 0:
        return 0
    else:
        output = recursive(input - 1)
        print(output)


def get_fib(position):
    """A recursive function that represents the Fibonacci Sequence, takes
    position and return its value within the Fibonacci Sequence.
    Time Complexity O(n)"""

    # Base Case: Positions greater thatn 0 or 1, since Fibonacci for 0 is 0 and
    # 1 is 1.
    if position == 0 or position == 1:
        return position

    return get_fib(position - 1) + get_fib(position - 2)

def recursive(input):
    # Base case
    if input <= 0:
        return 0
    else:
        output = recursive(input - 1)
        return output


def get_fib(position):
    """A recusrsive function to represetn the Fibonacci Sequence.
    Time Complexity O(n)"""

    # Base case
    if position == 0 or position == 1:
        return position

    return get_fib(position - 1) + get_fib(position - 2)

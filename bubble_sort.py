""" Python program for implementation of Bubble Sort."""


def bubble_sort(arr):
    """ Time Complexity O(n ** 2)"""

    n = len(arr)

    # NOTE: Not mandatory for Bubble Sort, will be used within the code for the
    # feedback messages to show the steps during execustion, Thus deleting will
    # cause ERROR.
    outer_loop_result = 0
    inner_loop_result = 0

    # Outer loop, loop over all elements in the array.
    for outer_loop in range(n):
        outer_loop_result += 1
        inner_loop_result = 0
        print(f"Result: {outer_loop_result} ==> {arr}")

        # Inner loop.
        # Loop is (n - 2) to avoid index out of range when swap last two elements.
        for inner_loop in range(n - outer_loop - 1):
            # If left element greater than its next element, swap them.
            if arr[inner_loop] > arr[inner_loop + 1]:
                arr[inner_loop],
                arr[inner_loop + 1] = arr[inner_loop + 1], arr[inner_loop]

            # Feedback message.
            inner_loop_result += 1
            print(f"    Inner: {inner_loop_result} ==> {arr}")


arr = [5, 3, 1, 9, 8, 2, 4, 7]

bubble_sort(arr)

print((5 * '\n') + "Sorted array is:")
for i in arr:
    print(i)

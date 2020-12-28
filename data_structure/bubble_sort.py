""" Python program for implementation of Bubble Sort.
Code from: https://www.geeksforgeeks.org/bubble-sort/"""


def bubble_sort(arr):
    """ Time Complexity O(n ** 2)"""

    n = len(arr)
    # Show steps during iterations, and not mandatory for Bubble Sort.
    outer_loop_result = 0
    inner_loop_result = 0

    # Outer loop.
    for out_step in range(n):
        outer_loop_result += 1
        inner_loop_result = 0
        print(f"Result: {outer_loop_result} ==> {arr}")

        # Inner loop.
        # Loop is (n - 2) to avoid out of range when swap last two elements.
        for in_step in range(n - out_step - 1):
            # If left element greater than right element.
            if arr[in_step] > arr[in_step + 1]:
                # Swap elements.
                arr[in_step], arr[in_step + 1] = arr[in_step + 1], arr[in_step]

            inner_loop_result += 1
            print(f"    Inner: {inner_loop_result} ==> {arr}")


arr = [5, 3, 1, 9, 8, 2, 4, 7]

bubble_sort(arr)

print((5 * '\n') + "Sorted array is:")
for i in arr:
    print(i)

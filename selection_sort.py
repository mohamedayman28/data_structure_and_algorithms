""" Python program for implementation of Selection Sort.
Code originally from:
https://www.geeksforgeeks.org/python-program-for-selection-sort/"""


def selection_sort(arr):
    """ Time Complexity O(n ** 2).
    Space Complexity O(1)."""

    n = len(arr)

    # Feedback messages are not mandatory for Bubble Sort, will be used within
    # the code to show the steps during execustion, Thus deleting next variable
    # will cause an ERROR.
    result = 0

    # Outer loop, loop over all elements in the array.
    for outer_loop in range(n):

        # Feedback message.
        result += 1
        print(f"Result: {result} ==> {arr}")

        # Set first index in the array as smallest.
        smallest_index = outer_loop

        # Inner loop, escape index by +1(smallest_index + 1, n) for each loop,
        # and loop over the rest elements in the array, to make comparison
        # between escaped element and rest of element.
        for inner_loop in range(smallest_index + 1, n):
            if arr[smallest_index] > arr[inner_loop]:
                smallest_index = inner_loop

        # Swamp elements, if needed.
        arr[outer_loop], arr[smallest_index] = arr[smallest_index], arr[outer_loop]


arr = [6, 5, 1, 2, 4, 3]

selection_sort(arr)

print((5 * '\n') + "Sorted array is:")
for i in arr:
    print(i)

""" Python program for implementation of Binary Search."""

from math import floor


list_data = [2, 3, 4, 7, 8, 9, 11, 13, 98]
target = 1


def binary_search(list_data=list_data, target=target):
    # Set low and high pointers
    low = 0
    high = len(list_data) - 1

    while low <= high:
        # If mid is 3.5 use 3 as mid.
        mid = floor((low + high) / 2)

        # NOTE: list index is O(1).
        if list_data[mid] == target:
            return mid
        elif target < list_data[mid]:
            high = mid - 1
        else:
            low = mid + 1

    # -1 for not exist element.
    return -1

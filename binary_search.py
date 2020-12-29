""" Python program for implementation of Binary Search."""

list_data = [2, 3, 4, 7, 8, 9, 11, 13, 98]
target = 98


def binary_search(list_data=list_data, target=target):
    # Set low and high pointers
    low = 0
    high = len(list_data) - 1

    while low <= high:
        mid = (low + high) // 2

        if list_data[mid] == target:
            return mid
        elif target < list_data[mid]:
            high = mid - 1
        else:
            low = mid + 1

    # If element does not exist.
    return -1

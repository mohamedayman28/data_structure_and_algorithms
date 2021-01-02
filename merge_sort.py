""" Python program for implementation of Merge Sort.
Code originally from:
https://www.geeksforgeeks.org/merge-sort/"""


def merge_sort(arr):
    """ Divide and Conquer sorting algorithm using recursion abstraction.
    Time Complexity O(n log n).
    Space Complexity O(n)."""

    # Base Case: Array has more than one element.
    if len(arr) > 1:

        # Middle must not be float number .
        mid = len(arr) // 2

        # Dividing array into 2 halves. On Prime numbers right half will always
        # has greater number of elements by one element.
        left_half = arr[:mid]
        right_half = arr[mid:]

        print(f"Current array is: {arr}")
        print(f"    Left of the array: {left_half}")
        print(f"    Right of the array: {right_half} \n")

        # Each function will keep recurse until array has one element left.
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Copy data to two temporarily arrays left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Eventually the above loop will break due the imbalance
        # e.g. False and True, and biggest number from either left or right half
        # will be remained without being added to the temporarily array.
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


arr = [8, 7, 4, 3, 9, 2, 1]

merge_sort(arr)
print("Sorted array is: ", end="\n")
printList(arr)

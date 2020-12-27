""" Python program for implementation of Bubble Sort.
Code from: https://www.geeksforgeeks.org/bubble-sort/"""


def bubble_sort(arr):
    """ Time Complexity O(n ** 2)"""
    n = len(arr)

    # Last i elements are already in place.
    for i in range(n):

        # traverse the array from 0 to n-i-1
        # Swap if the element found is greater
        # than the next element
        for j in range(n - i - 1):
            print(n - i - 1)
            if arr[j] > arr[j + 1]:
                # Swap elements.
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Driver code to test above
arr = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]

bubble_sort(arr)

print("Sorted array is:")
for i in arr:
    print(i)

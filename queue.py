""" Python program for implementation of Queue abstract data structure."""

from collections import deque


queue = deque(['A', 'B', 'C'])


# Add at first.
# Time complexity O(1).
queue.appendleft(-1)

# Add at end.
# Time complexity O(1).
queue.append('Z')

# Remove first element.
# Time complexity O(1).
queue.popleft()

# Remove last element.
# Time complexity O(1).
queue.pop()

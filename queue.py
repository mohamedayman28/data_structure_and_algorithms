"""Python program for implementation of different types of Queue."""

from collections import deque


queue = deque(['A', 'B', 'C'])


# Add at first.
# Time complexity O(1).
queue.appendleft(-1)

# Add at end.
# Time complexity O(1).
queue.append('Z')

# Remove first element(-1).
# Time complexity O(1).
queue.popleft()

# Remove last element(Z).
# Time complexity O(1)).
queue.pop()

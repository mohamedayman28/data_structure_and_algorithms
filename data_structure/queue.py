class Queue:
    def __init__(self, head=None):
        self.__items = [head]
        self.__size = 0

    def __str__(self):
        return str(self.__items)

    def get_size(self):
        return self.__size

    def enqueue(self, new_element):
        """Time complexity O(1)"""
        self.__size += 1
        return self.__items.append(new_element)

    def dequeue(self):
        """Time complexity O(1)"""
        if self.__size != 0:
            self.__size -= 1
            return self.__items.pop(0)

    def peek(self):
        """Time complexity O(1)"""
        return self.__items[0]

class Node:
    def __init__(self, value):
        self.value = value
        self.__next = None

    def __str__(self):
        string = f"Node({self.value})"
        return string

    def get_current_node_value(self):
        return self.value

    def set_next_node(self, value):
        self.__next = value

    def get_next_node(self):
        return self.__next


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def __str__(self):
        return f'LinkedList.head({self.__head})\nLinkedList.Tail({self.__tail})\nLinkedList.size({self.__size})'

    def delete_tail(self):
        """ Delete Tail and assign pre-last element as Tail.
        Access Tail Time complexity is O(n), while deleting Tail is O(1)."""

        if self.__size == 0:
            return "List is empty"
        else:
            # Three pointer respectively Head, Head.Next, Head.Next.Next.
            first_pointer = self.__head
            second_pointer = first_pointer.get_next_node()
            # If None pointers reached end of list.
            third_pointer = second_pointer.get_next_node()

            while third_pointer is not None:
                # Shift pointers by one step.
                first_pointer = second_pointer
                second_pointer = third_pointer
                third_pointer = second_pointer.get_next_node()
            else:
                # If third pointer is None, set first pointer as Tail.
                self.__tail = first_pointer
                self.__tail.set_next_node(None)
                self.__size -= 1

    def delete_head(self):
        """ Delete Head and assign Head.next as Head.
        Time complexity O(1)."""

        if self.__size == 0:
            return "List is empty"
        else:
            # Two pointer respectively Head, Head.Next.
            first_pointer = self.__head
            second_pointer = first_pointer.get_next_node()
            # Replace first pointer with second pointer.
            self.__head = second_pointer
            self.__size -= 1

    def delete_node(self, value):
        """ Delete node at specific position and shift list Nodes by one.
        Time complexity is O(n))."""

        if self.__size == 0:
            return "List is empty"
        else:
            # Three pointer respectively Head, Head.Next, Head.Next.Next.
            first_pointer = self.__head
            second_pointer = first_pointer.get_next_node()
            third_pointer = second_pointer.get_next_node()

        while second_pointer.get_current_node_value() != value:
            # Shift pointers by one step.
            first_pointer = second_pointer
            second_pointer = third_pointer
            third_pointer = second_pointer.get_next_node()
        else:
            first_pointer.set_next_node(third_pointer)
            self.__size -= 1

    def get_tail(self):
        """ Time complexity O(1)."""

        if self.__tail is None:
            return None
        else:
            return self.__tail

    def get_head(self):
        """ Time complexity O(1)."""
        if self.__head is None:
            return None
        else:
            return self.__head

    def get_size(self):
        """ Time complexity O(1)."""
        return self.__size

    def get_node_position(self, value):
        """ Comparing argument value against each Node value and return its position.
        Time complexity O(n)."""

        # Set Head pointer.
        current_node = self.__head
        # Set position starter.
        position = 1

        # As pointer didn't reach end of the list.
        while current_node is not None:
            # If argument value equals Node value return Node position.
            if current_node.get_current_node_value() == value:
                return position
            # If argument value not equals Node value increment position by one.
            else:
                position += 1
                # Shift pointer to next Node.
                current_node = current_node.get_next_node()
        # If argument value doesn't evaluate with any Node value.
        return -1

    def append_node(self, value=None):
        """ Add Node to the end of the list.
        Time complexity O(1)."""

        if isinstance(value, Node):
            new_node = value
        else:
            new_node = Node(value)

        if self.__size == 0:
            self.__head = new_node
        else:
            self.__tail.set_next_node(new_node)

        self.__tail = new_node
        self.__size += 1

    def prepend_node(self, value=None):
        """ Add Node at the front of the list.
        Time complexity O(1)."""

        if self.__size == 0:
            self.append_node(value)
        else:
            current_head = self.__head

            if isinstance(value, Node):
                new_head = value
            else:
                new_head = Node(value)

            new_head.set_next_node(current_head)
            # Set new Node as Head.
            self.__head = new_head
            # Increment list size by one.
            self.__size += 1

    def add_node_after_node(self, value, position):
        """ Get Node by position and assign its next pointer to the new Node.
        Time complexity O(n)."""

        current_position = 0
        target_position = position - 1

        if not isinstance(value, Node):
            new_node = Node(value)
        else:
            new_node = value

        # Set two pointer respectively Head, Head.Next.
        first_pointer = self.__head
        second_pointer = first_pointer.get_next_node()

        if self.__size == 0:
            self.prepend_node(new_node)
        elif position == 0:
            first_pointer.set_next_node(new_node)
            return
        elif position > self.__size:
            self.append_node(new_node)
            return

        while current_position != target_position:
            # Shift pointers by one step.
            first_pointer = second_pointer
            second_pointer = first_pointer.get_next_node()
            current_position += 1
        else:
            first_pointer.set_next_node(new_node)
            new_node.set_next_node(second_pointer)

    def get_all_nodes(self):
        """ Loop over all Nodes and print them out.
        Time complexity O(n)."""
        if self.__size == 0:
            return "List is empty"

        first_pointer = self.__head

        while first_pointer is not None:
            print(first_pointer)
            first_pointer = first_pointer.get_next_node()

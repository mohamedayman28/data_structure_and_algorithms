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
        if self.__size == 0:
            return "List is empty"
        else:
            current_node = self.__head
            next_node = current_node.get_next_node()
            next_next_node = next_node.get_next_node()

            while next_next_node is not None:
                current_node = next_node
                next_node = next_next_node
                next_next_node = next_node.get_next_node()
            else:
                self.__tail = current_node
                self.__tail.set_next_node(None)
                self.__size -= 1

    def get_tail(self):
        if self.__tail is None:
            return None
        else:
            return self.__tail

    def delete_head(self):
        if self.__size == 0:
            return "List is empty"
        else:
            current_head = self.__head
            new_head = current_head.get_next_node()
            self.__head = new_head
            self.__size -= 1

    def get_head(self):
        if self.__head is None:
            return None
        else:
            return self.__head

    def get_size(self):
        return self.__size

    def append_node(self, value=None):
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
        if self.__size == 0:
            self.append_node(value)
        else:
            current_head = self.__head

            if isinstance(value, Node):
                new_head = value
            else:
                new_head = Node(value)

            new_head.set_next_node(current_head)
            self.__head = new_head
            self.__size += 1

    def delete_node(self, value):
        if self.__size == 0:
            return "List is empty"
        else:
            current_node = self.__head
            next_node = current_node.get_next_node()
            next_next_node = next_node.get_next_node()

        while next_node.get_current_node_value() != value:
            current_node = next_node
            next_node = next_next_node
            next_next_node = next_node.get_next_node()
        else:
            current_node.set_next_node(next_next_node)
            self.__size -= 1

    def add_node_after_node(self, value, position):
        current_position = 0
        wanted_position = position - 1

        if not isinstance(value, Node):
            new_node = Node(value)
        else:
            new_node = value

        if position == 0:
            self.prepend_node(new_node)
            return
        elif position > self.__size:
            self.append_node(new_node)
            return

        current_node = self.__head
        next_node = current_node.get_next_node()

        while current_node is not None and current_position != wanted_position:
            current_node = next_node
            next_node = current_node.get_next_node()
            current_position += 1
        else:
            current_node.set_next_node(new_node)
            new_node.set_next_node(next_node)

    def get_node_position(self, value):
        current_node = self.__head
        position = 1

        while current_node is not None:
            if current_node.get_current_node_value() == value:
                return position
            else:
                position += 1
                current_node = current_node.get_next_node()

        return -1

    def get_all_nodes(self):
        if self.__size == 0:
            return "List is empty"

        current_node = self.__head

        while current_node is not None:
            print(current_node)
            current_node = current_node.get_next_node()


if __name__ == '__main__':
    print(5 * '\n')
    linked_list = LinkedList()

    linked_list.append_node('foo')
    linked_list.append_node('fool')

    linked_list.add_node_after_node('zar', 0)

    print(linked_list.get_size() == 3)

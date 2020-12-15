import unittest

from data_structure import linked_list


class TestNode(unittest.TestCase):

    node = linked_list.Node

    def get_next_node(self, value):
        """Call Node.set_next_node() and Node.get_next_node() in one function
        and use it in setUp."""
        new_node = TestNode.node(None)
        new_node.set_next_node(value)
        next_node = new_node.get_next_node()

        return next_node

    def setUp(self):
        self.get_next_node = self.get_next_node

    def test_get_next_node(self):
        self.assertIsNone(self.get_next_node(None))
        self.assertIsInstance(self.get_next_node('foo'), str)
        self.assertIsInstance(self.get_next_node(52), int)
        self.assertIsInstance(self.get_next_node(1.3), float)
        self.assertIsInstance(self.get_next_node([3]), list)
        self.assertIsInstance(self.get_next_node({'a': 1}), dict)
        self.assertIsInstance(self.get_next_node((1,)), tuple)
        self.assertIsInstance(self.get_next_node(False), bool)
        self.assertIsInstance(self.get_next_node(
            TestNode.node('')), TestNode.node)


class TestLinkedList(unittest.TestCase):
    # Call the list object
    list_ = linked_list.LinkedList

    def setUp(self):
        # List with one node.
        self.deafult_list = TestLinkedList.list_()
        self.one_node_list = TestLinkedList.list_()
        self.one_node_list.append_node('a')

        # List with two nodes.
        self.two_nodes_list = TestLinkedList.list_()
        self.two_nodes_list.append_node('a')
        self.two_nodes_list.append_node('b')

        # List with three nodes.
        self.three_nodes_list = TestLinkedList.list_()
        self.three_nodes_list.append_node('a')
        self.three_nodes_list.append_node('b')
        self.three_nodes_list.append_node('c')

    def test_delet_head_method(self):
        self.assertIsInstance(self.deafult_list.delete_head(), str)

    def test_get_head_get_tail_get_size_methods(self):
        self.assertIsNone(self.deafult_list.get_head(), None)
        self.assertIsNone(self.deafult_list.get_tail(), None)
        self.assertEqual(self.deafult_list.get_size(), 0)

        self.assertIsInstance(self.one_node_list.get_head(), TestNode.node)
        self.assertIsInstance(self.one_node_list.get_tail(), TestNode.node)
        self.assertIsInstance(self.one_node_list.get_size(), int)
        self.assertEqual(self.one_node_list.get_size(), 1)

        self.assertIsInstance(self.two_nodes_list.get_head(), TestNode.node)
        self.assertIsInstance(self.two_nodes_list.get_tail(), TestNode.node)
        self.assertIsInstance(self.two_nodes_list.get_size(), int)
        self.assertEqual(self.two_nodes_list.get_size(), 2)

    def test_append_node_method(self):
        # Append node to an empty list.
        self.deafult_list.append_node('foo')
        head = self.one_node_list.get_head()
        tail = self.one_node_list.get_tail()
        same = head is tail
        self.assertTrue(same)

        # Append sceond node.
        self.deafult_list.append_node(TestNode.node('foo'))
        head = self.deafult_list.get_head()
        tail = self.deafult_list.get_tail()
        same = head is not tail
        self.assertTrue(same)

    def test_prepend_node_method(self):
        # Append nodes.
        self.deafult_list.append_node('foo')
        self.deafult_list.append_node('foo')
        old_head = self.deafult_list.get_head()

        # Prepend node.
        self.deafult_list.prepend_node('foo')
        new_head = self.deafult_list.get_head()
        same = new_head.get_next_node() is old_head
        self.assertTrue(same)

    def test_get_node_position_method(self):
        self.deafult_list.append_node('a')
        self.deafult_list.append_node('b')
        self.deafult_list.append_node('c')
        self.assertEqual(self.deafult_list.get_node_position('z'), -1)
        self.assertNotEqual(self.deafult_list.get_node_position('b'), -1)
        self.assertEqual(self.deafult_list.get_node_position('b'), 2)

    def test_add_node_after_node_method(self):
        # Add node to an empty list.
        self.deafult_list.add_node_after_node('foo', 10)
        head = self.deafult_list.get_head()
        tail = self.deafult_list.get_tail()
        head_is_tail = head is tail
        self.assertTrue(head_is_tail)

        # Add node to list with ndoes, as position > list size.
        self.two_nodes_list.add_node_after_node('foo', 10)
        head = self.two_nodes_list.get_head()
        tail = self.two_nodes_list.get_tail()
        tail_is_new_node = tail.get_current_node_value()
        self.assertEqual(tail_is_new_node, 'foo')

        # Add node to list with ndoes, at position 1.
        self.three_nodes_list.add_node_after_node('foo', 0)
        list_size_is_4 = self.three_nodes_list.get_size()
        node_position_is_1 = self.three_nodes_list.get_node_position('foo')
        self.assertEqual(list_size_is_4, 4)
        self.assertEqual(node_position_is_1, 1)

    def test_delete_node_method(self):
        pass


if __name__ == '__main__':
    print(5 * '\n')
    unittest.main()

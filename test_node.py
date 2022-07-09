import unittest

from node import Node, DoubleLinkedNode


class TestNode(unittest.TestCase):
    def test_init_node_without_next(self):
        node = Node(5)
        self.assertIsNone(node.next,
                          msg='Значение следующего узла должно быть None')

    def test_init_node_with_next(self):
        second_node = Node('second_node')
        first_node = Node('first_node', second_node)

        expected_value = second_node
        actual_node = first_node.next
        self.assertIs(expected_value, actual_node,
                      msg='Не тождественно равные объекты next')

    def test_repr_node_without_next(self):
        node = Node(5)
        expected_value = 'Node(5, None)'
        actual_value = repr(node)
        self.assertEqual(expected_value, actual_value,
                         msg='Представление repr не совпадает')

    def test_repr_node_with_next(self):
        first_node = Node('first_node')
        second_node = Node('second_node')
        first_node.next = second_node

        expected_value = 'Node(first_node, Node(second_node))'
        actual_value = repr(first_node)
        self.assertEqual(expected_value, actual_value,
                         msg='Представление repr не совпадает')

    def test_str(self):
        some_value = 5
        node = Node(some_value)

        expected_value = '5'
        self.assertEqual(expected_value, str(node),
                         msg='Представление str не совпадает')
        self.assertEqual(expected_value, f'{node}',
                         msg='Представление str не совпадает')

    def test_is_valid(self):
        Node.is_valid(None)
        Node.is_valid(Node(5))
        with self.assertRaises(TypeError, msg="Неверный тип ошибки"):
            Node.is_valid("incorrect_value")


class TestDln(unittest.TestCase):
    def test_double_linked_node_init_prev(self):
        prev_node = DoubleLinkedNode(1)
        middle_node = DoubleLinkedNode(2, prev=prev_node)
        prev_node.next = middle_node

        expected_value = 'DoubleLinkedNode(2, None, ' \
                         'DoubleLinkedNode(1, None, None))'
        actual_value = repr(middle_node)

        self.assertEqual(expected_value, actual_value)

    def test_double_linked_node_without_next(self):
        prev_node = DoubleLinkedNode(1)
        middle_node = DoubleLinkedNode(2)

        middle_node.prev = prev_node
        prev_node.next = middle_node

        expected_value = 'DoubleLinkedNode(2, None, ' \
                         'DoubleLinkedNode(1, None, None))'

        actual_value = repr(middle_node)

        self.assertEqual(expected_value, actual_value)

    def test_double_linked_node_without_next_and_prev(self):
        middle_node = DoubleLinkedNode(2)

        expected_value = "DoubleLinkedNode(2, None, None)"
        actual_value = repr(middle_node)

        self.assertEqual(expected_value, actual_value)

    def test_double_linked_node_with_next_and_prev(self):
        prev_node = DoubleLinkedNode(1)
        middle_node = DoubleLinkedNode(2)
        next_node = DoubleLinkedNode(3)

        middle_node.prev = prev_node
        middle_node.next = next_node

        expected_value = 'DoubleLinkedNode(2, DoubleLinkedNode(3, None, None), ' \
                         'DoubleLinkedNode(1, None, None))'

        actual_value = repr(middle_node)
        self.assertEqual(expected_value, actual_value)

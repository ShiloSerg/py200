import unittest

from task import LinkedList, DoubleLinkedList


class TestLinkedList(unittest.TestCase):

    def test_init_ll(self):
        value = [1, 2, 3]
        ll = LinkedList(value)

        self.assertEqual("LinkedList([1, 2, 3])", repr(ll),
                         msg='Ожидаемые и актуальные данные не совпадают')
        self.assertEqual("[1, 2, 3]", str(ll),
                         msg='Ожидаемые и актуальные данные не совпадают')

    def test_ll_nodes(self):
        value = [1, 2]
        ll = LinkedList(value)
        first_node = ll.step_by_step_on_nodes(0)
        second_node = ll.step_by_step_on_nodes(1)

        self.assertTrue(first_node.next is second_node,
                        msg='Ожидаемые и актуальные данные не совпадают')
        self.assertIsNone(second_node.next,
                          msg='Ожидаемые и актуальные данные не совпадают')

    def test_insert(self):
        value = [1, 2]
        ll = LinkedList(value)
        ll.insert(1, 3)
        expected_value = 'LinkedList([1, 3, 2])'
        actual_value = repr(ll)

        self.assertEqual(expected_value, actual_value,
                         msg='Представление repr не совпадает')

    def test_ll_append(self):
        value = [1, 2]
        ll = LinkedList(value)
        ll.append(3)
        expected_value = 'LinkedList([1, 2, 3])'
        actual_value = repr(ll)

        self.assertEqual(expected_value, actual_value,
                         msg='Представление repr не совпадает')

    def test_getitem(self):
        value = [1, 2]
        ll = LinkedList(value)
        expected_value = 2
        actual_value = ll.__getitem__(1)

        self.assertEqual(expected_value, actual_value,
                         msg='Представление repr не совпадает')

    def test_setitem(self):
        value = [1, 2]
        ll = LinkedList(value)
        ll.__setitem__(1, 3)
        expected_value = 'LinkedList([1, 3])'
        actual_value = repr(ll)

        self.assertEqual(expected_value, actual_value,
                         msg='Представление repr не совпадает')

    def test_step_by_step_on_nodes(self):
        value = [1, 2]
        ll = LinkedList(value)
        value_index = 1
        expected_value = 'Node(2, None)'
        actual_value = repr(ll.step_by_step_on_nodes(value_index))
        self.assertEqual(expected_value, actual_value,
                         msg='Представление repr не совпадает')

    def test_delitem(self):
        value = [1, 2, 3]
        ll = LinkedList(value)
        ll.__delitem__(1)
        expected_value = 'LinkedList([1, 3])'
        actual_value = repr(ll)
        self.assertEqual(expected_value, actual_value,
                         msg='Представление repr не совпадает')

    def test_len(self):
        value = [1, 2, 3]
        ll = LinkedList(value)
        expected_value = 3
        actual_value = ll.__len__()
        self.assertEqual(expected_value, actual_value,
                         msg='Представление repr не совпадает')

    def test_repr(self):
        value = [1, 2, 3]
        ll = LinkedList(value)
        expected_value = 'LinkedList([1, 2, 3])'
        actual_value = repr(ll)
        self.assertEqual(expected_value, actual_value,
                         msg='Представление repr не совпадает')

    def test_str(self):
        value = [1, 2, 3]
        ll = LinkedList(value)
        expected_value = '[1, 2, 3]'
        actual_value = str(ll)
        self.assertEqual(expected_value, actual_value,
                         msg='Ожидаемые и актуальные данные не совпадают')

    def test_count(self):
        value = [1, 2, 2]
        ll = LinkedList(value)
        expected_value = '2'
        actual_value = str(ll.count(2))
        self.assertEqual(expected_value, actual_value,
                         msg='Ожидаемые и актуальные данные не совпадают')

    def test_pop(self):
        value = [1, 2, 3]
        ll = LinkedList(value)
        expected_value = '3'
        actual_value = str(ll.pop(2))
        self.assertEqual(expected_value, actual_value,
                         msg='Ожидаемые и актуальные данные не совпадают')

    def test_index(self):
        value = [1, 2, 3]
        ll = LinkedList(value)
        self.assertEqual('0', repr(ll.index(1)),
                         msg='Ожидаемые и актуальные данные не совпадают')


class DoubleLinkedListTest(unittest.TestCase):

    def test_init_dll(self):
        value = [1, 2, 3]
        list2 = DoubleLinkedList(value)

        self.assertEqual('DoubleLinkedList([1, 2, 3])', repr(list2),
                         msg='Ожидаемые и актуальные данные не совпадают')
        self.assertEqual('[1, 2, 3]', str(list2))

    def test_dll_nodes(self):
        value = [1, 2]
        dll = DoubleLinkedList(value)
        first_node = dll.step_by_step_on_nodes(0)
        second_node = dll.step_by_step_on_nodes(1)

        self.assertTrue(first_node.next is second_node,
                        msg='Ожидаемые и актуальные данные не совпадают')
        self.assertIsNone(second_node.next,
                          msg='Ожидаемые и актуальные данные не совпадают')

        self.assertIsNone(first_node.prev,
                          msg='Ожидаемые и актуальные данные не совпадают')
        self.assertTrue(second_node.prev is first_node,
                        msg='Ожидаемые и актуальные данные не совпадают')

    def test_append(self):
        value = [1, 2]
        dll = DoubleLinkedList(value)
        dll.append(3)
        dll.append(4)
        expected_value = '[1, 2, 3, 4]'
        actual_value = str(dll)
        self.assertEqual(expected_value, actual_value,
                         msg='Ожидаемые и актуальные данные не совпадают')

    def test_getitem(self):
        value = [0, 1, 2, 3, 4]
        dll = DoubleLinkedList(value)
        expected_value = 3
        actual_value = dll[3]
        self.assertEqual(expected_value, actual_value,
                         msg='Ожидаемые и актуальные данные не совпадают')

    def test_delete(self):
        value = [1, 2, 3]
        dll = DoubleLinkedList(value)
        del (dll[0])
        self.assertEqual("[2, 3]", str(dll),
                         msg='Ожидаемые и актуальные данные не совпадают')
        dll = DoubleLinkedList(value)
        del (dll[2])
        self.assertEqual("[1, 2]", str(dll),
                         msg='Ожидаемые и актуальные данные не совпадают')

    def test_insert(self):
        value = [1, 2, 3]
        dll = DoubleLinkedList(value)
        dll.insert(0, 0)
        self.assertEqual("[0, 1, 2, 3]", str(dll),
                         msg='Ожидаемые и актуальные данные не совпадают')
        dll.insert(4, 5)
        self.assertEqual("[0, 1, 2, 3, 5]", str(dll),
                         msg='Ожидаемые и актуальные данные не совпадают')
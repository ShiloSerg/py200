from typing import Any, Iterable, Optional

from collections.abc import MutableSequence

from node import Node, DoubleLinkedNode


class LinkedList(MutableSequence):

    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self._len = 0
        self._head: Optional[Node] = None
        self._tail = self._head

        if data is not None:
            for value in data:
                self.append(value)

    @property
    def list_node(self):
        return Node

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    def insert(self, index: int, value: Any):
        self.check_int(index)
        insert_node = self.list_node(value)

        if index == 0:
            insert_node.next = self._head
            self._head = insert_node
        elif index == self._len:
            self.append(value)
        elif index > self._len:
            raise ValueError('индекс больше длинны списка')
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            next_node = prev_node.next
            self.linked_nodes(prev_node, insert_node)
            self.linked_nodes(insert_node, next_node)

        self._len += 1

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = self.list_node(value)

        if self._head is None:
            self._head = self._tail = append_node
        else:
            self.linked_nodes(self._tail, append_node)
            self._tail = append_node

        self._len += 1

    def step_by_step_on_nodes(self, index: int):
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        self.check_int(index)

        if not 0 <= index < self._len:
            raise IndexError()

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node

    def __getitem__(self, index: int) -> Any:
        """
        Метод возвращает значение узла по указанному индексу.
        :param index: Индкес элемента
        """
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index: int):
        """ Метод удаляет узел по указанному индексу. """
        self.check_int(index)
        if not 0 <= index < self._len:
            raise IndexError()

        if index == 0:
            self._head = self._head.next
        elif index == self._len - 1:
            tail = self.step_by_step_on_nodes(index - 1)
            tail.next = None
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            del_node = prev_node.next
            next_node = del_node.next

            self.linked_nodes(prev_node, next_node)

        self._len -= 1

    def __len__(self):
        """ Метод возвращает длинну списка. """
        return self._len

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"

    def count(self, value: int):
        """ Функция count """
        __counter = 0
        if not isinstance(value, int):
            raise TypeError()
        elif self._head is None:
            raise ValueError('Лист пустой')
        else:
            for elem in self:
                if elem == value:
                    __counter += 1
        return __counter

    def pop(self, index: Optional[int] = None):
        """ Метод возвращает элемент и удаляет элемент списка"""
        self.check_int(index)
        if self._head is None:
            raise ValueError('Лист пустой')
        elif index > self._len - 1:
            data = self.step_by_step_on_nodes(self._len - 1)
            print(self.step_by_step_on_nodes(self._len - 1))
            self.__delitem__(self._len - 1)
            return data
        else:
            data = self.step_by_step_on_nodes(self._len - 1)
            print(self.step_by_step_on_nodes(index))
            self.__delitem__(index)
            return data

    def extend(self, new_list: list):
        """ Метод складывания двух списков """
        if not isinstance(new_list, list):
            raise TypeError('Указан не list')
        elif self._head is None:
            raise ValueError('Лист не может быть пустым')
        else:
            for elem in new_list:
                self.append(elem)

    def index(self, value: Any, **kwargs):
        """ Метод возвращает индекс элемента.
        :param value: Индеекс искомого элемента
        :param **kwargs: Аргументы поиска index(x[, start[, end]])
        """
        for index, elem in enumerate(self):
            if elem == value:
                return index

    @staticmethod
    def check_int(value: Any):
        """ Метод проверяет является ли значение числом"""
        if not isinstance(value, int):
            raise TypeError()

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.value
            current_node = current_node.next

    def __contains__(self, value: Any):
        """
        :param value: Значение для поиска в списке
        :return: Метод возвращает True, если значение есть в списке
        """
        if self.head is None:
            return False

        current_node = self._head
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next
        else:
            return False


class DoubleLinkedList(LinkedList):
    @property
    def list_node(self):
        return DoubleLinkedNode

    @staticmethod
    def linked_nodes(left_node: DoubleLinkedNode,
                     right_node: Optional[DoubleLinkedNode] = None) -> None:
        left_node.next = right_node
        right_node.prev = left_node

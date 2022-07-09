from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next = next_

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None \
            else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    @staticmethod
    def is_valid(node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self._next = next_


class DoubleLinkedNode(Node):
    """ Класс, который описывает узел двусвязного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None, prev: Optional["Node"] = None) -> None:
        super().__init__(value, next_)
        self._prev = prev

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev: Optional["DoubleLinkedNode"] = None):
        self.is_valid(prev)
        self._prev = prev

    def __repr__(self) -> str:
        next_repr: str = str(None) \
            if self.next is None \
            else f'DoubleLinkedNode({self.next.value}, {None}, {None})'
        prev_repr: str = str(None) \
            if self.prev is None \
            else f'DoubleLinkedNode({self.prev.value}, {None}, {None})'

        return f'DoubleLinkedNode({self.value}, {next_repr}, {prev_repr})'

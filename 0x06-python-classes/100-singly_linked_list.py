#!/usr/bin/python3


class Node:

    def __init__(self, data, next_node=None):
        if isinstance(data, int):
            self.__data = data
        else:
            raise TypeError("data must be an integer")

        if isinstance(next_node, Node) or next_node is None:
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:

    def __init__(self):
        self.__head = None

    def __str__(self):
        current = self.__head
        s = ""

        while current is not None:
            s += str(current.data)
            if current.next_node is not None:
                s += '\n'
            current = current.next_node

        return s

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
            return

        current = self.__head
        prev = None
        new = Node(value)

        while True:
            if current.data >= value:
                new.next_node = current
                if prev is not None:
                    prev.next_node = new
                if current is self.__head:
                    self.__head = new
                return
            prev = current
            current = current.next_node
            if current is None:
                prev.next_node = new
                return

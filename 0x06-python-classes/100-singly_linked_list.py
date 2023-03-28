#!/usr/bin/python3
class Node:
    """
    A class that defines a node of a singly linked list.

    Attributes:
        data (int): the integer value stored in the node.
        next_node (Node): the next node in the linked list.

    Methods:
        __init__(self, data, next_node=None): Instantiates a new Node object.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a new Node object with the given data and next_node.

        Args:
            data (int): The integer value to be stored in the node.
            next_node (Node): The next node in the linked list. Default is None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """int: The integer value stored in the node."""
        return self._data

    @data.setter
    def data(self, value):
        """
        Setter for the data attribute of a Node object.

        Args:
            value (int): The integer value to be stored in the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """Node: The next node in the linked list."""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter for the next_node attribute of a Node object.

        Args:
            value (Node): The next node in the linked list. Default is None.

        Raises:
            TypeError: If value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """
    A class that defines a singly linked list.

    Attributes:
        head (Node): The first node in the linked list.

    Methods:
        __init__(self): Instantiates a new SinglyLinkedList object.
        __repr__(self): Returns a string representation of the linked list.
        sorted_insert(self, value): Inserts a new node into the linked list in the correct sorted position.
    """
    def __init__(self):
        """
        Initializes a new SinglyLinkedList object with an empty list.
        """
        self.head = None

    def __repr__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: The linked list as a string, with each node's data on a new line.
        """
        current = self.head
        nodes = []
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        """
        Inserts a new node with the given value in the correct sorted position in the linked list.

        Args:
            value (int): The integer value to be stored in the new node.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif self.head.data > value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node


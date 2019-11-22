"""
A Doubly_linked_list class implementation
"""

# Built-in/Generic Imports

# Libs

# Own modules

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = ''


class DoublyLinkedList(object):
    class Node:
        """Doubly linked node which stores an object"""

        def __init__(self, element, next_node=None, previous_node=None):
            self.__element = element
            self.__next_node = next_node
            self.__previous_node = previous_node

        def get_element(self):
            """Returns the element stored in this node"""
            return self.__element

        def get_previous(self):
            """Returns the previous linked node"""
            return self.__previous_node

        def get_next(self):
            """Returns the next linked node"""
            return self.__next_node

        def set_element(self, element):
            """Sets the element stored in this node"""
            self.__element = element

        def set_previous(self, previous_node):
            """Sets the previous linked node"""
            self.__previous_node = previous_node

        def set_next(self, next_node):
            """Sets the next linked node"""
            self.__next_node = next_node

        def __lt__(self, other):
            '''return T|F self smaller than other'''
            return self.get_element() < other.get_element()

    def __init__(self):
        self.__size = 0
        self.__header = Node('Header')
        self.__trailer = Node('Trailer')
        self.__header.set_next(self.__trailer)
        self.__trailer.set_previous(self.__header)
        self.__current = None

    def __iter__(self):
        """Standard python iterator method"""
        self.__current = self.get_first()
        return self

    def __next__(self):
        """Standard python iterator method"""
        if self.__current == self.__trailer:
            raise StopIteration()
        result = self.__current
        self.__current = self.__current.get_next()
        return result

    def get_previous(self, node):
        """Returns the node before the given node"""
        if node is None:
            return None
        else:
            return node.get_previous()

    def get_next(self, node):
        """Returns the node after the given node"""
        if node is None:
            return None
        else:
            return node.get_next()

    def traverse(self, visitor):
        """Visit every element in the list"""
        for s in self: visitor(s)

    def size(self):
        """Returns the number of elements in the list"""
        return self.__size

    def get_first(self):
        """Get the first element of the list"""
        if self.is_empty():
            return None
        else:
            return self.__header.get_next()

    def get_last(self):
        """Get the last element of the list"""
        if self.is_empty():
            return None
        else:
            return self.__trailer.get_previous()

    def add_first(self, new):
        """Insert the node at the head of the list"""
        new.set_next(self.__header.get_next())
        new.set_previous(self.__header)
        # update header and trailer ..
        self.__header.get_next().set_previous(new)
        self.__header.set_next(new)
        self.__current = new
        self.__size += 1

    def add_last(self, new):
        """Insert the node at the tail of the list"""
        new.set_next(self.__trailer)
        new.set_previous(self.__trailer.get_previous())
        # update header and trailer ..
        self.__trailer.get_previous().set_next(new)
        self.__trailer.set_previous(new)
        self.__current = new
        self.__size += 1

    def is_empty(self):
        """Returns wether the list has zero nodes or not"""
        empty = False
        if self.__header.get_next() == self.__trailer and \
                self.__trailer.get_previous() == self.__header:
            empty = True
        return empty

    def remove(self, node):
        """Remove the given node from the list"""
        if node is not None:
            pred = node.get_previous()
            succ = node.get_next()
            pred.set_next(succ)
            succ.set_previous(pred)
            self.__current = pred
            self.__size -= 1

    def search(self, key):
        fnd = None
        curr = self.get_first()
        while curr != self.__trailer and not fnd:
            if curr.get_element() == key:
                fnd = curr
            else:
                curr = curr.get_next()
        return fnd

    def smallest(self):
        sml = self.get_first()
        curr = self.get_first().get_next()
        while curr != self.__trailer:
            if curr.get_element() < sml.get_element():
                sml = curr
            curr = curr.get_next()
        return sml
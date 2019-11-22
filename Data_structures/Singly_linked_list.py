"""

"""

# Built-in/Generic Imports

# Libs

# Own modules

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = ''


class SinglylinkedList:
    class Node:
        def __init__(self, data, next_item=None):
            self.__data = data
            self.__next_item = next_item

        def set_next(self, next_item):
            self.__next_item = next_item
            return

        def set_data(self, data):
            self.__data = data
            return

        def get_data(self):
            return self.__data

        def get_next(self):
            return self.__next_item

    # Constructs an empty list
    def __init__(self):
        self.length = 0
        self.head = self.Node(None)
        self.trail = self.Node(None)

        self.head.set_next(self.trail)

    # Adds a element to the list
    def add(self, val):
        if self.length == 0:
            new_node = self.Node(val)
            new_node.set_next(self.trail)
            self.head.set_next(new_node)
            self.length += 1

        else:
            node = self.head.get_next()

            while node.get_next() != self.trail:
                node = node.get_next()

            new_node = self.Node(val)
            new_node.set_next(self.trail)
            node.set_next(new_node)
            self.length += 1

    # Removes all elements equal to val
    def remove(self, val):
        if self.length == 0:
            return print("No items in list")

        else:
            prev_node = 0
            node = self.head

            while node != self.trail:
                if node.get_data() == val:
                    prev_node.set_next(node.get_next())
                    node = node.get_next()
                    self.length -= 1
                else:
                    prev_node = node
                    node = node.get_next()

    # Prints the list like a Python array
    def __str__(self):
        if self.length == 0:
            return "[]"

        else:
            printed_lst = "["
            node = self.head

            while node.get_next() != self.trail:
                node = node.get_next()
                printed_lst = printed_lst + str(node.get_data()) + ","
            printed_lst = printed_lst[:-1] + "]"

        return printed_lst
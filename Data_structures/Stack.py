"""
A stack implementation
"""

# Built-in/Generic Imports

# Libs

# Own modules

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = ''


class Stack(object):
    def __init__(self, max_size=10):
        self.__item_list = [None] * max_size
        self.__top = -1
        self.__capacity = max_size

    def push(self, node):
        if self.__top == self.__capacity - 1:
            print('warning: stack is full')
        else:
            self.__item_list[self.__top + 1] = node
            self.__top += 1

    def pop(self):
        node = None
        if self.__top > -1:
            node = self.__item_list[self.__top]
            self.__item_list[self.__top] = None
            self.__top -= 1
        return node

    def get_capacity(self):
        return self.__capacity

    def get_size(self):
        return self.__top + 1

    def is_empty(self):
        return self.get_size() == 0
"""
A simple memoisation example used to improve recursion processes, here demonstrated using fibonacy
"""

# Built-in/Generic Imports

# Libs

# Own modules

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = ''

# -- Memoisation example
iter_dict = {}
iter_dict[0] = 0
iter_dict[1] = 1


def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x - 2) + fib(x - 1)


def iter_fib(x):
    if x in iter_dict.keys():
        return iter_dict[x]
    else:
        iter_dict[x] = iter_fib(x - 2) + iter_fib(x - 1)
        return iter_dict[x]


# print(iter_fib(25))

# -- Stack overflow error correction
def foo(n):
    if n == 0:
        return 0
    return 1 + foo(n - 1)

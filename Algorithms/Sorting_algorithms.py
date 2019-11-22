"""
Various sorting algorithms packaged in functions for ease of use
"""

# Built-in/Generic Imports

# Libs

# Own modules

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = ''

# __________________________________________ Sorting algorithms ____________________________________________
lst = [3, 8, 6, 9, 7, 2, 1, 5, 4]


def bubble_sort(lst):
    for j in range(len(lst)):
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]

    print("bubble_sort", lst)
    return


def selection_sort(lst):
    sorted_lst = []
    iter_lst = lst

    while len(iter_lst) != 0:
        sorted_lst.append(min(iter_lst))
        iter_lst.remove(min(iter_lst))

    print("selection_sort", sorted_lst)
    return


def insertion_sort(lst):
    for i in range(1, len(lst)):
        j = i-1
        item = lst[i]

        while lst[j] > item and j != -1:
            lst[j+1] = lst[j]
            j -= 1

        lst[j+1] = item

    print("insertion_sort", lst)
    return


def insertion_sort_2(lst):
    for j in range(1, len(lst)):
        for i in range(j, 0, -1):
            if lst[i] < lst[i-1]:
                lst[i], lst[i-1] = lst[i-1], lst[i]

    print("insertion_sort", lst)
    return
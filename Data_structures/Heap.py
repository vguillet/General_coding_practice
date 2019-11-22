"""
A heap class implementation
"""

# Built-in/Generic Imports

# Libs

# Own modules

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = ''


class Heap:
    '''min heap queue'''
    def __init__(self):
        self.heap = []
        self.count = 0

    def empty(self):
        '''return T|F heap is empty'''
        return self.count == 0

    def hsize(self):
        '''return nr of items in heap'''
        return self.count

    def push(self, item):
        '''insert item in the heap'''
        self.heap.append(item)
        self.count += 1
        # restore the heap invariant ...
        self.heapify_min(self.count - 1)

    def pop(self):
        '''get next item from the heap'''
        next_item = None
        if not self.empty():
            # copy the root node ...
            next_item = self.heap[0]
            # swap the rightmost leaf ...
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            self.count -= 1
            # restore the heap property ...
            self.heapify_min(0)
            # return the (former) root item ...
        return next_item

    def heapify_min(self, ndx):
        '''restore the min heap invariant'''

        def _swap(p, q):
            """swap two heap elements"""
            self.heap[p], self.heap[q] = self.heap[q], self.heap[p]

        if self.count > 2 * ndx + 2:
            if (self.heap[ndx] > self.heap[2 * ndx + 1]) or (self.heap[ndx] > self.heap[2 * ndx + 2]):
                if self.heap[2 * ndx + 1] < self.heap[2 * ndx + 2]:
                    nextNode = 2 * ndx + 1
                else:
                    nextNode = 2 * ndx + 2
                _swap(ndx, nextNode)
                self.heapify_min(nextNode)
        elif (self.count == 2 * ndx + 2):
            if self.heap[ndx] > self.heap[2 * ndx + 1]:
                nextNode = 2 * ndx + 1
                _swap(ndx, nextNode)
                self.heapify_min(nextNode)
        if ndx > 0:
            parent = int((ndx - (2 - ndx % 2)) / 2)
            if self.heap[ndx] < self.heap[parent]:
                _swap(ndx, parent)
                self.heapify_min(parent)

    def print_heap(self):
        '''print the heap item list'''
        print('Heap (items: {:d}):'.format(self.count))
        print('{:s}'.format(str(self.heap)))

    def print_heap_structure(self, title=''):
        '''print the structure of the heap, level by level'''

        def _deepest(heap_items, k):
            return self.count <= 2 ** (k + 1) - 1

        def _items_at_depth(heap_items, k):
            _from, _to = 2 ** k - 1, 2 ** (k + 1) - 1
            if _deepest(heap_items, k):
                # correct it if not full ...
                _to = self.count
            return self.heap[_from:_to]

        print(title)
        depth, done = 0, False
        while not done:
            # if deepest level ...
            print('{:s}'.format(str(_items_at_depth(self.heap, depth))))
            if _deepest(self.heap, depth):
                done = True
            else:
                depth += 1

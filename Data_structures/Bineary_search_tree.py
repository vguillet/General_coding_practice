"""
A binary search tree class implementation
"""

# Built-in/Generic Imports

# Libs

# Own modules

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = ''


class Node:
    @staticmethod
    def find(root, parent, key):
        """return node with key given or None if not found"""
        # key in the root?
        if root is None or root.data == key:
            return root, parent
        # key greater than root's key?
        if key > root.data:
            return Node.find(root.right, root, key)
        # Key is smaller than root's key
        return Node.find(root.left, root, key)

    @staticmethod
    def height(tree):
        if (tree == None):
            return 0
        hleft = Node.height(tree.left)
        hright = Node.height(tree.right)
        return max(hleft, hright) + 1

    @staticmethod
    def printNode(node):
        """visitor function"""
        print('{:s}'.format(str(node.data)), end=' ')

    # ---------------------

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def child_count(self):
        """return nr of chldren"""
        count = 0
        if self.left is not None:
            count += 1
        if self.right is not None:
            count += 1
        return count

    def insert(self, data):
        """insert data in binary tree"""
        if data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                # insert it in the left subtree ...
                self.right.insert(data)
        else:
            if self.left is None:
                self.left = Node(data)
            else:
                # insert it in the right subtree ...
                self.left.insert(data)

    def delete(self, key):
        """delete node with key given"""

        # aux functions for delete ...
        def _delete_leaf(node, parent):
            """delete a leaf node; 0 children"""
            result = False
            if parent is None:
                # it is the root node...
                # ... no parent to update ...
                node = None
            else:
                # it is a leaf node ...
                # ... update the correct link info ...
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
            del node
            result = True
            return result

        def _delete_one(node, parent):
            """delete a node with 1 child"""
            result = False
            # ... shift up child to position of the node ...
            # ... connect node->child to parent ...
            if node.left is not None:
                toShiftUp = node.left
            else:
                toShiftUp = node.right
            if parent is None:
                # it is the root node ...
                # ... just copy ...
                node.left = toShiftUp.left
                node.right = toShiftUp.right
                node.set_data = toShiftUp.data
            else:
                # no, it's not the root ...
                if parent.left is node:
                    parent.left = toShiftUp
                else:
                    parent.right = toShiftUp
                del node
            result = True
            return result

        def _delete_two(node, parent):
            """delete a node with two subtrees"""

            def _find_successor(node, parent):
                """find successor and keep track of node and parent"""
                parent_succ = node
                succ = node.right
                while succ.left is not None:
                    parent_succ = succ
                    succ = succ.left
                # we reached the leaf ...
                return succ, parent_succ

            result = False

            # we are always finding a successor ...
            succ, parent_succ = _find_successor(node, parent)
            # now copy the data ...
            node.data = succ.data
            # ... and recursively remove my duplicate (succ)...
            # ... which can atmost have 1 child (to the right)
            if succ.right is not None:
                result = _delete_one(succ, parent_succ)
            else:
                result = _delete_leaf(succ, parent_succ)
            return result

        # delete main function ...
        # -----------------------------------------

        # keep track of the result of deletion ...
        result = False

        # find it ...
        node, parent = Node.find(self, None, key)

        if node is None:
            return result
        else:
            # found it ... what type of node?
            nrChildren = node.child_count()

            if nrChildren == 0:
                # ... it's a leaf node ...
                result = _delete_leaf(node, parent)
            elif nrChildren == 1:
                # it has a single child ...
                result = _delete_one(node, parent)
            else:  # nrChildren == 2
                result = _delete_two(node, parent)
        # give back if succeeded or not ...
        return result

    def traverse_tree_pre_order(self, visitor):
        """traverese tree pre-order mode and fire visitor on node"""

        # ... first, process the node ...
        visitor(self)

        # ... then left tree ...
        if self.left is not None:
            self.left.traverse_tree_pre_order(visitor)

        # ... finally, right tree...
        if self.right is not None:
            self.right.traverse_tree_pre_order(visitor)

    def traverse_tree_in_order(self, visitor):
        """traverese tree in-order mode and fire visitor on node"""

        # left tree first ...
        if self.left is not None:
            self.left.traverse_tree_in_order(visitor)

        # ... process the node in-order ...
        visitor(self)

        # ... right tree...
        if self.right is not None:
            self.right.traverse_tree_in_order(visitor)

    def traverse_tree_post_order(self, visitor):
        """traverese tree post-order mode and fire visitor on node"""

        # ... first, left tree ...
        if self.left is not None:
            self.left.traverse_tree_post_order(visitor)

        # ... then, right tree...
        if self.right is not None:
            self.right.traverse_tree_post_order(visitor)

        # ... finally, process the node ...
        visitor(self)


ROOT = ['Lars']  # we make this a list, to merge with other names
NAMES = [
    'Maze', 'Leon', 'John', 'Zack', 'Chuc', 'Pete', 'Lisa', \
    'Mary', 'Rodd', 'Bert', 'Sean', 'Will', 'Dora', 'Anna'
]
ALL_NAMES = NAMES + ROOT  # we can do this, because ROOT also a list


def make_bst():
    # add the root name ...
    a_bst = Node(ROOT[0])

    # add other names in addition to the root ...
    for name in NAMES:
        a_bst.insert(name)

    return a_bst


def print_tree_structure(tree, title='', header=True):
    """print tree nodes in a tree structure"""

    def _print_subtree(tree, level=0):
        if tree is None:
            return
        else:
            # walk down the right subtree first ...
            _print_subtree(tree.right, level + 1)
            # ... now print the node ...
            _print_node_at_level(tree, level)
            # ... and walk down the left subtree ...
            _print_subtree(tree.left, level + 1)

    def _print_node_at_level(node, level):
        TAB, SPACE = (6, ' ')
        line = '' + SPACE * (TAB * level) + str(node.data)
        print(line)

    if header == True:
        print_header(title, width=40)
    if tree is None:
        print('tree is None')
    # now start walking the tree and print ...
    _print_subtree(tree, level=0)


def print_nodes_sorted(tree, title='', header=True):
    """print tree nodes in order"""
    if header == True:
        print_header(title, width=40)
    if tree is None:
        print('print tree structure: cannot print None tree')
    else:
        # print the tree
        tree.traverse_tree_in_order(Node.printNode)
        print()


def print_header(title, banner=True, width=80):
    if banner == True:
        print(''.join(['-' for s in range(width)]))
    print(title)
    if banner == True:
        print(''.join(['-' for s in range(width)]))


def print_all_names(bst, namelist):
    if bst is None:
        return
    for name in namelist:
        node, parent = Node.find(bst, None, name)
        if node is None:
            print('{:s} not on tree'.format(str(name)))
        else:
            print('{:s} found: {:s}'. \
                  format(str(name), str(node.data)), end='')
            if parent is not None:
                print(' (child of: {:s})'.format(str(parent.data)))
            else:
                print(' (no parent)')


# Tests are down here...
def test_add_names():
    print_header('Test whether names end up correctly in the tree')
    bst = make_bst()

    # Create some names that are not in the tree
    NOT_ON_TREE = ['Jacques', 'Kit']
    TEST_LIST = ALL_NAMES + NOT_ON_TREE

    # For all names, display whether they are in the tree
    print_all_names(bst, TEST_LIST)

    # print all the nodes in order ...
    print_tree_structure(bst, 'bst after insertions')


## run the test ...
test_add_names()
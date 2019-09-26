""" 
Binary Tree

- A node in a BT has a val, left child, and right child.
- BT is represented by a root node.

Operations:
- add a node
- remove a node
- traversal

"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, val):
        self.root = Node(val)

    def inorder(self, root):
        """ Print items in in-order traversal """
        res = []
        if not root:
            return
        self.inorder(self.root.left)
        res.append(self.root.val)
        self.inorder(self.root.right)
        return res
    




# Tests

import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree(5)

    def test_inorder_traverse(self):
        actual = self.tree.inorder(self.tree.root)
        expected = [5]
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
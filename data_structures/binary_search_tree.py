""" 
Binary Search Tree

- A node in a BST has a val, left child, and right child.
- BST is represented by a root node.
- In a BST, all values in the left subtree < root value < values in right subtree (can have different variants)
- In this implementation, we don't allow duplicate value, i.e. nothing is changed if the value to be added is already present in the tree

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
    def __init__(self):
        self.root = None
        self.count = 0

    def add(self, val):
        """ Add a val to the BST. Modifies the tree and returns nothing. """
        def _add(val, root):
            if root is None:
                self.root = Node(val)
                self.count += 1
            else:
                if val < root.val:
                    if not root.left:
                        root.left = Node(val)
                        self.count += 1
                    else:
                        _add(val, root.left)
                if val > root.val:
                    if not root.right:
                        root.right = Node(val)
                        self.count += 1
                    else:
                        _add(val, root.right)
        
        _add(val, self.root)

    def inorder(self):
        """ Print items in in-order traversal - Recursive method"""
        res = []
        def _inorder(root, output):
            if root is None:
                return
            _inorder(root.left, output)
            output.append(root.val)
            _inorder(root.right, output)
        
        _inorder(self.root, res)
        return res
    
    def inorder_iterative(self):
        """ Print items in in-order traversal - Iterative method"""
        def _inorder_iterative(root):
            res = []
            stack = []
            while stack or root:
                while root:
                    stack.append(root)
                    root = root.left
                root = stack[-1]
                stack.pop()
                res.append(root.val)
                root = root.right
            return res
        return _inorder_iterative(self.root)




# Tests

import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree()
        self.tree.add(5)
        self.tree.add(4)
        self.tree.add(6)
    
    def test_add(self):
        self.assertEqual(3, self.tree.count)

        # Add 3 - count should be 4
        self.tree.add(3)
        self.assertEqual(4, self.tree.count)

        # duplicate - count should stay the same
        self.tree.add(5)
        self.assertEqual(4, self.tree.count)

    def test_inorder_traverse(self):
        actual = self.tree.inorder()
        expected = [4,5,6]
        self.assertSequenceEqual(actual, expected)

        self.tree.add(3)
        self.tree.add(7)
        actual = self.tree.inorder()
        expected = [3,4,5,6,7]
        self.assertSequenceEqual(actual, expected)

    def test_inorder_iterative(self):
        actual = self.tree.inorder_iterative()
        expected = [4,5,6]
        self.assertSequenceEqual(actual, expected)

        self.tree.add(2)
        self.tree.add(8)
        self.tree.add(5)
        actual = self.tree.inorder_iterative()
        expected = [2,4,5,6,8]
        self.assertSequenceEqual(actual, expected)

unittest.main(verbosity=2)
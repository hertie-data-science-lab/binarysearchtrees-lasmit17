# -*- coding: utf-8 -*-
"""
Created on Tue May 16 16:21:09 2023

@author: lasmi
"""

from treetemplate import Tree
from abc import ABC, abstractmethod

class BinaryTree(Tree):
    """Class representing a binary tree."""

    class Node:
        def __init__(self, element, parent=None, left=None, right=None):
            
            self.element = element
            self.parent = parent
            self.left = left
            self.right = right

    def __init__(self):
        self.root_node = None
        self.size = 0

    def root(self):
        return self.root_node

    def parent(self, p):
        return p.parent

    def left(self, p):
        return p.left

    def right(self, p):
        return p.right

    def num_children(self, p):
        count = 0
        if p.left is not None:
            count += 1
        if p.right is not None:
            count += 1
        return count

    def children(self, p):
        if p.left is not None:
            yield p.left
        if p.right is not None:
            yield p.right

    def __len__(self):
        return self.size

class BinarySearchTree(Tree):
    """Class representing a binary search tree."""

    class Node:
        def __init__(self, element, parent=None, left=None, right=None):
            self.element = element
            self.parent = parent
            self.left = left
            self.right = right

    def __init__(self):
        self.root_node = None
        self.size = 0

    def root(self):
        return self.root_node

    def parent(self, p):
        return p.parent

    def left(self, p):
        return p.left

    def right(self, p):
        return p.right

    def num_children(self, p):
        count = 0
        if p.left is not None:
            count += 1
        if p.right is not None:
            count += 1
        return count

    def children(self, p):
        if p.left is not None:
            yield p.left
        if p.right is not None:
            yield p.right

    def __len__(self):
        return self.size

    def insert(self, element):
        if self.root_node is None:
            self.root_node = self.Node(element)
            self.size = 1
        else:
            self._insert_recursive(element, self.root_node)

    def _insert_recursive(self, element, node):
        if element < node.element:
            if node.left is None:
                node.left = self.Node(element, parent=node)
                self.size += 1
            else:
                self._insert_recursive(element, node.left)
        elif element > node.element:
            if node.right is None:
                node.right = self.Node(element, parent=node)
                self.size += 1
            else:
                self._insert_recursive(element, node.right)

def convert_to_binary_search_tree(binary_tree):
    """
    Convert a binary tree into a binary search tree.

    Args:
        binary_tree: The binary tree to be converted.

    Returns:
        The resulting binary search tree.
    """
    def in_order_traversal(node, elements):
        if node is None:
            return
        in_order_traversal(node.left, elements)
        elements.append(node.element)
        in_order_traversal(node.right, elements)

    elements = []
    in_order_traversal(binary_tree.root(), elements)

    bst = BinarySearchTree()

    def build_bst(start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = bst.Node(elements[mid])
        left_child = build_bst(start, mid - 1)
        right_child = build_bst(mid + 1, end)
        node.left = left_child
        node.right = right_child

        if left_child is not None:
            left_child.parent = node
        if right_child is not None:
            right_child.parent = node

        return node

    bst.root_node = build_bst(0, len(elements) - 1)
    bst.size = len(elements)

    return bst


binary_tree = BinaryTree()
root = binary_tree.Node(5)
node2 = binary_tree.Node(3)
node3 = binary_tree.Node(7)
node4 = binary_tree.Node(2)
node5 = binary_tree.Node(4)
node6 = binary_tree.Node(6)
node7 = binary_tree.Node(8)

root.left = node2
root.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

binary_tree.root_node = root

bst = convert_to_binary_search_tree(binary_tree)

print(len(bst))
print(bst.root().element)  
print(bst.left(bst.root()).element)
print(bst.right(bst.root()).element)

def in_order_traversal(node):
    """
    Perform an in-order traversal of a binary tree.
    
    Args:
        node: The current node being visited.
        elements: A list to store the elements in the order of traversal.
    
    Returns:
        None
    """
    if node is None:
        return
    in_order_traversal(node.left)
    print(node.element)
    in_order_traversal(node.right)

in_order_traversal(bst.root())
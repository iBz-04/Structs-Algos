## QUESTION:
"""Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.

Note that the root node is at depth 1.

The adding rule is:

Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
cur's original left subtree should be the left subtree of the new left subtree root.
cur's original right subtree should be the right subtree of the new right subtree root.
If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree."""


##INTUITION:
"""Intuition
I solved it by adding a new row of nodes at a specified depth in a binary tree. If the specified depth is 1, 
the new nodes become the new root with the existing tree as their child."""

##APPROACH:
"""If the target depth (depth) is 1, I directly create a new root node with the given value val and set its left child to the original tree
. Otherwise, we'll recursively traverse the tree to the (depth - 1) level."""

##COMPLEXITY
#Time complexity:
### O(n), (n is the number of nodes in the tree)

#Space complexity:
### O(h), (h is the height of the tree)

## difficulty:
# medium

##CODE:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
       if depth == 1:
           return TreeNode(val, left=root)

       def traverse(node, depth_left):
           if node is None:
               return
           if depth_left == 1:
               old_left = node.left
               old_right = node.right

               node.left = TreeNode(val, left=old_left)
               node.right = TreeNode(val, right=old_right)  

               return
           traverse(node.left, depth_left - 1)     
           traverse(node.right, depth_left - 1)

       traverse(root, depth - 1)
       return root
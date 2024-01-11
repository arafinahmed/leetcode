from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        nodes = []
        max_diff = 0
        def traverse(node):
            if not node: return
            nodes.append(node)
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        
        def findmax(node, value):
            if not node: return
            max_diff = max(max_diff, abs(node.val - value))
            findmax(node.left, value)
            findmax(node.right, value)

        for node in nodes:
            findmax(node, node.val)

        return max_diff
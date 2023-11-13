from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(root, h):
            if not root:
                return h
            return max(depth(root.left, h+1), depth(root.right, h+1))
        
        return depth(root, 0)
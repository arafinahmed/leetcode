from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')
        self.helper(root)
        return self.maxSum
    
    def helper(self, root):
        if not root:
            return 0
        
        left = max(0, self.helper(root.left))
        right = max(0, self.helper(root.right))

        self.maxSum = max(self.maxSum, left + right + root.val)

        return max(left, right) + root.val



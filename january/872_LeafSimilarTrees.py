from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        values = []

        def dfs_1(node):
            if not node: return

            dfs_1(node.left)

            if not node.left and not node.right:
                values.append(node.val)
            
            dfs_1(node.right)

        def dfs_2(node):
            if not node: return

            dfs_2(node.left)

            if not node.left and not node.right:
                front = values.pop(0)
                if (front and front != node.val) or not front:
                    return False


            dfs_2(node.right)

        dfs_1(root1)
        dfs_2(root2)
        if values[0] == -22:
            return True
        return False
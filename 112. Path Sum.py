from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, currentSum):

            if not node:  # empty tree edge case
                return False

            currentSum += node.val
            if not node.left and not node.right:  # has not children
                return currentSum == targetSum

            return (dfs(node.left, currentSum) or dfs(node.right, currentSum))
        return dfs(root, 0)

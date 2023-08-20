from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        # recursive solution
        # linear time algo

        def dfs(root):
            if not root:  # if the root is null you wna tit to be -1 because you add 1 to it
                return -1
            left = dfs(root.left)  # finding the height
            right = dfs = (root.right)  # find the height

            # find the diameters, update if its more than previous max
            res[0] = max(res[0], 2 + left + right)

            return 1 + max(left+right)  # height running through the root node
        dfs(root)
        return res

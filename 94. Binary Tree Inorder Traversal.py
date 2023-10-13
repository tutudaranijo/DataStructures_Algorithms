from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# * recursive solution


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:

        res = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)  # right subtree

        inorder(root)
        return res
# * iterative solution


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:

        res = []
        stack = []
        cur = root

        while cur or stack:  # while stack is null or cur is null
            while cur:
                stack.append(cur)
                cur = cur.left  # left as far as we can
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right

        return res

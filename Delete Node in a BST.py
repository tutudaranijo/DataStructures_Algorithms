from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # base case
        if not root:
            return root
        # find node we want to delete
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:  # we found the node we want to delete
            if not root.left:  # left subtree is null return right
                return root.right
            elif not root.right:  # right subtree is null right left
                return root.left

        # min from right subtree

            cur = root.right
            while cur.left:  # should keep going to min in right subtree
                cur = cur.left
            root.val = cur.val
            root.right = self.deleteNode(root.right, cur.val)
        return root

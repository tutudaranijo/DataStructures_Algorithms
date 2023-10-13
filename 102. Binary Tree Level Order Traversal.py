from typing import Optional
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:

        res = []

        q = collections.deque()  # get a queue

        q.append(root)

        while q:
            qlen = len(q)  # make sure we go through one level at a time
            level = []
            for i in range(qlen):
                node = q.popleft()
                if node:  # node if null
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:  # make sure level non empty
                res.append(level)
        return res

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursive solution
        if not root:
            return 0

        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))


class SolutionBFS:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS solution
        if not root:
            return 0

        level = 0  # start level
        q = deque([root])
        while q:
            # * traverse the entry level - add the children delete the root
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level


class SolutionIT:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS solution

        stack = [[root, 1]]
        res = 0
        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res

# Definition for a binary tree node.
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        res =[]

        q = collections.deque()

        q.append(root)

        while q: 
            qLen= len(q)
            print(' Queue Length: qLen:', qLen)
            level = []
            for i in range(qLen):
                print('The Value of I:', i)
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res

if __name__ == "__main__":
    # Create the first tree
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)
    tree1.left.left = TreeNode(6)
    tree1.right.right = TreeNode(7)
    tree1.left.right = TreeNode(8)
    tree1.right.left = TreeNode(9)



    # Create an instance of the Solution class
    solution = Solution()

    # Check if the trees are the same
    result = solution.levelOrder(tree1)
    print("Levels of Tree", result)         
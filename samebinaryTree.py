# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and 
        self.isSameTree(p.right, q.right))
    
        
        

# Example usage
if __name__ == "__main__":
    # Create the first tree
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)

    # Create the second tree
    tree2 = TreeNode(1)
    tree2.left = TreeNode(2)
    tree2.right = TreeNode(3)

    # Create an instance of the Solution class
    solution = Solution()

    # Check if the trees are the same
    result = solution.isSameTree(tree1, tree2)
    print("Are the trees the same?", result)  # Output: True
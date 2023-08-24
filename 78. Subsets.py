class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):  # greater than length out of bounds so return
                res.append(subset.copy())  # subset is going to be modify
                return

            # decisions to include nums [i] # left decision tree
            subset.append(nums[i])
            dfs(i+1)

            # decisions not to include nums[i]
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res

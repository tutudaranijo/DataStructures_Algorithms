class Solution:
    # Time and Memory O(n)
    def removeDuplicates(self, nums: list[int]) -> int:
        prevMap = {}
        delList = []
        for i, n in enumerate(nums):
            if n in prevMap:
                delList.append(i)
            prevMap[n] = i
        delList = delList[::-1]
        for j in delList:
            nums.pop(j)
        numsLength = len(nums)
        return numsLength

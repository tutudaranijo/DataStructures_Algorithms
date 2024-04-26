from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        res = 0
        onePointer, TwoPointer = 0,1



        while onePointer < len(nums):
            if TwoPointer == len(nums):
                onePointer += 1
                TwoPointer= onePointer + 1
            else:
                if nums[onePointer] + nums[TwoPointer] < target  :
                    res += 1
                    TwoPointer += 1
                
                else  :
                    onePointer += 1
                    TwoPointer= onePointer + 1
        return res
        

# Test the function
solution = Solution()
nums = [6, -1, 7, 4, 2, 3]
target = 8
result = solution.countPairs(nums, target)
print(f"Total Pairs: {result}")
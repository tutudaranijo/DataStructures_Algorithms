class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        numset= set(nums)
        longest = 0

        for n in nums:
            # check for left neigbor by checking if its a start

            if ( n-1) not in numset:
                length = 0
                while (n + length) in numset:
                    length += 1
                longest = max(length,longest)
        return longest
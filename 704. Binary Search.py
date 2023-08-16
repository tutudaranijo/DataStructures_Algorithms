class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r, = 0, len(nums)-1
# * log(n)
        while l <= r:
            m = (l+r) // 2  # mid way
            if nums[m] > target:  # num is greater than target move to left once
                r = m-1
            elif nums[m] < target:
                l = m+1  # midpoint lless than move to the right
            else:
                return m  # means there no more or target is found
        return -1  # go past it so need one behind

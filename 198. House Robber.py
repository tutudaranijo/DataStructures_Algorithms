class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1, rob2 = 0, 0
        # * rob 2 is the last house
        # * rob 1 is the second to last house
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

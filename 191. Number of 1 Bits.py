class Solution:
    def hammingWeight(self, n: int) -> int:
        # O(1) - TIme complexity
        res = 0

        while n > 0:
            res += n % 2  # * if it = 1 then increment by one
            n = n >> 1  # shift the result
        return res

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1  # shift ot the right for ith bit
            res = res | (bit << (31 - i))  # or bit to put in output
        return res

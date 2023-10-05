def guess(num: int) -> int:
    num


class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n

        while True:  # * greenteed to find solution
            m = (l+r)//2
            res = guess(m)
            if res > 0:
                l = m + 1
            elif res < 0:
                r = m - 1
            else:
                return m

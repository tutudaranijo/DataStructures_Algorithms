class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        l, r = 0, 1  # ! left but right sell
        maxp = 0  # * max price

        while r < len(prices):  # r prices cannot pass the length of prices

            # ? profitable
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxp = max(maxp, profit)
            else:
                l = r  # only updates if profit doesnt increase or no profit
            r += 1  # right updates not matter what
        return maxp

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:

        cost.append(0)
        # -3 means -3 third to last to mention there are to steps to go
        # -1 loop continues til it reach -1
        # -1 loops in reverse order
        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+2], cost[i+1])
        # * cost[0] starts at very beginning and cost[1] starts at second step
        return min(cost[0], cost[1])

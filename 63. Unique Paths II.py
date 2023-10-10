class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        # * dynamic programming example
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * N  # dp row
        dp[N-1] = 1  # last value is 1

        for r in reversed(range(M)):
            for c in reversed(range(N)):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                elif c + 1 < N:
                    dp[c] = dp[c] + dp[c+1]  # bottom , to the right
        return dp[0]


class recursiveSolution:
    def recursiveuniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        # * time: O(N*M) Space: O(N*M)
        M, N = len(grid), len(grid[0])  # dimension of the grid

        dp = {(M-1, N-1): 1}  # cache

        def dfs(r, c):
            if r == M or c == N or grid[r][c]:  # go out bounce or block
                return 0
            if (r, c) in dp:  # already got the value in that position
                return dp[(r, c)]
            dp[(r, c)] = dfs(r+1, 2) + dfs(r, c+1)  # dfs
            return dp[(r, c)]
        return dfs(0, 0)

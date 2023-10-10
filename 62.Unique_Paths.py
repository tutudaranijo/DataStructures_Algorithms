class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):  # all rows but last
            # new row above the row # last value in every column is 1
            newRow = [1] * n
            # go from the second to last position  , keep going to you get to the beg, in reverse order
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        return row[0]

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1

        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1  # * larger values
            elif target < matrix[row][0]:
                bot = row - 1  # smaller values
            else:
                break

        if not (top <= bot):  # * none of the rows contained target value
            return False

        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l+r) // 2
            if target > matrix[row][m]:
                l = m + 1  # * shift right
            elif target < matrix[row][m]:
                r = m-1  # * shift left
            else:
                return True
        return False

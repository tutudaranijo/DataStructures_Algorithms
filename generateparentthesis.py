class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
         # only add open parathesis if open < n
         # only add a closing parathesis if closed < open
         # valid IIF open == closed == n

         # recursive

        stack = []

        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack)) # join them into a empty string and append to result
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        backtrack(0,0)

        return res

class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []  # initailza a stack

        for op in operations:
            if op == "+":
                # * adding the last two values
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(2*stack[-1])  # * 2 times the last number in stack
            elif op == "C":
                stack.pop()  # * delete from the stack
            else:
                stack.append(int(op))  # * return the int if its a int
        return sum(stack)
        #! time and memory O(n)

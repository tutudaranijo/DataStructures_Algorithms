class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # ! mapping the close to open parentheses
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in closeToOpen:  # * check if its a close parentheses
                # * stack is not empty and value is matching open parentheses
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()  # delete is they match
                else:
                    return False  # dont match
            else:
                stack.append(c)  # add to list if its open parentheses

        return True if not stack else False


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)

        stack=[] # pair: [temp , temp]

        for i , t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd ] = (i - stackInd)
            stack.append([t,i])
        return res

    
temperatures = [73,74,75,71,69,72,76,73]
test=Solution().dailyTemperatures(temperatures)
print(test)
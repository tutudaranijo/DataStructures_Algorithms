class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer=[]
        temp = 0
        nexttemp =1
        res =0
        while temp < len(temperatures) or   nexttemp < len(temperatures):

            if temperatures[temp] < temperatures[nexttemp] :
                nexttemp +=1
                res +=1
            else:
                answer.append(res)
                temp += 1
                nexttemp = temp +1
                res=0
        return answer
    
temperatures = [73,74,75,71,69,72,76,73]
test=Solution().dailyTemperatures(temperatures)
print(test)
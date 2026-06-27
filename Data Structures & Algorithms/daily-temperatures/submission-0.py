class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = [] #pair of temp and index

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                dayTemp,dayInd = stack.pop()
                res[dayInd] = i - dayInd

            stack.append([t,i])
        return res

            
                   
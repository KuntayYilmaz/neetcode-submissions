class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        i = len(cost)

        res = 0
        while i > 1:
            if cost[i-2] > cost[i-1]:
                res += cost[i-1]
                i = i - 1
            else:
                res += cost[i-2]
                i = i - 2
        
        return res
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1

        maxSoFar = 0

        while L < R:
            currentAmount = (R - L) * min(heights[R],heights[L])
            if currentAmount > maxSoFar:
                maxSoFar = currentAmount

            if heights[R] > heights[L]:
                L += 1
            else:
                R += -1
            

        return maxSoFar    
        

        
class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height) 
        maxRight = [0] * len(height)

        maxSoFar = 0
        for i in range(len(height) - 1):
            
            if height[i] > maxSoFar:
                maxSoFar = height[i]

            maxLeft[i+1] = maxSoFar


        maxSoFar = 0
        for i in range(len(height) - 1,0,-1):
            
            if height[i] > maxSoFar:
                maxSoFar = height[i]

            maxRight[i-1] = maxSoFar

        output = 0

        for i, a in enumerate(height):
            output += max(0,min(maxLeft[i],maxRight[i]) - a)

        return output

            
        
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        length = len(heights)
        stack = []
        maxSoFar = 0

        for index, height in enumerate(heights):
            if not stack:
                stack.append([index,height])
            elif height < stack[-1][1]:
                while stack and height < stack[-1][1]:
                    element_removed = stack.pop()
                    area = (index - element_removed[0]) * element_removed[1]
                    if area > maxSoFar:
                        maxSoFar = area
                stack.append([element_removed[0],height])
            else:
                stack.append([index,height])

        if stack:
            for index, height in stack:
                area = height * (length - index)
                if area > maxSoFar:
                    maxSoFar = area
        
        return maxSoFar


            
         
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0 , len(matrix) - 1
        if not len(matrix) == 1:
            while (low+1) != high:
                mid = (low + high) // 2
                if matrix[mid][0] == target:
                    return True

                if target < matrix[mid][0]:
                    high = mid
                elif target > matrix[mid][0]:
                    low = mid

            if target >= matrix[high][0]:
                target_row = high
            else:
                target_row = low
        else:
            target_row = 0
        
        #Binary Search on a Single Row
        low, high = 0, len(matrix[0])-1
            
        while low <= high:
            mid = (low + high) // 2
            a = matrix[target_row][mid]
            if a > target:
                high = mid - 1
            elif a < target:
                low = mid + 1
            else:
                return True

        return False
        
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = m
        cols = n

        prewRow = [0] * cols
        curRow = [0] * cols
        curRow[-1] = 1

        for r in range(rows - 1,-1,-1):
            for c in range(cols - 2,-1,-1):
                curRow[c] = curRow[c+1] + prewRow[c]

            prewRow = curRow
        
        return prewRow[0]
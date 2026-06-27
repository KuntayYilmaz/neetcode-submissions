class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, r, c, visit):
            ROWS, COLS = len(grid), len(grid[0])
            if(min(r,c) < 0 or
                r == ROWS or c == COLS or 
                (r, c) in visit or grid[r][c] == 0):
                return 0
            #Then this is a new valid 1 grid
            visit.add((r,c))

            count = 1
            count += dfs(grid, r + 1, c, visit)
            count += dfs(grid, r - 1, c, visit)
            count += dfs(grid, r, c + 1, visit)
            count += dfs(grid, r, c - 1, visit)

            return count

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        max_count = 0
        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if(grid[r][c] == 1 and (r,c) not in visit):
                    count = dfs(grid,r,c,visit)
                    if count > max_count:
                        max_count = count
        return max_count
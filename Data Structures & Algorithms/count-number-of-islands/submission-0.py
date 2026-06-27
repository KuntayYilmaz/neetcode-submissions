class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, r, c, visit):
            ROWS, COLS = len(grid), len(grid[0])
            if(min(r,c) < 0 or
                r == ROWS or c == COLS or 
                (r, c) in visit or grid[r][c] == "0"):
                return
            #Then this is a new valid 1 grid
            visit.add((r,c))

            dfs(grid, r + 1, c, visit)
            dfs(grid, r - 1, c, visit)
            dfs(grid, r, c + 1, visit)
            dfs(grid, r, c - 1, visit)

            return

        ROWS, COLS = len(grid), len(grid[0])
        n_island = 0
        visit = set()
        for r in range(ROWS):
            for c in range(COLS):
                if(grid[r][c] == "1" and (r,c) not in visit):
                    n_island += 1
                    dfs(grid,r,c,visit)
        return n_island

            
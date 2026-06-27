class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        que = deque()
        num_fresh = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    que.append((i,j))
                if grid[i][j] == 1:
                    num_fresh += 1
        if num_fresh == 0:
            return 0
            
        print(num_fresh)
        mins_passed = -1

        while que:
            for i in range(len(que)):
                r,c = que.popleft()
                for dr,dc in directions:
                    if min(r+dr,c+dc) < 0 or r+dr >= ROWS or c+dc >= COLS:
                        continue
                    if grid[r+dr][c+dc] == 1:
                        grid[r+dr][c+dc] = 2
                        num_fresh -= 1
                        que.append((r+dr,c+dc))
            mins_passed += 1

        if num_fresh == 0:
            return mins_passed
        return -1


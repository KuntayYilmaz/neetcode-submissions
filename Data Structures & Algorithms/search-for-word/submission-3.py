class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        n = len(word)
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(r,c,idx):
            if idx == n:
                nonlocal result
                result = True
                return
            
            for dr,dc in directions:
                if (r+dr,c+dc) not in visited and min(r+dr,c+dc) > -1 and r+dr < ROWS and c+dc < COLS and board[r+dr][c+dc] == word[idx]:
                    visited.add((r+dr,c+dc))
                    dfs(r+dr,c+dc,idx+1)
                    visited.remove((r+dr,c+dc))
                    
            
        result = False
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    visited = set()
                    visited.add((r,c))
                    dfs(r,c,1)
        
        return result

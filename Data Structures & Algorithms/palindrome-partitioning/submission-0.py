class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr_subset = []
        n = len(s)
        dp_array = [[True] * n for _ in range(n)]
        for i in range(1,n):
            for j in range(n-i):
                if s[j] == s[j+i] and dp_array[j+1][j+i-1]:
                    continue
                else:
                    dp_array[j][j+i] = False

        def dfs(l,r):
            if l == n:
                res.append(curr_subset.copy())
                return
            if r == n:
                return
            
            if dp_array[l][r]:
                curr_subset.append(s[l:r+1])
                dfs(r+1,r+1)
                curr_subset.pop()
            
            dfs(l,r+1)
        
        dfs(0,0)

        return res
            

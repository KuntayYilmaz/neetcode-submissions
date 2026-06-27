class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        unused = set()
        res = []
        curr_permute = []
        for num in nums:
            unused.add(num)
        
        def dfs():
            if not unused:
                res.append(curr_permute.copy())
                return
                    
            snapshot = list(unused)
            for num in snapshot:
                curr_permute.append(num)
                unused.remove(num)
                dfs()
                curr_permute.pop()
                unused.add(num)

        dfs()
        return res
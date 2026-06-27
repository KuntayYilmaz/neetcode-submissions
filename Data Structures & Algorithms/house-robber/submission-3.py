class Solution:
    def rob(self, nums: List[int]) -> int:

        n_house = len(nums)
        cache = {}

        def dfs(i):
            if i >= n_house:
                return 0
            
            if i not in cache:
                cache[i] = max(nums[i] + dfs(i+2), dfs(i+1))

            return cache[i]

        return dfs(0)
        
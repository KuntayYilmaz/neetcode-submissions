class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        def dfs(curr_subset,idx):
            if idx == n:
                result.append(curr_subset.copy())
                return
            
            dfs(curr_subset.copy(),idx+1)
            curr_subset.append(nums[idx])
            dfs(curr_subset.copy(),idx+1)

        dfs([],0)
        return result
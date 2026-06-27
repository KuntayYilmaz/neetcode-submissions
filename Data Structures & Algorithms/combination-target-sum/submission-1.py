class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr_comb = []
        res = []

        def dfs(idx,curr_sum):
            if curr_sum == target:
                res.append(curr_comb.copy())
                return
            if idx >= len(nums) or curr_sum > target:
                return

            curr_comb.append(nums[idx])
            dfs(idx,curr_sum+nums[idx])
            
            curr_comb.pop()
            dfs(idx+1,curr_sum)

        dfs(0,0)

        return res



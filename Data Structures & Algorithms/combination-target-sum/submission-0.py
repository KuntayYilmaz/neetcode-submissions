class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        currComb = []

        def helper(i):
            if sum(currComb) == target:
                result.append(currComb.copy())
                return
            if sum(currComb) > target:
                return

            for j in range(i,len(nums)):
                currComb.append(nums[j])
                helper(j)
                currComb.pop()
        
        helper(0)
        return result
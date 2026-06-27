class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        currComb = []

        def helper(i,total):
            if total == target:
                result.append(currComb.copy())
                return
            if total > target or i == len(candidates):
                return

            currComb.append(candidates[i])
            helper(i+1, total + candidates[i])
            currComb.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1            
            helper(i+1,total)

        helper(0,0)
        return result
        
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        currComb = []

        def helper(i):
            if sum(currComb) == target:
                if currComb not in result:
                    result.append(currComb.copy())
                return
            if sum(currComb) > target:
                return

            for j in range(i,len(candidates)):
                currComb.append(candidates[j])
                helper(j+1)
                currComb.pop()
        
        helper(0)
        return result
        
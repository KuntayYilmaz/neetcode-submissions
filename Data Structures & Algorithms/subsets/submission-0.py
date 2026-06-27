class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curSet, resultSet = [], []
        self.helper(0,nums,curSet,resultSet)
        return resultSet

    def helper(self,i,nums,curSet,resultSet):
        if i >= len(nums):
            resultSet.append(curSet.copy())
            return
        
        curSet.append(nums[i])
        self.helper(i+1,nums,curSet,resultSet)
        curSet.pop()
        self.helper(i+1,nums,curSet,resultSet)


        
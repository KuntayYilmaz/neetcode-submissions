class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float("-inf")
        currSum = 0
        L = 0

        for R in range(len(nums)):
            if currSum < 0:
                L = R
                currSum = 0
            currSum += nums[R]
            maxSum = max(maxSum,currSum)

        return maxSum
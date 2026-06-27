class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        out = [1] * len(nums)
        #nums = [1,2,4,6]
        #suffix = [1,1,2,8]
        #prefix = [48,24,6,1]

        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        for i in range(len(nums)):
            out[i] = suffix[i] * prefix[i]
        
        return out
        
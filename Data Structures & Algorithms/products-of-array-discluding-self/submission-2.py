class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        prefix = [0] * n
        postfix = [0] * n
        output = [0] * n

        prefix[0] = nums[0]
        postfix[n - 1] = nums[n - 1]

        for i in range(n-1):
            prefix[i+1] = prefix[i] * nums[i+1] 

        for i in range(n-1,0,-1):
            postfix[i-1] = postfix[i] * nums[i-1]

        output[0] = postfix[1]
        output[n - 1] = prefix[n - 2]

        for i in range(n-2):
            output[i+1] = prefix[i] * postfix[i+2] 
        
        return output

        
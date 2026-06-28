class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3
        for num in nums:
            counts[num] += 1
        ptr = 0
        for i in range(len(nums)):
            while(counts[ptr] == 0):
                ptr += 1
            nums[i] = ptr
            counts[ptr] -= 1


        # nums = [1,0,1,2]
        # out  = [0,1,1,2]
        
        # counts = [1,2,1]
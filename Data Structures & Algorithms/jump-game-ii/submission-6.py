class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        result = 1
        curr_place = 0

        while curr_place + nums[curr_place] < len(nums) - 1:
            curr_place = max([ (curr_place+i+nums[curr_place + i],curr_place+i) for i in range(1,min(nums[curr_place]+1,len(nums)-curr_place))] )[1]
            result += 1

        return result
        
                
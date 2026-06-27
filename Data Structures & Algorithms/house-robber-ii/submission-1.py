class Solution:
    def rob(self, nums: List[int]) -> int:
        nums1 = nums[1:]
        nums2 = nums[:-1]

        if len(nums) == 1:
            return nums[0]

        rob1,rob2 = 0,0
        for n in nums1:
            tmp = max(rob1 + n,rob2)
            rob1 = rob2
            rob2 = tmp

        rob3,rob4 = 0,0
        for n in nums2:
            tmp = max(rob3 + n,rob4)
            rob3 = rob4
            rob4 = tmp

        return max(rob4,rob2)

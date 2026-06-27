class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0],nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        new_slow = nums[0]

        while new_slow != slow:
            slow = nums[slow]
            new_slow = nums[new_slow]

        return slow
        


        
        
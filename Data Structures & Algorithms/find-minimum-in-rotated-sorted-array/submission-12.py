class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1
    
        while l <= r:
            mid = (l + r) // 2
            if nums[l] < nums[r]:
                r = mid
            elif nums[l] > nums[r]:
                if l == mid:
                    l = r
                else:
                    l += 1
            else:
                return nums[mid]

        return nums[mid]

        
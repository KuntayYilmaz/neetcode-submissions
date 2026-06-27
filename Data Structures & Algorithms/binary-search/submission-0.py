class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L,R = 0, len(nums)-1

        while L <= R:
            mid = (L + R) // 2
            a = nums[mid]
            if a > target:
                R = mid - 1
            elif a < target:
                L = mid + 1
            else:
                return mid
        return -1
        
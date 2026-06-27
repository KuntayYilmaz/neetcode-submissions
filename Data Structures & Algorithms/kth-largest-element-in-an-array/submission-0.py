class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-1 * num for idx,num in enumerate(nums)]
        heapq.heapify(nums)
        for _ in range(k-1):
            heapq.heappop(nums)

        return -heapq.heappop(nums)
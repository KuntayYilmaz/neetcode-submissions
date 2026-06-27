class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)

        biggestSoFar = 0

        for i in range(len(nums)):
            n = nums[i]
            counter = 0
            while(n in hashset):
                counter += 1
                n += 1
            if counter > biggestSoFar:
                biggestSoFar = counter

        return biggestSoFar


        
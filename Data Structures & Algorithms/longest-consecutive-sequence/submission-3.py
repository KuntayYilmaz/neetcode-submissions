class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)

        biggestSoFar = 0

        for n in hashset:
            if n - 1 not in hashset:
                counter = 0
                while(n + counter in hashset):
                    counter += 1
                if counter > biggestSoFar:
                    biggestSoFar = counter
        return biggestSoFar


        
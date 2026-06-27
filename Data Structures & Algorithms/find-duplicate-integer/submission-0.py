class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashset = set()

        for a in nums:
            if a in hashset:
                return a
            else:
                hashset.add(a)

        
        
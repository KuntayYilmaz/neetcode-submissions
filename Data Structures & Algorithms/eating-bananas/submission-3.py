class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)

        while l < r:
            mid = (l + r) // 2
            hour = 0
            for n in piles:
                hour += (n + mid - 1) // mid

            if hour > h:
                l = mid + 1
            else:
                r = mid
        return l
        
            

        

        
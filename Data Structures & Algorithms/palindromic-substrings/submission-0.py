class Solution:
    def countSubstrings(self, s: str) -> int:

        count = 0
        for i in range(len(s)):
            count += 1
            l,r = i-1,i+1
            while l > -1 and r < len(s) and s[l] == s[r]:
                count += 1
                l += -1
                r += 1

        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                count += 1
            l,r = i-1,i+2
            while l > -1 and r < len(s) and s[l] == s[r]:
                count += 1
                l += -1
                r += 1

        return count
            
            
            
        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        hashmap = defaultdict(int)
        s = list(s)
        l,r = 0,0
        while r < len(s):
            hashmap[s[r]] += 1
            while len(hashmap) != (r-l + 1):
                hashmap[s[l]] -= 1
                if hashmap[s[l]] == 0:
                    del hashmap[s[l]]
                l += 1
                 
            maxLength = max(maxLength,r-l+1)
            r += 1
        
        return maxLength
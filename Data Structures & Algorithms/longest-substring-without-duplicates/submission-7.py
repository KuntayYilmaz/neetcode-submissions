class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, longest, R = 0, 0, 0
        hashset = set()
        while R < len(s):
            if s[R] not in hashset:
                hashset.add(s[R])
                longest = max(longest,R-L+1)
            else:
                while s[R] in hashset:
                    hashset.remove(s[L])
                    L += 1
                hashset.add(s[R])
            R += 1

        return longest

            
        
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {}

        L = 0
        longest = 0

        for R in range(len(s)):

            char_count[s[R]] = char_count.get(s[R], 0) + 1
            most_freq = max(char_count.values())
            
            while (R-L+1) - most_freq > k:
                char_count[s[L]] -= 1
                L += 1

            longest = max(longest,R-L+1)

        return longest

        
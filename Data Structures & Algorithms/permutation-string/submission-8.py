class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = {}

        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1

        window = {}
        L = 0

        window_size = len(s1)

        for R in range(len(s2)):
            window[s2[R]] = window.get(s2[R], 0) + 1
            if R - L + 1 == window_size:

                if window == s1_count:
                    return True 

                window[s2[L]] -= 1
                if window[s2[L]] == 0:
                    del window[s2[L]]
                L += 1
    
            
        return False
        
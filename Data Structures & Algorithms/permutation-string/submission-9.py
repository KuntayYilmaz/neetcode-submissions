class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = {}
        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1

        window = {}
        L = 0
        matches = 0  # Count of matching characters
        window_size = len(s1)

        for R in range(len(s2)):
            # Add the new character to the window
            window[s2[R]] = window.get(s2[R], 0) + 1
            
            # Check if we matched the character count
            if window[s2[R]] == s1_count.get(s2[R], 0):
                matches += 1
            
            # When we hit the size of s1, check for matches
            if R - L + 1 == window_size:
                # Check if we matched all characters
                if matches == len(s1_count):
                    return True 

                # Remove the leftmost character from the window
                if window[s2[L]] == s1_count.get(s2[L], 0):
                    matches -= 1
                window[s2[L]] -= 1
                if window[s2[L]] == 0:
                    del window[s2[L]]
                L += 1
    
        return False

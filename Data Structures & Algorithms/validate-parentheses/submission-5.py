class Solution:
    def isValid(self, s: str) -> bool:
        
        hashmap = {')':'(',']':'[','}':'{'}
        stack = []

        len_s = len(s)
        for i in range(len_s):
            if s[i] in hashmap: 
                if not stack:
                    return False
                elif stack.pop() != hashmap[s[i]]:
                    return False
            else: 
                stack.append(s[i])

        return not stack


        
        

        


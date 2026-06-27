class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits):
            return []
        res = []
        curr_chars = []
        digits_to_chars = {"2":['a','b','c'],"3":['d','e','f'],"4":['g','h','i'],"5":['j','k','l'],"6":['m','n','o'],"7":['p','q','r','s'],"8":['t','u','v'],"9":['w','x','y','z']}

        def dfs(idx):
            if idx == len(digits):
                res.append("".join(curr_chars.copy()))
                return
            
            for c in digits_to_chars[digits[idx]]:
                curr_chars.append(c)
                dfs(idx+1)
                curr_chars.pop()
        
        dfs(0)
        return res
            

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper_recursive(open,close):
            if close > open:
                return
            if open > n:
                return
            if open + close == 2 * n:
                result.append("".join(curr_string))
            
            curr_string.append("(")
            helper_recursive(open+1,close)
            curr_string.pop()
            
            curr_string.append(")")
            helper_recursive(open,close+1)
            curr_string.pop()

        curr_string = []
        result = []
        helper_recursive(0,0)
        return result
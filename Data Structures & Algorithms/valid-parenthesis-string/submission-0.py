class Solution:
    def checkValidString(self, s: str) -> bool:
        star_count = 0
        stack = []
        left_matched = 0

        for char in s:
            if char == "(":
                stack.append("(")
            elif char == ")":
                if stack:
                    stack.pop()
                elif star_count > 0:
                    star_count -= 1
                elif left_matched > 0:
                    left_matched -= 1
                else:
                    return False
            elif char == "*":
                if stack:
                    star_count += 1
                    left_matched += 1
                    stack.pop()
                else:
                    star_count += 1
        if stack:
            return False
        return True
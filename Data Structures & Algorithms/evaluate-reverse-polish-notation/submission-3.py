class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for i in range(len(tokens)):
            
            if tokens[i] == '/' :
                l_int = stack.pop()
                r_int = stack.pop()
                stack.append(int(r_int / l_int))
            elif tokens[i] == '+':
                l_int = stack.pop()
                r_int = stack.pop()
                stack.append(r_int + l_int)
            elif tokens[i] == '-':
                l_int = stack.pop()
                r_int = stack.pop()
                stack.append(r_int - l_int)
            elif tokens[i] == '*':
                l_int = stack.pop()
                r_int = stack.pop()
                stack.append(r_int * l_int)
            else:
                stack.append(int(tokens[i]))

        return stack[0]

            

            

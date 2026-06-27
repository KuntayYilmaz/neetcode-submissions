class MinStack:

    def __init__(self):
        self.stack = []
        self.mins_Stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.mins_Stack.append(val)
        elif self.mins_Stack[-1] >= val:
            self.mins_Stack.append(val)
            self.stack.append(val)
        else:
            self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.mins_Stack[-1]:
            self.mins_Stack.pop(-1)

        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        

        return self.mins_Stack[-1]

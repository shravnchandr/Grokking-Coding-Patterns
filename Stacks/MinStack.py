class MinStack:

    def __init__(self):
        self.normal_stack, self.min_stack = list(), list()

    def push(self, value: int) -> None:
        if self.min_stack:
            if self.min_stack[-1] >= value:
                self.min_stack.append(value)
        else:
            self.min_stack.append(value)

        self.normal_stack.append(value)

    def pop(self) -> None:
        if self.normal_stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()
            

    def top(self) -> int:
        return self.normal_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
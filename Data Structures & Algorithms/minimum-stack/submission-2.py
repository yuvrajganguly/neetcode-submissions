class MinStack:

    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.stack2:
            self.stack2.append(val)
        elif val <= self.stack2[-1]:
            self.stack2.append(val)
        

    def pop(self) -> None:
        if self.stack[-1] == self.stack2[-1]:
            self.stack2.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack2[-1]

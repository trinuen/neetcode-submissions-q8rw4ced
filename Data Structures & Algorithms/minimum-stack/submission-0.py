class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.insert(0, val)
        if self.min_stack:
            min_val = min(val, self.min_stack[0])
            self.min_stack.insert(0, min_val)
        else:
            self.min_stack.insert(0, val)

    def pop(self) -> None:
        self.stack.pop(0)
        self.min_stack.pop(0)

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        return self.min_stack[0]

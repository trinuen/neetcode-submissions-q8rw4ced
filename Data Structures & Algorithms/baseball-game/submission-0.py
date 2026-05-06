class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = 0
        stack = []
        for op in operations:
            if op == "+":
                num_a = stack.pop()
                num_b = stack.pop()
                stack.append(num_b)
                stack.append(num_a)
                stack.append(num_a + num_b)
            elif op == "C":
                stack.pop()
            elif op == "D":
                stack.append(stack[-1]*2)
            else:
                stack.append(int(op))
        return sum(stack)
class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = {"}": "{", ")": "(", "]": "["}
        stack = []

        if len(s) % 2 == 1:
            return False
        
        for char in s:
            if char not in brackets:
                stack.append(char)
            else:
                if stack and brackets[char] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return not stack and True
        
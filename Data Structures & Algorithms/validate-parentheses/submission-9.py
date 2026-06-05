class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"}": "{", "]": "[", ")": "("}
        for bracket in s:
            #check opening bracket
            if bracket not in brackets:
                stack.append(bracket)
            #check closing bracket
            else:
                if stack and stack[-1] == brackets[bracket]:
                    stack.pop()
                else:
                    return False
        return True and not stack
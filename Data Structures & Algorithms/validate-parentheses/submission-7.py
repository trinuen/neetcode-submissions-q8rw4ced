class Solution:
    def isValid(self, s: str) -> bool:

        brackets = {")":"(", "}":"{", "]":"["}
        stack = []

        for b in s:
            #closing case
            if b in brackets:
                if stack and stack[-1] == brackets[b]:
                    stack.pop()
                else:
                    return False
            #opening case
            else:
                stack.append(b)
        
        return not stack
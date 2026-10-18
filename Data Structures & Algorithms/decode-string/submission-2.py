class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for i in range(len(s)):
            if s[i] == "]":
                curr = stack.pop()
                sub = ""
                while stack and curr != "[":
                    sub = curr + sub
                    curr = stack.pop()
                num = ""
                while stack:
                    curr_num = stack.pop()
                    if curr_num not in nums:
                        stack.append(curr_num)
                        break
                    num = curr_num + num
                stack.append(int(num) * sub)
            else:
                stack.append(s[i])

        return ''.join(stack)
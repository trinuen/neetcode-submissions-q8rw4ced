class Solution:
    def isAlphaNum(self, c: str) -> bool:
        return (ord('a') <= ord(c) <= ord('z') or 
            ord('A') <= ord(c) <= ord('Z') or
            ord('0') <= ord(c) <= ord('9'))
            
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while (right > left):
            while right > left and not self.isAlphaNum(s[right]):
                right -= 1
            while right > left and not self.isAlphaNum(s[left]):
                left += 1
            if (s[right].lower() != s[left].lower()):
                return False
            right -= 1
            left += 1
        return True


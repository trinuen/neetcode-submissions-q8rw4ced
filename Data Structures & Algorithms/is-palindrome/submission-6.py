class Solution:

    def isAlphaNum(self, c: str) -> bool:
        return (ord('a') <= ord(c) <= ord('z') or 
        ord('A') <= ord(c) <= ord('Z') or 
        ord('0') <= ord(c) <= ord('9'))
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while not self.isAlphaNum(s[l]) and l < r:
                l += 1
            while not self.isAlphaNum(s[r]) and l < r:
                r -= 1
            if s[l].lower() != s[r].lower():
                print(s[l])
                print(s[r])
                return False
            l += 1
            r -= 1
        return True
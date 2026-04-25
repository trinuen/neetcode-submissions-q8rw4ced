class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                new_s = s[:l] + s[l+1:]
                new_s2 = s[:r] + s[r+1:]
                if new_s == new_s[::-1] or new_s2 == new_s2[::-1]:
                    return True
            l += 1
            r -= 1

        return False
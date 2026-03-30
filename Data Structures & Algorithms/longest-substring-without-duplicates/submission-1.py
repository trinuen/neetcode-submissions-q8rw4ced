class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_len = 0
        chars = set()

        #zxyzxyz
        while r < len(s):
            if s[r] not in chars:
                chars.add(s[r])
                max_len = max(max_len, len(chars))
                r += 1
            elif s[r] in chars:
                while s[l] != s[r]:
                    chars.remove(s[l])
                    l += 1
                l += 1
                r += 1

        return max_len
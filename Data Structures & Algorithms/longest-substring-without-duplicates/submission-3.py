class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        chars = set()
        for r in range(len(s)):
            if s[r] not in chars:
                chars.add(s[r])
                max_len = max(max_len, len(chars))
            else:
                while s[l] != s[r]:
                    chars.remove(s[l])
                    l += 1
                l += 1
        return max_len
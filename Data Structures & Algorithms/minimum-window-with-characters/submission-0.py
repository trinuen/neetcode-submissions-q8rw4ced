class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count, window = {}, {}

        #count freq in t
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1
    
        l = 0
        have, need = 0, len(t_count)
        res, resLen = [-1, -1], float("inf")
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if c in t_count and window[c] == t_count[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                c = s[l]
                window[c] = window.get(c, 0) - 1
                if c in t_count and window[c] < t_count[c]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""
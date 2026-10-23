class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = {}
        for c in s:
            count[c] = count.get(c,0) + 1
        res = []
        seen = set()
        size = 0
        for i in range(len(s)):
            size += 1
            if s[i] not in seen:
                seen.add(s[i])
            count[s[i]] -= 1
            if count[s[i]] == 0:
                seen.remove(s[i])
            if len(seen) == 0:
                res.append(size)
                size = 0
        return res

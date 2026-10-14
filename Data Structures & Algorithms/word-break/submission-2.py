class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        cache = {}
        def dfs(i):
            if i == len(s):
                return True
            if i in cache:
                return cache[i]

            for word in wordDict:
                if (len(word) + i) <= len(s) and s[i:i+len(word)] == word:
                    res = dfs(i+len(word))
                    if res:
                        cache[i] = True
                        return True
            cache[i] = False
            return False
        return dfs(0)
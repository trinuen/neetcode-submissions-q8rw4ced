class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(remaining):
            if remaining == 0:
                return 0
            if remaining in cache:
                return cache[remaining]
            res = float('inf')
            for c in coins:
                if remaining - c >= 0:
                    res = min(res, 1 + dfs(remaining - c))
            cache[remaining] = res
            return res

        res = dfs(amount)
        return -1 if res == float('inf') else res
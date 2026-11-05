class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = {}
        def dfs(i, remain):
            if remain == 0:
                return 1
            if i >= len(coins) or remain < 0 or coins[i] > remain:
                return 0

            if (i, remain) in dp:
                return dp[(i, remain)]

            dp[(i, remain)] = dfs(i, remain - coins[i]) + dfs(i+1, remain)
            return dp[(i, remain)]
        return dfs(0, amount)

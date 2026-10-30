class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        #[5,10]
        #[0, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]
        for i in range(len(dp)):
            for c in coins:
                remaining = i - c
                if remaining >= 0:
                    dp[i] = min(dp[i], dp[remaining]+1)
        
        return dp[amount] if dp[amount] != amount+1 else -1
        

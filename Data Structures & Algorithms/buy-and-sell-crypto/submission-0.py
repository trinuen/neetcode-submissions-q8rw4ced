class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, r = 0, 1
        highest = 0
        
        while r < len(prices):
            sell = prices[r] - prices[l]
            if sell > 0:
                highest = max(highest, sell)
                r += 1
            else:
                l = r
                r += 1

        return highest
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1: return 0

        max_profit = 0
        l,r = 0, 1
        while r < n and l < n:
            if l == r: r += 1
            else: 
                buy, sell = prices[l], prices[r]
                if buy < sell:
                    max_profit = max(sell - buy, max_profit)
                    r += 1
                else:
                    l += 1

        return max_profit


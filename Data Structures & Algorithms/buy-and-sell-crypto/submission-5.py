class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        l,r = 0, 1
        while r < n:
            buy, sell = prices[l], prices[r]
            if buy < sell:
                max_profit = max(sell - buy, max_profit)
            else:
                l = r
            r += 1

        return max_profit


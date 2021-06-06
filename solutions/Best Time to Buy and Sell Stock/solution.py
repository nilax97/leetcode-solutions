class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_val = prices.copy()
        n = len(prices)
        if n == 0:
            return 0
        previous = prices[-1]
        for i in range(n):
            max_val[n-i-1] = max(prices[n-i-1],previous)
            previous = max_val[n-i-1]
        profit = 0
        for i in range(n):
            temp = max_val[i] - prices[i]
            if temp > profit:
                profit = temp
        return profit

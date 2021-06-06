class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit = 0
        curMin = prices[0]
        
        for price in prices:
            if price < curMin:
                curMin = price
            elif price > curMin + fee:
                profit += price - curMin - fee
                curMin = price - fee
        
        return profit

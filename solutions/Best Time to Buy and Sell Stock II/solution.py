class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        profit = 0
        flag = 0
        while i<(len(prices)-1):
            if prices[i] < prices[i+1] and flag==0:
                profit -= prices[i]
                flag = 1
            elif prices[i] > prices[i+1] and flag==1:
                profit+=prices[i]
                flag = 0
            i+=1
        if(flag==1):
            profit += prices[i]
        return max(profit,0)
                

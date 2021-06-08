class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        price = [0] * (n + 1)
        price[n-1] = cost[n-1]
        price[n-2] = cost[n-2]
        for i in range(n-3,-1,-1):
            price[i] = cost[i] + min(price[i+1],price[i+2])
        return min(price[0],price[1])
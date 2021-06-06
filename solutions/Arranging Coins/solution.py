class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 0;
        for i in range(1,n+1):
            value = i*(i+1)/2
            if value > n:
                return i-1
            elif value == n:
                return i
        return 0

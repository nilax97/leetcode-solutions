class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 1:
            return 0
        ans = [0] * (n+1)
        ans[0] = 0
        ans[1] = 1
        val = 1
        for i in range(2,n+1):
            if i % 2 == 0:
                ans[i] = ans[i//2]
            else:
                ans[i] = ans[i//2] + ans[i//2 + 1]
            val = max(val,ans[i])
        return val

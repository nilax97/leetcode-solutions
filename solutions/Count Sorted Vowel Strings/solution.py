class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[i for i in range(5,0,-1)] for _ in range(n)]
        for i in range(1,n):
            for j in range(3,-1,-1):
                dp[i][j] = dp[i - 1][j] + dp[i][j + 1]
        return dp[n-1][0]

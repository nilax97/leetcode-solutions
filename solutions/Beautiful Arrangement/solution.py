ans = {}
class Solution:
    def countArrangement(self, n: int) -> int:
        def dp(i,X):
            if i==1:
                return 1
            key = (i,X)
            if key in ans:
                return ans[key]
            total = 0
            for j in range(len(X)):
                if X[j] % i == 0 or i % X[j] == 0:
                    total += dp(i-1,X[:j] + X[j+1:])
            
            ans[key] = total
            return total
        return dp(n,tuple(range(1,n+1)))

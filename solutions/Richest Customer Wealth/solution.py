class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = -1
        for i in range(len(accounts)):
            total = 0
            for j in range(len(accounts[i])):
                total += accounts[i][j]
                ans = max(total,ans)
        return ans

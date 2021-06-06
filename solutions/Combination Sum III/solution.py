class Solution:
    def combinationSum3(self, k, n):
        self.sol = []
        self.BackTr(k, n, [])
        return self.sol
        
    def BackTr(self, k, n, curr_sol):
        if n < 0 or k < 0: return
        if n == 0 and k == 0:
            self.sol.append(curr_sol)
            
        start = curr_sol[-1] + 1 if curr_sol else 1
            
        for i in range(start, 10):
            self.BackTr(k - 1, n - i, curr_sol + [i])

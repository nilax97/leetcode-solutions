class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2 == 1:
            target = 2 * (n//2) + 1
        else:
            target = ((n-1)//2) + (n//2) + 1
        ans = 0
        for i in range(n):
            ans += abs(target - (2*i + 1))
        return ans//2

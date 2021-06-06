class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans, MOD = 0, 10 ** 9 + 7
        for x in range(1, n + 1):
            ans = (ans * (1 << (len(bin(x)) - 2)) + x) % MOD
        return ans

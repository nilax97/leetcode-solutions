class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        ans = [1] * (n)
        ans[0] = 0
        ans[1] = 0
        index = 2
        while(index * index < n):
            factor = index
            while(index * factor < n):
                ans[index*factor] = 0
                factor += 1
            index += 1
            while(ans[index] == 0):
                index += 1
        val = 0
        for x in ans:
            val += x
        return val

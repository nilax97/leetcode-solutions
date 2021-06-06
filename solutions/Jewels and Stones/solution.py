class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        val = dict()
        for x in jewels:
            val[x] = 0
        ans = 0
        for x in stones:
            if x in val:
                ans += 1
        return ans

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        val = dict()
        for x in nums:
            if x in val:
                val[x] += 1
            else:
                val[x] = 1
        ans = 0
        for x in nums:
            if val[x] < 1:
                continue
            if (k-x) in val:
                if val[k-x] > 0:
                    ans += 1
                    val[x] -= 1
                    val[k-x] -= 1
                    if val[x] < 0:
                        ans -= 1
                        val[x] = 0
        return ans

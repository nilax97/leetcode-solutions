class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        val = dict()
        ans = 0
        for x in nums:
            ans += x
            if x in val:
                val[x] += 1
                ans -= x * val[x]
                val[x] = 0
            else:
                val[x] = 1
        return ans

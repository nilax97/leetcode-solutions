class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        ans = {}
        for x in sorted(arr):
            ans[x] = 1 + sum(ans[y] * ans.get(x/y, 0) for y in arr if y < x)
        return sum(ans.values()) % (10**9 + 7)


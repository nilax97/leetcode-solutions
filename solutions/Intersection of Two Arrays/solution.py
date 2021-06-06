class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = set()
        val1 = dict()
        for x in nums1:
            val1[x] = 1
        for x in nums2:
            if x in val1:
                ans.add(x)
        return list(ans)

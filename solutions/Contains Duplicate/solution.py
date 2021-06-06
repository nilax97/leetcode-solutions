class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check = dict()
        for x in nums:
            if x in check.keys():
                return True
            check[x] = 1
        return False

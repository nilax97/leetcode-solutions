class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total = (n * (n+1)) // 2
        missing = total-sum(set(nums))
        duplicate = missing - (total-sum(nums))
        return [duplicate,missing]

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 102
        for x in nums:
            count[x+1] += 1
        for i in range(1,101):
            count[i] += count[i-1]
        return [count[x] for x in nums]

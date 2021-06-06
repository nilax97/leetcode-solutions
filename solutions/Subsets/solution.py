class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[],nums]
        val = self.subsets(nums[1:])
        val2 = val + self.subsets(nums[1:])
        for i in range(len(val)):
            val2[i].append(nums[0])
        return val2

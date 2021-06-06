class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val = dict()
        for i in range(len(nums)):
            if (target-nums[i]) in val.keys():
                return [val[target-nums[i]],i]
            val[nums[i]] = i

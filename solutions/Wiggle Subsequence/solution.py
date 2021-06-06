class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        prevdiff = nums[1] - nums[0]
        if prevdiff != 0:
            count = 2
        else:
            count = 1
        for i in range(2,len(nums)):
            diff = nums[i] - nums[i-1]
            if (diff > 0 and prevdiff <=0) or (diff < 0 and prevdiff >=0):
                count += 1
                prevdiff = diff
        return count

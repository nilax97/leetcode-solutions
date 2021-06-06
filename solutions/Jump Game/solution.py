class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        target = n-1
        for i in range(n-1,-1,-1):
            if nums[i] >= (target-i):
                target = i
        if target == 0:
            return True
        else:
            return False

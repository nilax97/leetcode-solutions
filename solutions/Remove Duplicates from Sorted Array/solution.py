class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        extra = 0
        current = 1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[current] = nums[i]
                current += 1
            else:
                extra+=1
        return len(nums)-extra

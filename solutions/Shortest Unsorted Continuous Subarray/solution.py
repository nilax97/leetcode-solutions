class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        num2 = sorted(nums)
        start = 0
        end = (len(nums) - 1)
        while(start <= end):
            if nums[start] == num2[start]:
                start += 1
            elif nums[end] == num2[end]:
                end -= 1
            else:
                break
        return (end - start + 1)

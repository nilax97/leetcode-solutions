class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        start = 0
        end = -1
        val = min(1,len(nums))
        while(start < (len(nums)-1)):
            if nums[start+1] > nums[start]:
                start+=1
                val = max(val,start-end)
            else:
                end = start
                start+= 1
            val = max(val,start-end)
        return val
                

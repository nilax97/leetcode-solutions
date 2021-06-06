class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        for i in range(len(nums)):
            if(nums[i]==0):
                continue
            else:
                if(i!=index):
                    temp = nums[i]
                    nums[i] = nums[index]
                    nums[index] = temp
                i+=1
                index+=1
                
                

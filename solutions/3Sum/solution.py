class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        ans = dict()
        for i in range(n):
            j = i+1
            k = n-1
            while(j<k):
                temp = nums[i] + nums[j] + nums[k]
                if(temp==0):
                    ans[(nums[i],nums[j],nums[k])] = 1
                    j+=1
                    k-=1
                elif(temp>0):
                    k-=1
                else:
                    j+=1        
        return ans.keys()
            

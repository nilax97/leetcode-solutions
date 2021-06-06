class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ans = list()
        n = len(nums)
        if(n==0):
            bot = lower
            top = upper
            if(bot==top):
                ans.append(str(bot))
            else:
                ans.append(str(bot) + "->" + str(top))
            return ans
            
        if(nums[0]>(lower)):
            bot = lower
            top = nums[0] - 1
            if(bot==top):
                ans.append(str(bot))
            else:
                ans.append(str(bot) + "->" + str(top))
        for i in range(1,n):
            bot = nums[i-1]+1
            top = nums[i]-1
            if(bot>top):
                continue
            elif(bot==top):
                ans.append(str(bot))
            else:
                ans.append(str(bot) + "->" + str(top))
        if(nums[-1] < upper):
            bot = nums[-1]+1
            top = upper
            if(bot==top):
                ans.append(str(bot))
            else:
                ans.append(str(bot) + "->" + str(top))
        return ans

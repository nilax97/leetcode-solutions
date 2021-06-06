class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n==0:
            return 0
        if n==1:
            if nums[0]!=k:
                return 0
            else:
                return 1
        values = dict()
        values[0] = [-1]
        temp = 0
        ans = 0
        for i in range(n):
            temp = temp + nums[i]
            if (temp-k) in values:
                ans += len(values[temp-k])
            if temp in values:
                values[temp].append(i)
            else:
                values[temp] = [i]
        # print(values)
        return ans

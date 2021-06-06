class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        first = 10**5
        second = 10**5
        count1 = 0
        count2 = 0
        n = len(nums)
        for i in range(n):
            # print(nums[i],first,second,count1,count2)
            if nums[i] == first:
                count1 += 1
            elif nums[i] == second:
                count2 += 1
            elif count1 == 0:
                count1 += 1
                first = nums[i]
            elif count2 == 0:
                count2 += 1
                second = nums[i]
            else:
                count1 -= 1
                count2 -= 1
        count1 = 0
        count2 = 0
        for i in range(n):
            if nums[i] == first:
                count1 += 1
            elif nums[i] == second:
                count2 += 1
        ans = []
        if count1 > n//3:
            ans.append(first)
        if count2 > n//3:
            ans.append(second)
        return ans

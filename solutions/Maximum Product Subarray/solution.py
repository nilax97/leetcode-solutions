class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_pos = float('-inf')
        cur_pos = 0
        cur_neg = 0
        flag = 1
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)):
            x = nums[i]
            prev_pos = cur_pos
            prev_neg = cur_neg
            if x>0:
                cur_pos = max(prev_pos * x,x)
                cur_neg = prev_neg * x
            elif x<0:
                cur_pos = prev_neg * x
                cur_neg = min(prev_pos * x, x)
            else:
                cur_pos = 0
                cur_neg = 0
                flag = 0
            max_pos = max(max_pos, cur_pos)
            if flag != 0 and max_pos == 0:
                max_pos = cur_neg
            print(max_pos, cur_pos, cur_neg)
        return max_pos

class Solution:
    def rob(self, nums: List[int]) -> int:
        max_vals = [0]
        for x in nums:
            if len(max_vals) == 1:
                max_vals.append(x)
            elif len(max_vals) == 2:
                max_vals.append(max(x,max_vals[-1]))
            else:
                max_vals.append(max(max_vals[-1], max_vals[-2]+x))
        return max_vals[-1]

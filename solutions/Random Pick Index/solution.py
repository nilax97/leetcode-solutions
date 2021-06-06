import random

class Solution:

    def __init__(self, nums: List[int]):
        self.vals = dict()
        for i in range(len(nums)):
            if nums[i] in self.vals:
                self.vals[nums[i]].append(i)
            else:
                self.vals[nums[i]] = [i]

    def pick(self, target: int) -> int:
        n = len(self.vals[target])
        x = random.randint(0,n-1)
        return self.vals[target][x]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

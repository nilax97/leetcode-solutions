class Solution:
    def numberOfSteps (self, num: int) -> int:
        if num == 0:
            return 0
        if num %2 == 0:
            return 1 + self.numberOfSteps(num//2)
        else:
            return 1 + self.numberOfSteps(num - 1)

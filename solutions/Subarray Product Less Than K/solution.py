class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        self.ans = 0
        self.start = 0
        self.prev = 1
        for i in range(len(nums)):
            self.prev *= nums[i]
            while(self.prev >= k and self.start<=i):
                self.prev //= nums[self.start]
                self.start += 1
            self.ans += (i - self.start + 1)
        return self.ans
                

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)
        self.n = len(nums)
        self.k = k

    def add(self, val: int) -> int:
        self.n += 1
        for i in range(self.n-1):
            if self.nums[i] > val:
                self.nums.insert(i,val)
                break
        if len(self.nums) != self.n:
            self.nums.append(val)
        return self.nums[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

import random
class Solution:

    def __init__(self, nums: List[int]):
        self.reset = lambda: nums
        self.shuffle = lambda: random.sample(nums, len(nums))

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

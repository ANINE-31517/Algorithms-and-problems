class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums.copy()
        self.current = nums

    def reset(self) -> List[int]:
        self.current = self.nums[:]
        return self.current

    def shuffle(self) -> List[int]:
        from random import shuffle
        shuffle(self.current)
        return self.current


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
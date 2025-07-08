class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        min_of_nums, max_of_nums = min(nums), max(nums)
        for i in range(1, len(nums)-1):
            if nums[i] > min_of_nums and nums[i] < max_of_nums:
                count += 1
        return count
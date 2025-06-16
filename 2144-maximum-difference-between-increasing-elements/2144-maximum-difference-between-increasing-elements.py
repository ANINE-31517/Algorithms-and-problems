class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        cur_min = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > cur_min:
                ans = max(ans, nums[i] - cur_min)
            cur_min = min(cur_min, nums[i])
        return ans
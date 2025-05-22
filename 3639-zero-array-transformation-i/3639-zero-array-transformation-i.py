class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diff = [0 for _ in range(len(nums) + 1)]
        for i,j in queries:
            diff[i] -= 1
            diff[j+1] += 1
        summ = 0
        for i in range(len(nums)):
            summ += diff[i]
            if nums[i] > -1*summ:
                return False
        return True
        
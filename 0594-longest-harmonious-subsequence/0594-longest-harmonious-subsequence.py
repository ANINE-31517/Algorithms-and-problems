class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return 0
        nums.sort()
        l,r=0,1
        res=0
        while r<len(nums):
            if nums[r]-nums[l]<=1:
                if nums[r]-nums[l]==1:
                    res=max(res,r-l+1)
                r+=1
            else:
                l+=1
        return res
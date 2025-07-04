class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans,mod=0,10**9+7
        l,r=0,len(nums)-1
        while l<=r:
          if nums[l]+nums[r]>target:
            r-=1
          else:
            ans+=pow(2,r-l,mod)
            l+=1
        return ans%mod
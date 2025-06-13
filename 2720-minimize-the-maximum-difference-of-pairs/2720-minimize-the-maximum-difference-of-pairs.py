class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        '''nums.sort()
        diff=[]
        for i in range(1,len(nums)):
            diff.append(nums[i]-nums[i-1])
        diff.sort()
        return max(diff[:p]) if p else 0'''
        nums.sort()
        n=len(nums)
        l,r=0,nums[n-1]-nums[0]

        def check(n,nums,mid,p):
            count,i=0,1
            while(i<n):
                if nums[i]-nums[i-1]<=mid:
                    count+=1
                    i+=1
                if count>=p:
                    return True
                i+=1
            return False
            
        while(l<r):
            mid=l+(r-l)//2
            if check(n,nums,mid,p):
                r=mid
            else:
                l=mid+1
        return l
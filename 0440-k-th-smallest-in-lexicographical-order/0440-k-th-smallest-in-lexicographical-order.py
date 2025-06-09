class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        num,i,cur=1,1,0
        def find(a,b,n):
            nonlocal cur
            cur=0
            while a<=n:
                cur+=min(n+1,b)-a
                a*=10
                b*=10
            return cur
        while i<k:
            req=find(num,num+1,n)
            if i+req<=k:
                num+=1
                i+=req
            else:
                i+=1
                num*=10
        return num
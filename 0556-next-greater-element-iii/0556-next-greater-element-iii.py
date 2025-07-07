class Solution1:
    def nextGreaterElement(self, n: int) -> int:
        hm = defaultdict(int)
        for i in str(n):
            hm[i]+=1
        cur = n+1
        while len(str(cur)) == len(str(n)):
            new_hm = defaultdict(int)
            flag = 1
            for j in str(cur):
                new_hm[j]+=1
            for key, val in new_hm.items():
                if key not in hm:
                    flag = 0
                    break
                if val != hm[key]:
                    flag = 0
                    break
            if flag:
                return cur
            cur += 1
        return -1

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        i = len(digits)-2
        while i>=0 and digits[i]>=digits[i+1]:
            i-=1
        if i==-1:
            return -1
        j = len(digits)-1
        while j>i and digits[j]<=digits[i]:
            j-=1
        digits[i],digits[j] = digits[j],digits[i]
        digits[i+1:] = reversed(digits[i+1:])
        res = int(''.join(digits))
        return res if res<2**31 else -1 
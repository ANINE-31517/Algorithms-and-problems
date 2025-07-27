class Solution:
    def countHillValley(self, cur: List[int]) -> int:
        res = 0
        i = 1
        n = len(cur)
        while i<(n-1):
            if cur[i] != cur[i+1]:
                left, right = 0, 0
                for l in range(i-1, -1 ,-1):
                    if cur[l] == cur[i]:
                        continue
                    if cur[l] > cur[i]:
                        left = 1
                    break
                for r in range(i+1,n):
                    if cur[r] == cur[i]:
                        continue
                    if cur[r] > cur[i]:
                        right = 1
                    break
                if left and right:
                    res += 1
                    i += 1
                    continue
                left, right = 0, 0
                for l in range(i-1, -1 ,-1):
                    if cur[l] == cur[i]:
                        continue
                    if cur[l] < cur[i]:
                        left = 1
                    break
                for r in range(i+1,n):
                    if cur[r] == cur[i]:
                        continue
                    if cur[r] < cur[i]:
                        right = 1
                    break 
                if left and right:
                    res += 1
            i += 1
        return res
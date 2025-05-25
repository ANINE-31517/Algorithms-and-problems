class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        hm = defaultdict(list)
        for i in words:
            if i in hm:
                hm[i][0] += 1
            else:
                hm[i] = [1, 0]
        res = 0
        cen = 0
        even = 0
        for i, j in hm.items():
            rev = i[::-1]
            if i[0] == i[1]:
                if j[0] == 1:
                    if not cen:
                        res += 2
                        cen = 1
                else:
                    if j[0]%2 != 0:
                        even = 1
                    res += (j[0]//2)*4
                j[1] = 1
            elif rev in hm.keys() and hm[rev][1] == 0:
                res += min(j[0], hm[rev][0])*4
                j[1] = 1
                hm[rev][1] = 1
        if cen:
            return res
        elif not cen and even:
            return res + 2
        return res
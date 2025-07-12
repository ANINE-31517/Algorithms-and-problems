class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float('inf')
        for s in strs:
            min_length = min(min_length, len(s))
        res = ""
        for i in range(min_length):
            cur = set()
            for j in range(len(strs)):
                cur.add(strs[j][i])
            if len(cur) == 1:
                res+=strs[j-1][i]
            else:
                break
        return res
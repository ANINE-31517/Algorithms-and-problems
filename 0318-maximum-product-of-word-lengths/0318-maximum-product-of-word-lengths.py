class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                s1, s2 = set(words[i]), set(words[j])
                l1, l2 = len(s1), len(s2)
                if l1 == len(s1 - s2):
                    res = max(res, len(words[i]) * len(words[j]))
        return res
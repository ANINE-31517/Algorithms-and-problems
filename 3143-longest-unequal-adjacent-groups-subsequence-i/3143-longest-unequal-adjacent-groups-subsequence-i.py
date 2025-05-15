class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        i,j=0,1
        res=[words[0]]
        while j<len(groups):
            if groups[i]!=groups[j]:
                i=j
                res.append(words[j])
            j+=1
        return res
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        hm = defaultdict(list)
        for i in dictionary:
            j, k = 0, 0
            while j<len(i) and k<len(s):
                if i[j] == s[k]:
                    j += 1
                    k += 1
                else:
                    k += 1 
                if j == len(i):
                    hm[len(i)].append(i)
                    break
        if not hm:
            return ""
        true_list = hm[max(hm.keys())]
        true_list.sort()
        return true_list[0]
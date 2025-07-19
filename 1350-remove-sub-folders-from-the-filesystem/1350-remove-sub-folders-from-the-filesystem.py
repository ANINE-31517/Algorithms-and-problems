class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        print(folder)
        res=[folder[0]]
        prev=folder[0]
        i=1
        while i<len(folder):
            if not folder[i].startswith(prev+'/'):
                res.append(folder[i])
                prev=folder[i]
            i+=1
        return res
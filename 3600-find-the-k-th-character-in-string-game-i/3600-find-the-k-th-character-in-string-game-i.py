class Solution:
    def kthCharacter(self, k: int) -> str:
        s = "a"
        while len(s)<k:
            cur_s = ""
            for i in s:
               char = ord(i)+1
               if char > 122:
                    char = 97
               cur_s+=chr(char)
            new_s = s + cur_s
            s = new_s 
        return s[k-1]
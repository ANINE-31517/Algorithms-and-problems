class Solution:
    def countAndSay(self, n: int) -> str:
        cur = "1"
        n -= 1
        while n:
            r = 0
            temp = ""
            while r < len(cur):
                flag = cur[r]
                count = 0
                while r < len(cur) and flag == cur[r]:
                    count += 1
                    r += 1
                temp += str(count) + flag
            cur = temp
            n -= 1
        return cur
        
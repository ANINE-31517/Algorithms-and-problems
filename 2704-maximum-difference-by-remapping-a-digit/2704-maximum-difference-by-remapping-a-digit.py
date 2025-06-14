class Solution:
    def minMaxDifference(self, num: int) -> int:
        num1, num2 = "", ""
        num = str(num)
        target_min = num[0]
        target_max = 0
        for i in num:
            if i != "9":
                target_max = i
                break
        for i in num:
            f1, f2 = 0, 0 
            if i == target_max:
                num1 += "9"
                f1 = 1
            if i == target_min:
                num2 += "0"
                f2 = 1
            if not f1:
                num1 += i
            if not f2:
                num2 += i
        return int(num1) -int(num2)

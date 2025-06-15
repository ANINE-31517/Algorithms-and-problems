class Solution:
    def maxDiff(self, num: int) -> int:
        num1, num2 = "", ""
        num = str(num)
        target_min = max(num)
        target_max = 1
        count = 0
        identity = 0
        for i in num:
            if i != "1" and i != "0":
                target_min = i
                break
            else:
                count += 1
        for i in num:
            if i != "9":
                target_max = i
                break
        if max(num) == "1":
            identity = 1
        for i in num:
            f1, f2 = 0, 0 
            if i == target_max:
                num1 += "9"
                f1 = 1
            if i == target_min:
                if count:
                    num2 += "0"
                else:
                    num2 += "1"
                f2 = 1
            if not f1:
                num1 += i
            if not f2:
                num2 += i
        if identity:
            return int(num1) - int(num)
        return int(num1) - int(num2)
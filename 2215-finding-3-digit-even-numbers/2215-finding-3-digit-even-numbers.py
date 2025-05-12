class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = []
        s = set()
        n = len(digits)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and j != k and k != i and digits[i] != 0 and digits[k]%2 == 0:
                        num = digits[i]*100 + digits[j]*10 + digits[k]
                        if num not in s:
                            res.append(num)
                            s.add(num)
        return sorted(res)


        
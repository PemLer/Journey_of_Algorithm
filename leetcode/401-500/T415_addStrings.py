class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        carry = 0
        n1, n2 = len(num1), len(num2)
        c1, c2 = n1 - 1, n2 - 1
        res = []
        while c1 >= 0 and c2 >= 0:
            a, b = int(num1[c1]), int(num2[c2])
            res.append((a + b + carry) % 10)
            carry = (a + b + carry) // 10
            c1 -= 1
            c2 -= 1

        while c1 >= 0:
            a = int(num1[c1])
            res.append((a + carry) % 10)
            carry = (a + carry) // 10
            c1 -= 1

        while c2 >= 0:
            b = int(num2[c2])
            res.append((b + carry) % 10)
            carry = (b + carry) // 10
            c2 -= 1

        if carry:
            res.append(carry)

        return ''.join(map(str, res[::-1]))

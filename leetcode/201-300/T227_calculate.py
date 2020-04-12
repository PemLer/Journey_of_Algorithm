class Solution:
    def calculate(self, s: str) -> int:
        nums = []
        ops = []

        def cal():
            a = nums.pop()
            b = nums.pop()
            c = ops.pop()
            if c == '+':
                nums.append(b + a)
            elif c == '-':
                nums.append(b - a)
            elif c == '*':
                nums.append(b * a)
            else:
                nums.append(int(b / a))

        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            elif s[i].isdigit():
                t = ''
                while i < len(s) and s[i].isdigit():
                    t += s[i]
                    i += 1
                nums.append(int(t))
            elif not ops:
                ops.append(s[i])
                i += 1
            elif s[i] == '+' or s[i] == '-':
                while ops:
                    cal()
                ops.append(s[i])
                i += 1
            else:
                while ops and (ops[-1] == '*' or ops[-1] == '/'):
                    cal()
                ops.append(s[i])
                i += 1
        while ops:
            cal()

        return nums[-1]
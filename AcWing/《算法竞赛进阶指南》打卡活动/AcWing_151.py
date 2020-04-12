s = input()
nums = []
ops = []
s = '(' * len(s) + s + ')'


def qmi(a, k):
    res = 1
    while k:
        if k & 1:
            res *= a
        a *= a
        k >>= 1
    return res


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
    elif c == '/':
        nums.append(b / a)
    else:
        nums.append(qmi(b, a))


def solve():
    i = 0
    while i < len(s):
        if s[i].isdigit():
            t = ''
            while i < len(s) and s[i].isdigit():
                t += s[i]
                i += 1
            nums.append(int(t))
        else:
            if s[i] == '(':
                ops.append(s[i])
                i += 1
            elif s[i] == '+' or s[i] == '-':
                # 确定‘-’是否为负号
                if s[i] == '-' and i and not s[i-1].isdigit() and s[i-1] != ')':
                    t = '-'
                    i += 1
                    while s[i].isdigit():
                        t += s[i]
                        i += 1
                    nums.append(int(t))
                else:
                    # 因为加减法优先级最低，所以直接先进行计算
                    while ops[-1] != '(':
                        cal()
                    ops.append(s[i])
                    i += 1

            elif s[i] == '*' or s[i] == '/':
                while ops[-1] == '*' or ops[-1] == '/' or ops[-1] == '^':
                    cal()
                ops.append(s[i])
                i += 1
            elif s[i] == '^':
                while ops[-1] == '^':
                    cal()
                ops.append(s[i])
                i += 1
            elif s[i] == ')':
                while ops[-1] != '(':
                    cal()
                ops.pop()
                i += 1


solve()
print(int(nums[-1]))

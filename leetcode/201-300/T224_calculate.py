# 方法一中缀转后缀
class Solution:
    def calculate(self, s: str) -> int:
        items = self.in_to_post_exp(s)
        stack = []
        for item in items:
            if item.isdigit():
                stack.append(int(item))
            elif item == '+':
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v2 + v1)
            else:
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v2 - v1)
        return stack[0]

    def in_to_post_exp(self, s):
        """中缀表达式转化为后缀表达式"""
        items = list(s.replace(' ', ''))
        stack = []
        exp_post = []
        i = 0
        while i < len(items):
            if items[i].isdigit():
                tmp = ''
                while i < len(items) and items[i].isdigit():
                    tmp += items[i]
                    i += 1
                exp_post.append(tmp)
                continue

            if not stack or items[i] == '(':
                stack.append(items[i])
            elif items[i] == ')':
                while stack and stack[-1] != '(':
                    exp_post.append(stack.pop())
                stack.pop()  # 将‘(’弹出
            else:
                # 由于只有+和-，没有优先级关系，因此默认将栈顶运算符加入exp
                while stack and (stack[-1] == '+' or stack[-1] == '-'):
                    exp_post.append(stack.pop())
                stack.append(items[i])
            i += 1
        while stack:
            exp_post.append(stack.pop())
        return exp_post


# 方法二 直接计算
class Solution2:
    def calculate(self, s: str) -> int:
        nums = []
        ops = []

        def cal():
            a = nums.pop()
            b = nums.pop()
            c = ops.pop()
            if c == '+':
                nums.append(b + a)
            else:
                nums.append(b - a)

        s = '(' + s + ')'  # 前后加括号便于最后计算出所有值
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            elif s[i].isdigit():
                tmp = ''
                while i < len(s) and s[i].isdigit():
                    tmp += s[i]
                    i += 1
                nums.append(int(tmp))
            elif s[i] == '(':
                ops.append(s[i])
                i += 1
            elif s[i] == ')':  # 右括号时计算上一个左括号到现在右括号的值并将结果压入数据栈
                while ops[-1] != '(':
                    cal()
                ops.pop()
                i += 1
            else:
                while ops and ops[-1] != '(':  # 由于只有加减法，没有所有前面入栈的操作符优先级高于当前，计算完之前的再加入现在的
                    cal()
                ops.append(s[i])
                i += 1
        return nums[-1]

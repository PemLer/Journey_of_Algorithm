class Solution:
    def addOperators(self, num: str, target: int):
        if not num:
            return []
        self.res = []
        self.backtrack(num, target, '', 0, 0)
        return self.res

    def backtrack(self, num, target, sub, val, pre):
        if not num:
            if val == target:
                self.res.append(sub)
            return
        for i in range(len(num)):
            cur_str = num[:i + 1]
            if len(cur_str) > 1 and cur_str.startswith('0'):
                continue
            cur = int(cur_str)
            if not sub:
                self.backtrack(num[i + 1:], target, sub + cur_str, val + cur, cur)
            else:
                self.backtrack(num[i + 1:], target, sub + '+' + cur_str, val + cur, cur)
                self.backtrack(num[i + 1:], target, sub + '-' + cur_str, val - cur, -cur)
                self.backtrack(num[i + 1:], target, sub + '*' + cur_str, val - pre + pre * cur, pre * cur)



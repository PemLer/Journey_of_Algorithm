class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        self.dic = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        self.res = []
        self.dfs(list(digits), '')
        return self.res

    def dfs(self, digits, sub):
        if not digits:
            self.res.append(sub)
            return
        # num = digits.pop(0)
        for s in self.dic[digits[0]]:
            self.dfs(digits[1:], sub + s)

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.res = []
        left = 0
        right = 0
        
        # count "(" and ")"
        for i in s:
            if i == ')':
                if left != 0:
                    left -= 1
                else:
                    right += 1
            elif i == '(':
                left += 1
        
        # check s is valid or not
        def is_valid(s):
            count = 0
            for i in s:
                if i == '(':
                    count += 1
                elif i == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0
        
        # backtrack
        def dfs(s, pos, left, right):
            if left == 0 and right == 0 and is_valid(s):
                self.res.append(s)
                return
            for i in range(pos, len(s)):
                if i != pos and s[i] == s[i-1]:
                    continue
                if s[i] == ')' and right > 0:
                    dfs(s[:i]+s[i+1:], i, left, right-1)
                if s[i] == '(' and left > 0:
                    dfs(s[:i]+s[i+1:], i, left-1, right)
        dfs(s, 0, left, right)
        return self.res
        

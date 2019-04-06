class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = []
        choice = [x for x in range(n)]
        self.backtrack(n, choice, [])
        return len(self.res)
    
    def backtrack(self, n, choice, sub):
            if len(sub) == n:
                tmp = []
                for k in range(n):
                    tmp.append('.'*sub[k]+'Q'+'.'*(n-sub[k]-1)) 
                self.res.append(tmp)
                return
            for i in range(len(choice)):
                if self.is_legal(sub, choice[i]):
                    self.backtrack(n, choice[:i]+choice[i+1:], sub+[choice[i]])
                
    def is_legal(self, sub, i):
        cur = (i, len(sub))
        if i not in sub:
            for index in range(len(sub)):
                tmp = (sub[index], index)
                if abs(tmp[0]-cur[0]) == abs(tmp[1]-cur[1]):
                    return False
        else:
            return False
        return True
        

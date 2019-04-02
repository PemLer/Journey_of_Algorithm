class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        sub = ''
        self.res = []
        self.dfs(s,0,sub)
        return self.res
    
    def dfs(self,s,k,sub):
        if k == 4:
            self.res.append(sub)
        elif k == 3:
            if s and int(s) <= 255:
                if s[0] == '0' and len(s) > 1:
                    pass
                else:
                    self.dfs('',k+1,sub+s)
        else:
            if s:
                if s[0] != '0':
                    self.dfs(s[1:],k+1,sub+s[0]+'.')
                    self.dfs(s[2:],k+1,sub+s[:2]+'.')
                    if int(s[:3]) <= 255:
                        self.dfs(s[3:],k+1,sub+s[:3]+'.')
                else:
                    self.dfs(s[1:],k+1,sub+s[0]+'.')

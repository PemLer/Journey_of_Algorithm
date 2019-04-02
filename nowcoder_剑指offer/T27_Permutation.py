# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        if not ss:
            return []
        self.res = []
        ss_list = list(ss)
        self.dfs(ss_list, [])
        return sorted(list(set([''.join(x) for x in self.res])))

    def dfs(self, ss_list, sub):
        if not ss_list:
            self.res.append(sub)
            return
        for i in range(len(ss_list)):
            self.dfs(ss_list[:i]+ss_list[i+1:], sub+[ss_list[i]])

if __name__=='__main__':
    sol = Solution()
    ss = 'aab'
    print(sol.Permutation(ss))
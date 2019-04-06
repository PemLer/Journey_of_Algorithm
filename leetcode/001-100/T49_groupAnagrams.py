class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = []
        for i in strs:
            s = list(i)
            s.sort()
            ans.append(''.join(s))

        t = 0
        dic = {}
        res = []
        for i in range(0,len(ans)):
            if ans[i] not in dic:
                dic[ans[i]] = t
                # print(t)
                res.append([strs[i]])
                t += 1
            else:
                res[dic[ans[i]]].append(strs[i])

        return res

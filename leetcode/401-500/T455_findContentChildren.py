class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g:
            return 0
        g.sort()
        s.sort()
        cur = 0
        res = 0
        for num in s:
            if num >= g[cur]:
                cur += 1
                res += 1
            else:
                pass
            if cur == len(g):
                break
        return res

import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tar = collections.defaultdict(int)
        cur = collections.defaultdict(int)

        def check():
            flag = True
            for key, val in tar.items():
                if cur[key] < val:
                    flag = False
                    break
            return flag

        for char in t:
            tar[char] += 1

        l, r = 0, 0
        ans = float('inf')
        llen, rlen = -1, -1
        while r < len(s):
            char = s[r]
            if char in tar:
                cur[char] += 1

            while check() and l <= r:
                if r - l + 1 < ans:
                    ans = r - l + 1
                    llen, rlen = l, r + 1
                if s[l] in tar:
                    cur[s[l]] -= 1
                l += 1
            r += 1
        return s[llen:rlen] if llen != -1 else ''

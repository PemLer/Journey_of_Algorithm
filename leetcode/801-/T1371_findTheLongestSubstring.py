class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        """
        1 >> 1 = 10 = 2
        1 >> 2 = 100 = 4
        ...
        1 >> 5 = 100000 = 32
        11111 = 31
        """
        n = len(s)
        pos = [-1] * (1 << 5)
        pos[0] = 0  # 表示从起始位置开始
        res, state = 0, 0
        for i in range(n):
            if s[i] == 'a':
                state ^= (1 << 0)
            elif s[i] == 'e':
                state ^= (1 << 1)
            elif s[i] == 'i':
                state ^= (1 << 2)
            elif s[i] == 'o':
                state ^= (1 << 3)
            elif s[i] == 'u':
                state ^= (1 << 4)

            if pos[state] != -1:
                res = max(res, i + 1 - pos[state])
            else:
                pos[state] = i + 1
        return res


if __name__ == '__main__':
    sol = Solution()
    ss = ["eleetminicoworoep", "leetcodeisgreat", "bcbcbc"]
    for s in ss:
        print(sol.findTheLongestSubstring(s))

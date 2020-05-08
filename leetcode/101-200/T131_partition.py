from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def is_valid(string):
            l, r = 0, len(string) - 1
            flag = True
            while l < r:
                if string[l] == string[r]:
                    l += 1
                    r -= 1
                else:
                    flag = False
                    break
            return flag

        n = len(s)
        res = []

        def dfs(index, tmp):
            if index == n:
                res.append(tmp[:])
                return

            for i in range(index + 1, n + 1):
                if is_valid(s[index:i]):
                    tmp.append(s[index:i])
                    dfs(i, tmp)
                    tmp.pop()

        dfs(0, [])
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.partition('aaba'))

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:

        def cal(i, j):
            ans = 0
            while i:
                ans += i % 10
                i //= 10
            while j:
                ans += j % 10
                j //= 10
            return ans

        count = 0
        memo = [[False] * n for _ in range(m)]
        if k == 0:
            return 1
        else:
            stack = [(0, 0)]
            memo[0][0] = True
        count += 1

        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        while stack:
            i, j = stack.pop(0)
            for t in range(4):
                a, b = i + dx[t], j + dy[t]
                if 0 <= a < m and 0 <= b < n and not memo[a][b] and cal(a, b) <= k:
                    memo[a][b] = True
                    count += 1
                    stack.append((a, b))
        return count
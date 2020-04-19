from typing import List


class Pair:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __repr__(self):
        return "Pair({}, {})".format(self.first, self.second)


# 方法一 动态规划
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        """
        dp[i][j].first = max(piles[i] + dp[i+1][j].second, piles[j] + dp[i][j-1].second)
        i～j 的石头堆，先手获取的最大石头数
        """
        n = len(piles)
        dp = [[Pair(0, 0) for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i].first = piles[i]

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = l + i - 1
                left = piles[i] + dp[i + 1][j].second
                right = piles[j] + dp[i][j - 1].second
                if left > right:
                    dp[i][j].first = left
                    dp[i][j].second = dp[i + 1][j].first
                else:
                    dp[i][j].first = right
                    dp[i][j].second = dp[i][j - 1].first
        return dp[0][n - 1].first - dp[0][n - 1].second > 0


# 方法二 数学
class Solution2:
    def stoneGame(self, piles: List[int]) -> bool:
        return True


if __name__ == '__main__':
    sol = Solution()
    piles = [3, 7, 2, 3]
    print(sol.stoneGame(piles))

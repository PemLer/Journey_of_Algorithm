from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        if k > n / 2:
            return self.maxProfit_with_no_k_limit(prices)

        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]
        for i in range(n):
            for j in range(1, k + 1):
                if i == 0:  # 初始状态
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[0]
                else:  # 状态转移
                    dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                    dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

        return dp[n - 1][k][0]

    def maxProfit_with_no_k_limit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(len(prices) - 1):
            diff = prices[i + 1] - prices[i]
            if diff > 0:
                ans += diff
        return ans
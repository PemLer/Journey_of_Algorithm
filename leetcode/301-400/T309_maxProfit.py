from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n+2)]

        for i in range(2, n+2):
            if i == 2:
                dp[i][1] = - prices[i-2]
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i-2])
                dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i-2])

        return dp[n+1][0]
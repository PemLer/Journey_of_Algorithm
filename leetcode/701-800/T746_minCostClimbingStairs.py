from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, n):
            dp[i] += cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[-1], dp[-2])


if __name__ == '__main__':
    sol = Solution()
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(sol.minCostClimbingStairs(cost))

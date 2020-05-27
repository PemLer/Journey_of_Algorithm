class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        """
        dp[i][j] = dp[i0][j-1] + cal(i0, j)
        """
        n = len(A)
        pre_sum = [0] * n
        pre_sum[0] = A[0]
        for i in range(1, n):
            pre_sum[i] = pre_sum[i - 1] + A[i]

        def cal(i, j):
            return (pre_sum[j] - pre_sum[i] + A[i]) / (j - i + 1)

        dp = [[0] * (K + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(min(i, K) + 1):
                if j == 1:
                    dp[i][j] = cal(0, i - 1)
                else:
                    for k in range(1, i):
                        dp[i][j] = max(dp[i][j], dp[k][j - 1] + cal(k, i - 1))
        return dp[-1][-1]
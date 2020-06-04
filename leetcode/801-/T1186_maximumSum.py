class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        """
        1 还没行使删除权利 0 已经行使删除权利
        dp[i][1] = max(dp[i-1][1] + arr[i], arr[i])
        dp[i][0] = max(dp[i-1][0] + arr[i], dp[i-1][1])
        """
        n = len(arr)
        dp = [[float('-inf')] * 2 for _ in range(n)]
        dp[0][1] = arr[0]
        ans = arr[0]
        for i in range(1, n):
            dp[i][1] = max(dp[i-1][1] + arr[i], arr[i])
            dp[i][0] = max(dp[i-1][0] + arr[i], dp[i-1][1])
            ans = max(ans, dp[i][1], dp[i][0])
        return ans
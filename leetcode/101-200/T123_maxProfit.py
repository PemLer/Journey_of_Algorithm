class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        dp = [0 for _ in range(len(prices))]
        min_num = prices[0]
        for i in range(1, len(prices)):
            dp[i] = max(dp[i-1], prices[i] - min_num)
            min_num = min(min_num, prices[i])
        
        max_num = prices[-1]
        res = dp[-1]
        for i in range(len(prices)-1, 0, -1):
            if prices[i] < max_num:
                res = max(res, max_num - prices[i] + dp[i-1])
            max_num = max(max_num, prices[i])
        return res

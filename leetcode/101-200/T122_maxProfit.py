class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            diff = prices[i+1] - prices[i]
            if diff > 0:
                profit += diff
        return profit
        

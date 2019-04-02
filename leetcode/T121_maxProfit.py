class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        pro = 0
        min_num = prices[0]
        for i in range(1, len(prices)):
            pro = max(pro, prices[i]-min_num)
            min_num = min(min_num, prices[i])
        return pro

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        对于每一步都选择最优的策略
        """
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash


if __name__ == '__main__':
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    sol = Solution()
    print(sol.maxProfit(prices, fee))

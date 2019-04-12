class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for x in coins:
                if x <= i and dp[i-x] != (amount+1):
                    dp[i] = min(dp[i-x]+1,dp[i])
        if dp[-1] == amount+1:
            return -1
        return dp[-1]
        


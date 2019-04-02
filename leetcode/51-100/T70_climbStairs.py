class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        condition = [0] * (n + 1)
        condition[0] = 1
        condition[1] = 1
        for i in range(2, n+1):
            condition[i] = condition[i-1] + condition[i-2]
        return condition[n]

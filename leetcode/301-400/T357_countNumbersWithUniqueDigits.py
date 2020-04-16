class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        dp = [0] * n
        dp[0] = 10
        factor = 9
        for i in range(1, n):
            factor *= (10 - i)
            factor = max(0, factor)
            dp[i] = dp[i-1] + factor
        return dp[n-1]


if __name__ == '__main__':
    sol = Solution()
    for i in range(15):
        print(sol.countNumbersWithUniqueDigits(i+1))

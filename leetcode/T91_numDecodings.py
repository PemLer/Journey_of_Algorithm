class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        dp = [0]*(l+1)
        if l == 0 or s[0] == '0':
            return 0
        dp[0],dp[1] = 1,1

        for i in range(2,l+1):
            if 10 <= int(s[i-2:i]) <= 26 and s[i-1] != '0':
                dp[i] = dp[i-1]+dp[i-2]
            elif int(s[i-2:i]) == 10 or int(s[i-2:i]) == 20:
                dp[i] = dp[i-2]
            elif s[i - 1] != '0':
                dp[i] = dp[i - 1]
            else:
                return 0
        return dp[l]


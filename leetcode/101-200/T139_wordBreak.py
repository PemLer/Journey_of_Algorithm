class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        m = len(s)
        dp = [True] + [False] * m
        for i in range(0,m):
            for j in range(0,i+1):
                if dp[j] == True and s[j:i+1] in wordDict:
                    dp[i+1] = True
                    break
        return dp[m]

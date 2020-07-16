class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        max_len = 0
        record = set()
        for word in dictionary:
            record.add(word)
            max_len = max(max_len, len(word))

        n = len(sentence)
        dp = [n] * (n + 1)
        dp[0] = 0

        for i in range(n):
            for j in range(max(0, i - max_len), i+1):
                word = sentence[j:i+1]
                if word in record:
                    dp[i+1] = min(dp[j], dp[i+1])
                else:
                    dp[i+1] = min(dp[i]+1, dp[i+1])
        return dp[-1]

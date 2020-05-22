class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        if not books or not books[0]:
            return 0
        n = len(books)

        pre_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            pre_sum[i] += pre_sum[i - 1] + books[i - 1][0]

        dp = [0] * (n + 1)
        for i in range(1, n+1):
            dp[i] += dp[i - 1] + books[i-1][1]

        for i in range(1, n):
            cur_height = 0
            for j in range(i, -1, -1):
                if pre_sum[i + 1] - pre_sum[j] <= shelf_width:
                    if books[j][1] > cur_height:
                        cur_height = books[j][1]
                    dp[i+1] = min(dp[i+1], dp[j] + cur_height)
        return dp[-1]
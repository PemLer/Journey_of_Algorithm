class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        """
        dp[i] = min(dp[i], dp[j] + max_height(j, i))
        """
        if not books or not books[0]:
            return 0
        n = len(books)

        # 前缀和记录厚度之和
        pre_sum = [0] * (n + 1)
        # 初始化为最大的高度
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            pre_sum[i] += pre_sum[i - 1] + books[i - 1][0]
            dp[i] += dp[i - 1] + books[i - 1][1]

        for i in range(1, n):
            cur_height = 0
            j = i
            while j >= 0 and pre_sum[i + 1] - pre_sum[j] <= shelf_width:
                if books[j][1] > cur_height:
                    cur_height = books[j][1]
                dp[i + 1] = min(dp[i + 1], dp[j] + cur_height)
                j -= 1
        return dp[-1]

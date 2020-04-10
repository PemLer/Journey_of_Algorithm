from typing import List


class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        stack.append(-1)
        max_area = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                max_area = max(max_area, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)

        while stack[-1] != -1:
            max_area = max(max_area, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        return max_area

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [0] * n
        ans = 0
        for i in range(m):
            for j in range(n):

                if matrix[i][j] == '1':
                    dp[j] += 1
                else:
                    dp[j] = 0

            ans = max(ans, self.largestRectangleArea(dp))
        return ans
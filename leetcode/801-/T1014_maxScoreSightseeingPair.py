class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        """
        A[i] + A[j] + i - j
        A[i] + i + A[j] - j
        """
        n = len(A)
        mx, ans = A[0], 0
        for j in range(1, n):
            ans = max(ans, mx + A[j] - j)
            mx = max(mx, A[j] + j)
        return ans
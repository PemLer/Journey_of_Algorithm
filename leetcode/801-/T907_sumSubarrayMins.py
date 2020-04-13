from typing import List

class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(A)
        left = [0] * n
        stack = []
        for i in range(n):
            while stack and A[stack[-1]] > A[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            else:
                left[i] = -1
            stack.append(i)

        stack = []
        right = [0] * n
        for i in range(n-1, -1, -1):
            while stack and A[stack[-1]] >= A[i]:  # 这里需要取等号，因为两者相等时最小值默认取前者
                stack.pop()
            if stack:
                right[i] = stack[-1]
            else:
                right[i] = n
            stack.append(i)

        ans = 0
        for i in range(n):
            ans += A[i] * (i - left[i]) * (right[i] - i)
            ans %= mod

        return ans


# 一次遍历
class Solution2:
    def sumSubarrayMins(self, A: List[int]) -> int:
        mod = 10 ** 9 + 7

        A = [float('-inf')] + A + [float('-inf')]
        stack = []
        ans = 0
        for i, a in enumerate(A):
            while stack and A[stack[-1]] > a:
                cur = stack.pop()
                ans += A[cur] * (cur - stack[-1]) * (i - cur)
            stack.append(i)
        return ans % mod
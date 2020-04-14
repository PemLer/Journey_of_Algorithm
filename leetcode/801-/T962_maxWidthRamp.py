from typing import List


class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        stack = []
        n = len(A)
        for i in range(n):
            if not stack or A[stack[-1]] > A[i]:
                stack.append(i)

        res = 0
        i = n - 1
        while i > res:  # 当res大于等于i时没必要继续遍历了
            while stack and A[stack[-1]] <= A[i]:
                res = max(res, i - stack[-1])
                stack.pop()
            i -= 1

        return res


if __name__ == '__main__':
    sol = Solution()
    nums = [
        [6, 0, 8, 2, 1, 5],
        [9, 8, 1, 0, 1, 9, 4, 0, 4, 1]
    ]
    for num in nums:
        print(sol.maxWidthRamp(num))

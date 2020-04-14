from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        nums_code = []
        for hour in hours:
            if hour > 8:
                nums_code.append(1)
            else:
                nums_code.append(-1)

        # 前缀和
        nums_pre_sum = []
        cur = 0
        for i in range(len(nums_code)):
            nums_pre_sum.append(cur)
            cur += nums_code[i]
        nums_pre_sum.append(cur)

        stack = []
        for i in range(len(nums_pre_sum)):
            if not stack or nums_pre_sum[stack[-1]] > nums_pre_sum[i]:
                stack.append(i)

        res = 0
        for i in range(len(nums_pre_sum)-1, -1, -1):
            while stack and nums_pre_sum[stack[-1]] < nums_pre_sum[i]:
                res = max(res, i - stack[-1])
                stack.pop()

        return res


if __name__ == '__main__':
    sol = Solution()
    hours = [
        [9, 9, 6, 0, 6, 6, 9],
        [9],
        [7],
        [8, 7],
        [6, 5, 9, 7],
        [6, 4, 9, 1, 10, 2],
        [6, 4, 9, 10]
    ]
    for hour in hours:
        print(sol.longestWPI(hour))

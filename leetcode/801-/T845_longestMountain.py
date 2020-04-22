from typing import List


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        i, n = 0, len(A)
        if n < 3:
            return 0
        res = 0
        while i < n:
            end = i
            if end + 1 < n and A[end] < A[end+1]:
                while end + 1 < n and A[end] < A[end+1]:
                    end += 1

                if end + 1 < n and A[end] > A[end+1]:
                    while end + 1 < n and A[end] > A[end+1]:
                        end += 1

                    res = max(res, end - i + 1)
            i = max(end, i+1)

        return res


if __name__ == '__main__':
    sol = Solution()
    A = [1, 2, 3, 1]
    print(sol.longestMountain(A))

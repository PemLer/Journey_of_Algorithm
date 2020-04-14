from typing import List


class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        """
        [10, 13, 12, 14, 15]
        [2, 3, 3, 4, -1]
        [-1, 2, -1, -1, -1]

         0  1  2  3  4
        [2, 3, 1, 1, 4]
        [1, 4, 3, 4, -1]
        [2, 2, 3, -1, -1]
        """
        n = len(A)
        odd = [-1] * n
        even = [-1] * n
        stack = []
        for i, a in enumerate(A):
            while stack and a >= A[stack[-1]]:
                v = stack.pop()
                odd[v] = i
            stack.append(i)

        stack = []
        for i, a in enumerate(A):
            while stack and a <= A[stack[-1]]:
                v = stack.pop()
                even[v] = i
            stack.append(i)

        ans = 1
        path = [odd, even]
        print(path)
        k = 1
        for i in range(n-1):
            next_i = i
            while next_i != -1:
                next_i = path[k % 2][next_i]
                k += 1
            if next_i == n - 1:
                ans += 1

        return ans


if __name__ == '__main__':
    sol = Solution()
    A = [10, 13, 12, 14, 15]
    print(sol.oddEvenJumps(A))

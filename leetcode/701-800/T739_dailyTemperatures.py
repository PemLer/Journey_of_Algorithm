from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        i = 0
        res = [0] * len(T)
        while i < len(T):
            while stack and T[i] > T[stack[-1]]:
                v = stack.pop()
                res[v] = i - v
            stack.append(i)
            i += 1
        while stack:
            v = stack.pop()
            res[v] = 0
        return res


if __name__ == '__main__':
    sol = Solution()
    temperatures = [73]
    print(sol.dailyTemperatures(temperatures))

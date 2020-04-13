from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i, n = 0, len(asteroids)
        while i < n:
            cur = asteroids[i]
            while stack and stack[-1] > 0 and cur < 0:
                v = stack.pop()
                if abs(v) == abs(cur):
                    cur = 0
                else:
                    cur = v if abs(v) > abs(cur) else cur
            if cur:
                stack.append(cur)
            i += 1
        return stack


if __name__ == '__main__':
    sol = Solution()
    asteroids = [
        [5, 10, -5],
        [8, -8],
        [10, 2, -5],
        [-2, -1, 1, 2],
        [-1, 10, -1, -2, -3, -11],
        [-1],
        []
    ]
    for a in asteroids:
        print(sol.asteroidCollision(a))
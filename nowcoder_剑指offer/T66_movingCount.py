# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        def axis_to_num(x, y):
            return sum(map(int, list(str(x)))) + sum(map(int, list(str(y))))

        def dfs(r, c, memories):
            print(memories)
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            for i in range(4):
                x = dx[i] + r
                y = dy[i] + c
                if 0 <= x < rows and 0 <= y < cols and memories[x][y] and axis_to_num(x, y) <= threshold:
                    memories[x][y] = False
                    dfs(x, y, memories)

        memories = [[True for _ in range(cols)] for __ in range(rows)]
        memories[0][0] = False
        dfs(0, 0, memories)
        print(memories)
        count = 0
        for items in memories:
            for element in items:
                if not element:
                    count += 1
        return count

sol = Solution()
print(sol.movingCount(-10,5,5))

# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        def dfs(r, c, s, memories):
            if not s:
                return True
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            for i in range(4):
                x = dx[i] + r
                y = dy[i] + c
                if (0 <= x < rows) and (0 <= y < cols) and memories[x][y] and matrix[x*cols+y] == s[0]:
                    memories[x][y] = False
                    if dfs(x, y, s[1:], memories):
                        return True
                    memories[x][y] = True
            return False


        if not path:
            return True
        memories = [[True for _ in range(cols)] for __ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i*cols+j] == path[0]:
                    memories[i][j] = False
                    if dfs(i, j, path[1:], memories):
                        return True
                    memories[i][j] = True
        return False


sol = Solution()
print(sol.hasPath("ABCESFCSADEE",3,4,"ABCCED"))
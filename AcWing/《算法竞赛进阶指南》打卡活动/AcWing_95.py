"""
1 穷举第一行 2^5
2 遍历前四行，如果grid[i][j]为0，以grid[i+1][j]为中心按灯
3 检查最后一行是否都为1，都为1且按灯次数小于6时满足条件
4 获取最小的次数
"""
import copy

def turn(x, y, grid):
    dx = [0, 1, 0, -1, 0]
    dy = [0, 0, 1, 0, -1]
    for i in range(5):
        a, b = x + dx[i], y + dy[i]
        if 0 <= a < 5 and 0 <= b < 5:
            grid[a][b] ^= 1


def is_successful(grid):
    flag = True
    for j in range(5):
        if grid[4][j] == 0:
            flag = False
            break
    return flag


def solve(grid_ori):
    
    ans = 1000
    for i in range(32):
        
        grid = copy.deepcopy(grid_ori)
        count = 0
        for j in range(5):
            if i >> j & 1:
                turn(0, j, grid)
                count += 1
                
        for i in range(4):
            for j in range(5):
                if not grid[i][j]:
                    turn(i+1, j, grid)
                    count += 1
                    
        if count <= 6 and is_successful(grid):
            ans = min(ans, count)
    if ans != 1000:
        return ans
    else:
        return -1
    
    
times = int(input())
ans = []
for _ in range(times):

    grid = [[-1] * 5 for _ in range(5)]
    for i in range(5):
        s = input()
        if not s:
            s = input()
        for j, c in enumerate(s):
            grid[i][j] = int(c)

    res = solve(grid)
    ans.append(res)
for a in ans:
    print(a)

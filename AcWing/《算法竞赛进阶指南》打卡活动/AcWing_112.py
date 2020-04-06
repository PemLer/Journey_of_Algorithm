import math

# 获取输入
n, d = map(int, input().split())

islands = [[0] * 2 for _ in range(n)]
for i in range(n):
    islands[i][0], islands[i][1] = map(int, input().split())


def main():
    # 将island的(x, y)转化为x轴上的(l, r)
    for i in range(n):
        x, y = islands[i]
        tmp = d ** 2 - y ** 2
        if tmp < 0:
            return -1
        l, r = x - math.sqrt(tmp), x + math.sqrt(tmp)
        islands[i] = [l, r]

    # 按l从小到大排序
    islands.sort(key=lambda x: x[0])
    pos = float('-inf')
    ans = 0
    for l, r in islands:
        if l > pos:
            ans += 1
            pos = r
        else:
            pos = min(pos, r)
    return ans


print(main())
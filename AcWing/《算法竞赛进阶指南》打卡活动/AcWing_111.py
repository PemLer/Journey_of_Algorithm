# 读取数据
n = int(input())
cows = [[0] * 3 for _ in range(n)]
for i in range(n):
    cows[i][0], cows[i][1], cows[i][2]= *map(int, input().split()), i

# 按开始时间从小到大排序
cows.sort(key=lambda x: x[0])

s = []
res = [0] * n
for tup in cows:
    start, end, i = tup
    if not s:  # 开始时s为空
        s.append(end)
        res[i] = 0
    else:
        # 遍历s，寻找一个合适的畜栏
        for j, t in enumerate(s):
            if start > t:
                s[j] = end
                res[i] = j
                break
        else:  # 在已有的畜栏中没有合适的
            s.append(end)
            res[i] = len(s) - 1

# 打印结果
print(len(s))
for r in res:
    print(r+1)
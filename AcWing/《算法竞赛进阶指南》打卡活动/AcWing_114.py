# 获取输入
n = int(input())
l_k, r_k = map(int, input().split())
array = [[0] * 3 for _ in range(n)]
for i in range(n):
    l, r = map(int, input().split())
    array[i] = [l, r, l * r]

array.sort(key=lambda x: x[2])

ans = 0
tmp = l_k
for l, r, _ in array:
    total = tmp // r
    ans = max(ans, total)
    tmp *= l

print(ans)
# 读入数据
C, L = map(int, input().split())

min_max_SPF = [[0] * 2 for _ in range(C)]
for i in range(C):
    m1, m2 = map(int, input().split())
    min_max_SPF[i][0], min_max_SPF[i][1] = m1, m2

SPF_cover = [[0] * 2 for _ in range(L)]
for i in range(L):
    s, c = map(int, input().split())
    SPF_cover[i][0], SPF_cover[i][1] = s, c

# 按min从从大到小排序
min_max_SPF.sort(key=lambda x: x[0], reverse=True)
SPF_cover.sort(key=lambda x: x[0], reverse=True)
# print(min_max_SPF)
# print(SPF_cover)


ans = 0
# 遍历
for m1, m2 in min_max_SPF:

    for i, tup in enumerate(SPF_cover):
        SPF, cover = tup
        if m1 <= SPF <= m2 and cover > 0:
            # print(m1, m2, SPF, cover)
            SPF_cover[i][1] -= 1
            ans += 1
            break

print(ans)
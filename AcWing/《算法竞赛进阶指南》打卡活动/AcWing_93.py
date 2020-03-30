def solve(n, m):
    res = []
    dfs(1, n, [], res, 0, m)
    return res


def dfs(cur, n, tmp, res, count, m):
    if count == m:
        res.append(tmp)
        return
    if cur == n + 1:
        return

    dfs(cur+1, n, tmp+[cur], res, count+1, m)
    dfs(cur+1, n, tmp, res, count, m)

n, m = map(int, input().split())
res = solve(n, m)
for r in res:
    print(' '.join(map(str, r)))

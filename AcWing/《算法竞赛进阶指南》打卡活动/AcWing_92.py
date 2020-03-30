def solve(n):
    res = []
    dfs(1, n, [], res)
    return res


def dfs(cur, n, tmp, res):
    if cur == n+1:
        res.append(tmp)
        return
    dfs(cur+1, n, tmp, res)
    dfs(cur+1, n, tmp+[cur], res)

n = int(input())
res = solve(n)
for r in res:
    print(' '.join(map(str, r)))


def solve(n):
    res = []
    dfs(list(range(1, n+1)), [], res, n)
    return res


def dfs(nums, tmp, res, n):
    if len(tmp) == n:
        res.append(tmp)
        return

    for i in range(len(nums)):
        dfs(nums[:i]+nums[i+1:], tmp+[nums[i]], res, n)

n = int(input())
res = solve(n)
for r in res:
    print(' '.join(map(str, r)))

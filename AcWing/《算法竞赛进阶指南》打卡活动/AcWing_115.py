class Node:
    father = 0
    sum = 0
    size = 1
    avg = 0


def find():
    avg = 0
    res = -1
    for i in range(1, n + 1):
        if i != root and nodes[i].avg > avg:
            avg = nodes[i].avg
            res = i
    return res


n, root = map(int, input().split())
nodes = [Node() for _ in range(n + 1)]

ans = 0
for i, num in enumerate(map(int, input().split())):
    nodes[i + 1].sum = num
    nodes[i + 1].avg = nodes[i + 1].sum
    ans += nodes[i + 1].sum

for i in range(n - 1):
    a, b = map(int, input().split())
    nodes[b].father = a

for i in range(n - 1):
    p = find()
    f = nodes[p].father
    ans += nodes[p].sum * nodes[f].size
    nodes[p].avg = -1
    for j in range(1, n + 1):
        if nodes[j].father == p:
            nodes[j].father = f
    nodes[f].sum += nodes[p].sum
    nodes[f].size += nodes[p].size
    nodes[f].avg = nodes[f].sum / nodes[f].size

print(ans)


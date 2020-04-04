"""
差分序列
"""

n = int(input())

a = [0] * 100010

for i in range(1, n + 1):
    a[i] = int(input())

for i in range(n, 0, -1):
    a[i] -= a[i - 1]

pos, neg = 0, 0
for i in range(2, n + 1):
    if a[i] > 0:
        pos += a[i]
    else:
        neg -= a[i]

print(min(pos, neg) + abs(pos - neg))
print(abs(pos - neg) + 1)
d, f = [0] * 15, [99999] * 15
d[1] = 1

for i in range(2, 13):
    d[i] = 1 + d[i-1] * 2

f[0] = 0
for i in range(1, 13):
    for j in range(0, i):
        f[i] = min(f[i], f[j] * 2 + d[i - j])

for num in f[1:13]:
    print(num)

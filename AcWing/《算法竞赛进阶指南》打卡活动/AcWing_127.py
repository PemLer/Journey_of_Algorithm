
while True:
    try:
        n, m = map(int, input().split())
    except EOFError:
        break

    machines = [[0] * 2 for _ in range(n)]
    tasks = [[0] * 2 for _ in range(m)]
    for i in range(n):
        machines[i][0], machines[i][1] = map(int, input().split())
    for i in range(m):
        tasks[i][0], tasks[i][1] = map(int, input().split())

    machines.sort(key=lambda x: (x[0], x[1]))
    tasks.sort(key=lambda x: (x[0], x[1]))

    # print(machines)
    # print(tasks)

    ys = []
    ans, count = 0, 0
    j = n - 1
    for i in range(m - 1, -1, -1):
        x, y = tasks[i][0], tasks[i][1]
        while j >= 0 and machines[j][0] >= x:
            ys.append(machines[j][1])
            j -= 1
        # print(dic)
        t = 0
        ys.sort()
        while t < len(ys):
            key = ys[t]
            if key >= y:
                ans += 500 * x + 2 * y
                ys.pop(t)
                count += 1
                # print(x, y)
                break
            else:
                t += 1

    print(count, ans)
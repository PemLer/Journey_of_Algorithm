n = int(input())
cnt = 20


def dfs(state1, state2, state3, n):
    global cnt
    if not cnt:
        return
    if len(state1) == n:
        for s in state1:
            print(s, end='')
        print()
        cnt -= 1

    if state2:
        value = state2.pop()
        state1.append(value)
        dfs(state1, state2, state3, n)
        state2.append(value)
        state1.pop()

    if state3 < n:
        state3 += 1
        state2.append(state3)
        dfs(state1, state2, state3, n)
        state3 -= 1
        state2.pop()


dfs([], [], 0, n)


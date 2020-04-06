"""
get_order: (x, y) -> order
main:
    1 读取输入，将矩阵读取为一个16位的二进制数
    2 获取change[i][j]矩阵，存储对每个数操作时应该异或的值
    3 进行2^16次遍历，记录过程
"""


def get_order(x, y):
    return 4 * x + y


def main():
    state = 0
    for i in range(4):
        string = input()
        for j, char in enumerate(string):
            if char == '+':
                state += 1 << get_order(i, j)

    change = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                change[i][j] += 1 << get_order(i, k)
                change[i][j] += 1 << get_order(k, j)

            change[i][j] -= 1 << get_order(i, j)

    res = []
    for k in range(1 << 16):
        now = state
        path = []
        for i in range(16):
            if k >> i & 1:
                x, y = i // 4, i % 4
                now ^= change[x][y]
                path.append((x, y))

        if not now and (not res or len(path) < len(res)):
            res = path[:]

    print(len(res))
    for x, y in res:
        print(x+1, y+1)


main()
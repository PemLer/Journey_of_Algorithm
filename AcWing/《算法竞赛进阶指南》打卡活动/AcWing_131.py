# 接受输入
while True:
    line = input()
    if line == '0':
        break
    items = list(map(int, line.split()))
    n = items[0]
    heights = items[1:]

    stack = [-1]

    ans = 0
    for i in range(n):
        if heights[i] > heights[stack[-1]]:
            stack.append(i)
        else:
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                ans = max(ans, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)

    while stack[-1] != -1:
        ans = max(ans, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
    print(ans)

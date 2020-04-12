string = input()

ans = 0
stack = []
for i in range(len(string)):
    c = string[i]
    if stack:
        t = string[stack[-1]]
        if c == ')' and t == '(' or c == ']' and t == '[' or c == '}' and t == '{':
            stack.pop()
        else:
            stack.append(i)
    else:
        stack.append(i)

    if stack:
        ans = max(ans, i - stack[-1])
    else:
        ans = max(ans, i + 1)

print(ans)

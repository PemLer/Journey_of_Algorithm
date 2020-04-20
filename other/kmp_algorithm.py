def gen_next(p):
    """生成针对p中各位置i的下一检查位置表，用于KMP算法"""
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m - 1:  # 生成下一个pnext元素
        if k == -1 or p[i] == p[k]:
            i, k = i + 1, k + 1
            if p[i] == p[k]:
                pnext[i] = pnext[k]
            else:
                pnext[i] = k
        else:
            k = pnext[k]
    return pnext


def kmp(t, p, pnext):
    i, j = 0, 0
    n, m = len(t), len(p)
    while j < n and i < m:           # i==m说明找到了匹配
        if i == -1 or t[j] == p[i]:  # 考虑p中下一字符
            j, i = j + 1, i + 1
        else:                        # 失败！考虑pnext决定下一字符
            i = pnext[i]
    if i == m:                       # 找到匹配，返回其下标
        return j - 1
    return -1                        # 无匹配，返回特殊值


if __name__ == '__main__':
    t = 'abcjkasbvhjabcxabcdabcjafkladsnfjbaabcdabcybvcasdlhkvbjkads'
    p = 'abcdabcy'
    pnext = gen_next(p)
    res = kmp(t, p, pnext)
    print(res)

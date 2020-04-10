from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        items = logs[0].split(':')
        index, prev = int(items[0]), int(items[2])
        stack.append(index)

        for log in logs[1:]:
            index, tag, t = log.split(':')
            if tag == 'start':
                if stack:
                    res[stack[-1]] += int(t) - prev
                stack.append(int(index))
                prev = int(t)
            else:
                res[stack[-1]] += int(t) - prev + 1
                stack.pop()
                prev = int(t) + 1

        return res

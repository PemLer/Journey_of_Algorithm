from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort()

        pos = intervals[0][1]
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= pos:
                res[-1][1] = max(pos, intervals[i][1])
                pos = max(pos, intervals[i][1])
            elif intervals[i][0] > pos:
                res.append(intervals[i])
                pos = intervals[i][1]
        return res


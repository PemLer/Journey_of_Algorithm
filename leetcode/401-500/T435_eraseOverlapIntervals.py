# 方法一 对起点进行排序

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n == 0:
            return 0
        intervals.sort(key=lambda x: (x[0]))
        prev = intervals[0][1]
        ans = 0
        for i in range(1, n):
            if intervals[i][0] < prev:
                if intervals[i][1] < prev:
                    prev = intervals[i][1]
                ans += 1
            else:
                prev = intervals[i][1]
        return ans

# 方法二 对终点进行排序

class Solution1:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n == 0:
            return 0
        intervals.sort(key=lambda x: (x[1]))
        prev = intervals[0][1]
        ans = 1
        for i in range(1, n):
            if intervals[i][0] >= prev:
                prev = intervals[i][1]
                ans += 1
        return len(intervals) - ans
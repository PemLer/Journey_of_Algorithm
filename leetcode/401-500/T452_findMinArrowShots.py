class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        pos = float('-inf')
        count =  0
        for start, end in points:
            if start > pos:
                pos = end
                count += 1
            else:
                pos = min(pos, end)

        return count
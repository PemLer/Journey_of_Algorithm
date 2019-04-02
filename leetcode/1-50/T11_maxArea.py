import json
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        a = 0
        b = len(height)-1
        d = 0
        while a < b:
            d = max(d,(b-a)*min(height[a],height[b]))
            if height[a] < height[b]:
                a += 1
            else:
                b -= 1
        return d

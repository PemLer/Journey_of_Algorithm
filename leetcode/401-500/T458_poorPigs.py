class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        count = minutesToTest // minutesToDie + 1
        res,t = 1,0
        while True:
            if res >= buckets:
                break
            res *= count
            t += 1
        return t

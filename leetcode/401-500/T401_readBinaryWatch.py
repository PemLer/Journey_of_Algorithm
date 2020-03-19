class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        """
        8 4 2 1
        32 16 8 4 2 1
        """
        elements = [(0, 1), (0, 2), (0, 4), (0, 8), (1, 1), (1, 2), (1, 4), (1, 8), (1, 16), (1, 32)]
        hour, minute = 0, 0
        self.res = []
        self.dfs(elements, 0, num, hour, minute)
        return self.res

    def dfs(self, elements, index, count, hour, minute):
        if count == 0:
            if hour < 12 and minute < 60:
                if minute < 10:
                    self.res.append("{}:0{}".format(hour, minute))
                else:
                    self.res.append("{}:{}".format(hour, minute))
            return
        if index == len(elements):
            return
        for i in range(index, len(elements)):
            key, num = elements[i]
            if key == 0:
                self.dfs(elements, i+1, count-1, hour+num, minute)
            else:
                self.dfs(elements, i+1, count-1, hour, minute+num)


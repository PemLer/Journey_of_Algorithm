from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]
        for i in range(rowIndex):
            tmp = [1]
            for j in range(1, len(res[-1])):
                tmp.append(res[-1][j]+res[-1][j-1])
            tmp.append(1)
            res.append(tmp)
        return res[-1]


class Solution1:
    def getRow(self, rowIndex: int) -> List[int]:
        temp = 1
        res = [0] * (rowIndex + 1)
        for i in range(rowIndex + 1):
            res[i] = temp
            temp = temp * (rowIndex - i) // (i + 1)
        return res
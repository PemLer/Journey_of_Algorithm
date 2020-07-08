class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        res = []
        if k == 0:
            return res
        if shorter == longer:
            return [shorter * k]
        for i in range(k+1):
            res.append(longer * i + shorter * (k - i))

        return res
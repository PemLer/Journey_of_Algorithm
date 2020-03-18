class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = set()
        tmp = set()
        for i in range(len(s) - 9):
            key = s[i:i+10]
            if key in tmp:
                res.add(key)
            else:
                tmp.add(key)
        return list(res)

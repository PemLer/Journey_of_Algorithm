class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        use = set()
        for a, b in zip(s, t):
            if a in d and d[a] != b:
                return False
            elif a not in d and b in use:
                return False
            elif a not in d:
                d[a] = b
                use.add(b)

        return True

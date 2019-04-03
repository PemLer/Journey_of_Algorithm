class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        ss1 = sorted(s1)
        ss2 = sorted(s2)
        if ss1 != ss2:
            return False
        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[len(s2)-i:]) and self.isScramble(s1[i:], s2[:len(s2)-i]):
                return True
        return False

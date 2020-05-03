class Solution:
    def replaceSpace(self, s: str) -> str:
        chars = list(s)
        for i in range(len(chars)):
            if chars[i] == ' ':
                chars[i] = '%20'
        return ''.join(chars)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        import re
        exist = re.search(p, s)
        if exist and exist.group(0) == s:
            return True
        else:
            return False
            

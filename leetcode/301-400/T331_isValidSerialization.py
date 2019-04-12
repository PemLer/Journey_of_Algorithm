class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if not preorder:
            return False
        lst = preorder.split(',')
        if lst[0] == '#' and len(lst) == 1:
            return True
        if lst[0] == '#' and len(lst) > 1:
            return False
        count = 1
        for node in lst:
            count -= 1
            if count < 0:
                return False
            if node != '#':
                count += 2
        return count == 0
            

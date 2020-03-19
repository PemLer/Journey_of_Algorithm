class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def helper(num):
            a = 0b10000000
            count = 0
            for _ in range(8):
                if num & a != 0:
                    count += 1
                    a >>= 1
                else:
                    break
            return count

        flag = True
        i = 0
        while i < len(data):
            key = helper(data[i])
            if key == 0:
                i += 1
            else:
                i += 1
                if i + key - 1 <= len(data) and 1 < key <= 4:
                    for j in range(i, i+key-1):
                        if helper(data[j]) != 1:
                            flag = False
                            break
                    i = j + 1
                else:
                    flag = False
                    break
        return flag


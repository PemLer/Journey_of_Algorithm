import collections


class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        n = len(value)
        count = collections.Counter(pattern)
        la = count.get('a', 0)  # a的个数
        lb = count.get('b', 0)  # b的个数
        if la == 0 and lb == 0:
            if n == 0:
                return True
            else:
                return False
        elif la == 0:
            if n % lb != 0:
                return False
            j = n // lb
            tb = value[0:j]
            pos = 0
            for char in pattern:
                t = value[pos:pos+j]
                if t == tb:
                    pos += j
                else:
                    break
            else:
                return True
        elif lb == 0:
            if n % la != 0:
                return False
            i = n // la
            ta = value[0:i]
            pos = 0
            for char in pattern:
                t = value[pos:pos+i]
                if t == ta:
                    pos += i
                else:
                    break
            else:
                return True
        # 0-n//la
        else:
            for i in range(n // la + 1):
                j = (n - la * i) // lb
                # i: a代表的长度
                # j: b代表的长度
                if la * i + lb * j != n:
                    continue
                ta = None
                tb = None
                pos = 0
                for char in pattern:
                    if char == 'a':
                        t = value[pos:pos + i]
                        if ta:
                            if ta == t:
                                pos += i
                            else:
                                break
                        else:
                            ta = t
                            pos += i
                    else:
                        t = value[pos:pos + j]
                        if tb:
                            if tb == t:
                                pos += j
                            else:
                                break
                        else:
                            tb = t
                            pos += j
                else:
                    # print(ta, tb)
                    if ta == tb:
                        return False
                    return True
        return False

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split('.')
        ver2 = version2.split('.')
        index1, index2 = 0, 0
        len1, len2 = len(ver1), len(ver2)
        while index1 < len1 or index2 < len2:
            if index1 == len1:
                if int(ver2[index2]) > 0:
                    return -1
                else:
                    index2 += 1
                    continue
            if index2 == len2:
                if int(ver1[index1]) > 0:
                    return 1
                else:
                    index1 += 1
                    continue
            cur1 = int(ver1[index1])
            cur2 = int(ver2[index2])
            if cur1 == cur2:
                index1 += 1
                index2 += 1
            elif cur1 > cur2:
                return 1
            else:
                return -1
        return 0

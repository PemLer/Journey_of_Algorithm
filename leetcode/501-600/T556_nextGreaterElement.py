class Solution:
    def nextGreaterElement(self, n: int) -> int:
        """
        123 132
        2143 2314
        45671 45716
        234321 14 3321
        """
        base = 2 ** 31
        n = list(str(n))
        i = len(n) - 2
        while i >= 0:
            if n[i] < n[i+1]:
                j = i + 1
                while j < len(n) and n[j] > n[i]:
                    j += 1
                n[i], n[j-1] = n[j-1], n[i]
                n[i+1:] = sorted(n[i+1:])
                break
            i -= 1
        else:
            return -1
        res = int(''.join(n))
        return res if res < base else -1


if __name__ == '__main__':
    sol = Solution()
    n = 2147483647
    print(sol.nextGreaterElement(n))

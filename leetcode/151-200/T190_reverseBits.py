class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        a = str(bin(n))
        b = (34-len(a))*'0' + a[2:]
        c = b[::-1]
        d = int(c,2)
        return d


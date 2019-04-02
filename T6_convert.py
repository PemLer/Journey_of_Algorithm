class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n = len(s)
        if numRows == 1:
            return s
        row_start = s[0:n:2 * (numRows - 1)]
        row_end = s[numRows - 1:n:2 * (numRows - 1)]
        if numRows == 2:
            return row_start + row_end
        A = ['']*(numRows-2)
        j = -1
        sign = 0
        for i in range(1,n):
            if i %(numRows-1) == 0:
                continue
            if sign == 0:
                j += 1
            else:
                j -= 1
            # print(j)
            A[j] += s[i]
            if j == len(A)-1 and sign == 0:
                sign = 1
                j = len(A)
            elif j == 0 and sign == 1:
                sign = 0
                j = -1

        row_mid = ''
        for i in A:
            row_mid += i
        return row_start + row_mid + row_end


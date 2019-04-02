class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        count = 1
        res = []
        for i in range(numRows):
            sub = []
            for j in range(count):
                if j == 0 or j == count-1:
                    sub.append(1)
                else:
                    sub.append(res[i-1][j-1]+res[i-1][j])
            count += 1
            res.append(sub)
        return res
                
        

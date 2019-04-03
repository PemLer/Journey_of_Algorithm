class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        are_A = (C - A) * (D - B)
        are_B = (G - E) * (H - F)
        lx,ly,rx,ry = max(A,E),max(B,F),min(C,G),min(D,H)
        if lx >= rx or ly >= ry: are_C = 0
        else: are_C = (rx-lx)*(ry-ly)
        return are_A+are_B-are_C

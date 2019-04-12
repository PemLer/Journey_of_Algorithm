class Solution:
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        #envelopes.sort()
        envelopes.sort(key = lambda x:(x[0],-x[1]))
        # print(envelopes)
        n = len(envelopes)
        ans = []
        for i in range(n):
            low = 0
            high = len(ans)-1
            while low <= high:
                mid = int((low+high)/2)
                if ans[mid][0] < envelopes[i][0] and ans[mid][1] < envelopes[i][1]:
                    low = mid +1
                else:
                    high = mid-1

            if low>=len(ans):
                ans.append(envelopes[i])
            else:
                ans[low] = envelopes[i]
        return len(ans)


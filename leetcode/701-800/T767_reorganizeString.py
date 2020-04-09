from heapq import heappush, heappop, heapify


class Solution:
    def reorganizeString(self, S: str) -> str:
        pq = [(-S.count(x), x) for x in set(S)]
        heapify(pq)

        tup = heappop(pq)
        if -tup[0] > (len(S) + 1) / 2:
            return ''
        heappush(pq, tup)

        res = []
        while len(pq) >= 2:
            count1, char1 = heappop(pq)
            count2, char2 = heappop(pq)
            res.extend([char1, char2])
            if count1 + 1:
                heappush(pq, (count1 + 1, char1))
            if count2 + 1:
                heappush(pq, (count2 + 1, char2))

        return ''.join(res) + (pq[0][1] if pq else '')
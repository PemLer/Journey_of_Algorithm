from typing import List
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        6 5 5 5
        last = 1
        res = (6 - 1) * (2 + 1) + 1 = 16
        max(16, 21)
        """
        ct = Counter(tasks)
        nbucket = ct.most_common(1)[0][1]
        last_bucket_size = list(ct.values()).count(nbucket)
        res = (nbucket - 1) * (n + 1) + last_bucket_size
        return max(res, len(tasks))
import collections
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        dic = collections.defaultdict(int)
        dic[0] = 1
        total, ans = 0, 0
        for num in nums:
            if num % 2 == 1:
                total += 1
            if total - k in dic:
                ans += dic[total - k]
            dic[total] += 1

        return ans

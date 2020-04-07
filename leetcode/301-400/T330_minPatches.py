from typing import List
"""
如果添加的数字是x，[1, miss)和[x, miss+x)均被覆盖。
如果 x<=miss，则miss=miss+x
否则 添加miss，覆盖范围到 miss+x就尽可能大
"""

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches, i = 0, 0
        miss = 1
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                patches += 1
        return patches
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []

        nums.sort()

        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                start, end = j + 1, n - 1
                while start < end:
                    total = nums[i] + nums[j] + nums[start] + nums[end]
                    if total > target:
                        end -= 1
                    elif total < target:
                        start += 1
                    else:
                        res.append([nums[i], nums[j], nums[start], nums[end]])
                        while start < end and nums[start] == nums[start + 1]:
                            start += 1
                        while start < end and nums[end] == nums[end - 1]:
                            end -= 1
                        start += 1
                        end -= 1
        return res



from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        ans = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            start, end = i + 1, len(nums) - 1
            while start < end:
                total = nums[i] + nums[start] + nums[end]
                if abs(total - target) < abs(ans - target):
                    ans = total

                if total < target:
                    start += 1
                elif total > target:
                    end -= 1
                else:
                    return target
        return ans
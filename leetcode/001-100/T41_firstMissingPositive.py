from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                index = nums[i] - 1
                nums[i], nums[index] = nums[index], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1


if __name__ == '__main__':
    sol = Solution()
    nums = [3, 4, 2, 1]
    print(sol.firstMissingPositive(nums))

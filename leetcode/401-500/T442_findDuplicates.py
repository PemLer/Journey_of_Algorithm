from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        for i in range(n):
            while nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                index = nums[i] - 1
                nums[i], nums[index] = nums[index], nums[i]
        for i in range(n):
            if nums[i] != i + 1:
                res.append(nums[i])
        return res


if __name__ == '__main__':
    sol = Solution()
    nums = [3, 11, 8, 16, 4, 15, 4, 17, 14, 14, 6, 6, 2, 8, 3, 12, 15, 20, 20, 5]
    print(sol.findDuplicates(nums))

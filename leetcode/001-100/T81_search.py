from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + right >> 1
            if nums[mid] == target:
                return True
            if nums[left] == nums[mid]:
                left += 1
                continue

            if nums[left] < nums[mid]:
                # target 在前半部分
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # target 在后半部分
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False


if __name__ == '__main__':
    sol = Solution()
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 0
    print(sol.search(nums, target))

    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 3
    print(sol.search(nums, target))

    nums = [2, 5, 6, 0, 0, 0, 0]
    target = 0
    print(sol.search(nums, target))

    nums = [1]
    target = 1
    print(sol.search(nums, target))

    nums = [3, 1]
    target = 1
    print(sol.search(nums, target))

    nums = [3, 1, 1]
    target = 3
    print(sol.search(nums, target))

    nums = [1, 3]
    target = 3
    print(sol.search(nums, target))

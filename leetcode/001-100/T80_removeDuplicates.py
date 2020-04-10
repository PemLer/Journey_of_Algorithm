from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pos, ans, tmp = 1, 1, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                tmp += 1
                if tmp <= 2:
                    ans += 1
                    nums[pos] = nums[i]
                    pos += 1
            else:
                tmp = 1
                ans += 1
                nums[pos] = nums[i]
                pos += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [
        [1, 1, 1, 2, 2, 3],
        [0, 0, 1, 1, 1, 1, 2, 3, 3],
        [1, 2, 2, 3],
        [1, 1, 1, 2, 2, 3, 4]
    ]
    for num in nums:
        print(sol.removeDuplicates(num))

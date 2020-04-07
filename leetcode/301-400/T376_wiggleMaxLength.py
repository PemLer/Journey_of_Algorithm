from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        prev_diff = nums[1] - nums[0]
        count = 2 if prev_diff != 0 else 1
        for i in range(2, n):
            diff = nums[i] - nums[i-1]
            if prev_diff <= 0 and diff > 0 or prev_diff >= 0 and diff < 0:
                count += 1
                prev_diff = diff

        return count


if __name__ == '__main__':
    sol = Solution()
    nums = [
        [1, 7, 4, 9, 2, 5],
        [1, 17, 5, 10, 13, 15, 10, 5, 16, 8],
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]
    for num in nums:
        print(sol.wiggleMaxLength(num))
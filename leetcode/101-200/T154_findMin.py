class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1] or len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums)
        while l < r and nums[l] == nums[-1]:
            l += 1

        while l < r:
            mid = l + r >> 1
            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid

        return nums[l] if l < len(nums) else nums[0]
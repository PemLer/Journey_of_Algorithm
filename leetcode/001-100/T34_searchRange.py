class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        if not nums or l >= len(nums) or nums[l] != target:
            return [-1, -1]

        left = l

        l, r = 0, len(nums)
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1

        return [left, l-1]
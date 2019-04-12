class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                if mid > 0 and nums[mid-1] != target or mid == 0:
                    break
                else:
                    r = mid - 1
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        if l > r:
            return [-1, -1]
        left = mid
        
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                if mid < len(nums)-1 and nums[mid+1] != target or mid == len(nums)-1:
                    break
                else:
                    l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        right = mid
        return [left, right]
        
        

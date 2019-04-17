class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.helper(nums, 0, len(nums)-1, k)
    
    def helper(self, nums, l, r, k):
        if l == r:
            return nums[l]
        i, j = l, r
        p = nums[i]
        while i < j:
            while i < j and nums[j] <= p:
                j -= 1
            if i < j:
                nums[i] = nums[j]
                i += 1
                
            while i < j and nums[i] >= p:
                i += 1
            if i < j:
                nums[j] = nums[i]
                j -= 1
        # nums[i] = p
        if i + 1 == k:
            return p
        elif i + 1 < k:
            return self.helper(nums, i + 1, r, k)
        else:
            return self.helper(nums, l, i - 1, k)


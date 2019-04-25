class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i + 1:
                i += 1
            else:
                t = nums[i]-1
                if nums[t] == nums[i]:
                    return nums[i]
                nums[i], nums[t] = nums[t], nums[i]
            # print(i, nums)
        

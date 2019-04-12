class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        if l <= 2:
            return True
        t = 0
        for i in range(0,l):
            if i == 0 and nums[0] > nums[1]:
                t += 1
                nums[0] = nums[1]
            elif i == l-1 and nums[i] < nums[i-1]:
                t += 1
            elif i > 0 and i < l-1:
                if (nums[i] > nums[i+1] or nums[i] <nums[i-1]) and nums[i+1] >= nums[i-1]:
                    t += 1
                    nums[i] = nums[i-1]
                elif nums[i] > nums[i+1] and nums[i] >= nums[i-1]:
                    pass
                elif (nums[i] > nums[i+1] or nums[i] < nums[i-1]) and nums[i+1] < nums[i-1]:
                    return False
        if t <= 1:
            return True
        else:
            return False
                
                
            

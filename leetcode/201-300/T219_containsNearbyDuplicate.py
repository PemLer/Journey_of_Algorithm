class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        l = len(nums)
        d = {}
        for i in range(0,l):
            if nums[i] not in d:
                d[nums[i]] = i
            else:
                if i - d[nums[i]] <= k:
                    return True
                else:
                    d[nums[i]] = i
        return False
    

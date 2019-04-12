class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_tar = [x for x in range(1,len(nums)+1)]
        return list(set(nums_tar)-set(nums))
        
        

class Solution():
    def twoSum(self,nums,target):
        d={}
        for ii,num in enumerate(nums):
            if target - num in d:
                return [d[target - num],ii]
            d[num] = ii

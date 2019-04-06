class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for i in range(len(nums)):
            l = 0
            r = len(res) - 1
            while l <= r:
                mid = (l+r)//2
                if res[mid] < nums[i]:
                    l = mid + 1
                else:
                    r = mid - 1
            if l >= len(res):
                res.append(nums[i])
            else:
                res[l] = nums[i]
        return len(res)
                       

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            one = 0
            for num in nums:
                one += num >> i & 1
            ans += one * (len(nums) - one)
        return ans

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = dict()
        dic[0] = 1
        total, ans = 0, 0
        for num in nums:
            total += num
            if total - k in dic:
                ans += dic[total-k]
            if total not in dic:
                dic[total] = 1
            else:
                dic[total] += 1
        return ans

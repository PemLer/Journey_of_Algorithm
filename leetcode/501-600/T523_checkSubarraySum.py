class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        dic = {0: -1}

        total = 0
        for i in range(n):
            total += nums[i]
            if k != 0:
                total = total % k
            if total in dic:
                if i - dic[total] > 1:
                    return True
            else:
                dic[total] = i
        return False
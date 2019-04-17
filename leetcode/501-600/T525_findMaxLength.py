class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count, ans = 0, 0
        dic = dict()
        dic[0] = 0
        for i, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1
            if count in dic:
                ans = max(ans, i-dic[count]+1)
            else:
                dic[count] = i+1
        return ans

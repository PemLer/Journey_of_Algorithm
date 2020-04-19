class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, pos = len(nums), 0
        for i in range(n):
            if i <= pos:
                pos = max(pos, i + nums[i])
                if pos >= n - 1:
                    return True
        return False
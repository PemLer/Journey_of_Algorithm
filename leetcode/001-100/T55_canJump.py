class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        记录当前还可以跳的长度
        """
        step = nums[0]
        for i in range(1, len(nums)):
            if step > 0:
                step -= 1
                step = max(step, nums[i])
            else:
                break
        else:
            return True
        return False

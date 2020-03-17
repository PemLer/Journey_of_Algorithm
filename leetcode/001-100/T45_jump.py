class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        贪心算法
        """
        step, end, max_pos = 0, 0, 0
        for i in range(len(nums) - 1):
            max_pos = max(max_pos, nums[i]+i)
            if i == end:
                end = max_pos
                step += 1
        return step

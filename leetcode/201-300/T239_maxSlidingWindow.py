class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = []
        res  = []
        for i, v in enumerate(nums):
            while queue and i - k == queue[0]:
                queue.pop(0)
            while queue and v > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            res.append(nums[queue[0]])
        return res[k-1:]

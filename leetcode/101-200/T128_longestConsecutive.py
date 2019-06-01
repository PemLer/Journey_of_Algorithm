class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_len = dict()
        max_len = 0
        for num in nums:
            if num not in num_len:
                left = num_len.get(num-1, 0)
                right = num_len.get(num+1, 0)
                cur_len = 1 + left + right
                
                if cur_len > max_len:
                    max_len = cur_len
                
                num_len[num] = cur_len
                num_len[num-left] = cur_len
                num_len[num+right] = cur_len
        return max_len

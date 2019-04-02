class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        if s is None or len(s) == 0:
            return max_len
        str_dict = {}
        start = 0
        for i in range(len(s)):
            if s[i] in str_dict and str_dict[s[i]] >= start:
                start = str_dict[s[i]] + 1
            one_max = i - start + 1
            str_dict[s[i]] = i
            max_len = max(max_len, one_max)
        return max_len


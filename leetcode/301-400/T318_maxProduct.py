class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        bitmasks = [0] * n
        lens = [0] * n
        mask_func = lambda x: ord(x) - ord('a')

        for i, word in enumerate(words):
            bitmask = 0
            for ch in word:
                bitmask |= 1 << mask_func(ch)
            bitmasks[i] = bitmask
            lens[i] = len(word)

        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if bitmasks[i] & bitmasks[j] == 0:
                    res = max(res, lens[i] * lens[j])
        return res

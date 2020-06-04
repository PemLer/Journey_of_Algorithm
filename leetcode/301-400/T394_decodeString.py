class Solution:
    def decodeString(self, s: str) -> str:
        chars = []
        nums = []
        i = 0
        while i < len(s):
            char = s[i]
            if char.isdigit():
                tmp = 0
                while i < len(s) and s[i] != '[':
                    tmp = tmp * 10 + int(s[i])
                    i += 1
                nums.append(tmp)
            elif char == ']':
                tmp = []
                while chars and chars[-1] != '[':
                    tmp.append(chars.pop())
                chars.pop()
                chars.append(nums.pop() * ''.join(tmp[::-1]))
                i += 1
            else:
                chars.append(char)
                i += 1
        return ''.join(chars)

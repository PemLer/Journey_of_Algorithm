class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        nums,chars = [],[]
        i,l = 0,len(s)
        while i < l:
            j = i+1
            if s[i].isdigit():
                num = int(s[i])
                while j < l:
                    if s[j].isdigit():
                        num = num*10+int(s[j])
                        j += 1
                    else:
                        break
                nums.append(num)
            elif s[i] == '[' or s[i].isalpha():
                chars.append(s[i])
            else:
                t = chars.pop()
                tm = []
                while t != '[':
                    tm.append(t)
                    t = chars.pop()
                tmp = nums.pop() * ''.join(tm[::-1])
                chars.append(tmp)
            i = j
        return ''.join(chars)
                
                        
                

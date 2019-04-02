class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        temp = ['1','11','21']
        if n == 1:
            return temp[0]
        elif n == 2:
            return temp[1]
        elif n == 3:
            return temp[2]
        else:
            for j in range(3,n):
                str1 = temp[j-1]
                d = ''
                t = 1
                for i in range(0, len(str1)):
                    if i == 0:
                        print(i)
                    else:
                        if str1[i] == str1[i-1]:
                            t += 1
                        else:
                            d = d + str(t) + str1[i-1]
                            t = 1
                        if i == len(str1)-1:
                            if str1[i] == str1[i-1]:
                                #t +=1
                                d = d + str(t) + str1[i]
                                t = 1
                            else:
                                d = d + '1' + str1[i]
                temp.append(d)
            return temp[n-1]


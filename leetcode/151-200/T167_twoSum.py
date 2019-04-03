class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(numbers)
        a = numbers[0]
        d = {a:0}
        i = 1
        re = []
        while i<l and a + numbers[i] <= target:
            if target - numbers[i] in d:
                re.append(d[target - numbers[i]]+1)
                re.append(i+1)
                return re
            else:
                d[numbers[i]] = i
                i += 1

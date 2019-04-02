class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        d_t = ['','M','MM','MMM']
        d_h = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
        d_s = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX","XC"]
        d_g = ["", "I", "II", "III", "IV", "V", "VI", "VII","VIII", "IX"]
        return d_t[num//1000] + d_h[num//100%10] + d_s[num//10%10] + d_g[num%10]



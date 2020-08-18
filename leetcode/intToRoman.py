class Solution:
    def intToRoman(self, num):
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        res = ""
        for i, v in zip(numerals, values):
            res += (num // v) * i
            num %= v
        return res

class Solution2:
    def intToRoman(self, num: int) -> str:
        tho = {0:'', 1:'M', 2:'MM', 3:'MMM'}
        hun = {0:'', 1:'C', 2:'CC', 3:'CCC', 4:'CD', 5:'D', 6:'DC', 7:'DCC', 8:'DCCC', 9:'CM'}
        ten = {0:'', 1:'X', 2:'XX', 3:'XXX', 4:'XL', 5:'L', 6:'LX', 7:'LXX', 8:'LXXX', 9:'XC'}
        one = {0:'', 1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX'}
        return tho[num // 1000] + hun[num // 100 % 10] + ten[num // 10 % 10] + one[num % 10]

class Solution3:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
             100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 
             10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        ans = ''
        for x in sorted(d.keys(), reverse=True):
            v, num = divmod(num, x)
            ans += d[x] * v
        return ans

class Solution4:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        numericals=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        roman     =['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        
        i=0
        res=''
        while num > 0:
            if num-numericals[i]>=0:
                res+=roman[i]
                num=num-numericals[i]
            else:
                i+=1
        return res

answer = Solution4()
print(answer.intToRoman('XCIV'))

'''
not mine!
'''

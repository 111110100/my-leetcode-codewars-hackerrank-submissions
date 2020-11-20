class Solution3:
    def addStrings(self, num1: str, num2: str) -> str:
        if num1 == '0' and num2 == '0':
            return '0'
        Number = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        n1, n2 = 0, 0
        t = 1
        num1, num2 = list(num1), list(num2)

        while len(num1) > 0 or len(num2) > 0: 
            n1 += Number[num1.pop()] * t if len(num1) > 0 else 0
            n2 += Number[num2.pop()] * t if len(num2) > 0 else 0
            t *= 10
        return str(n1+n2)

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if num1 == '0' and num2 == '0':
            return '0'
        Number = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        n1,n2 = 0,0
        t = 1
        for x in num1[::-1]:
            n1 += Number[x] * t
            t *= 10
        t = 1
        for x in num2[::-1]:
            n2 += Number[x] * t
            t *= 10
        return str(n1+n2)

class Solution2:
    def addStrings(self, num1: str, num2: str) -> str:
        if num1 == '0' and num2 == '0':
            return '0'
        Number = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        n1, n2 = 0, 0
        t = 1
        if len(num1) > len(num2):
            num2 = '0' * (len(num1) - len(num2)) + num2
        elif len(num1) < len(num2):
            num1 = '0' * (len(num2) - len(num1)) + num1
        for x, y in zip(num1[::-1], num2[::-1]):
            n1 += Number[x] * t
            n2 += Number[y] * t
            t *= 10
        return str(n1 + n2)

answer = Solution()
print(answer.addStrings('123', '456'))
print(answer.addStrings('111', '10'))
print(answer.addStrings('1', '10'))
print(answer.addStrings('9333852702227987', '85731737104263'))

'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:
The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = list(num1), list(num2)
        carry, res = 0, []
        while len(num2) > 0 or len(num1) > 0:
            n1 = ord(num1.pop())-ord('0') if len(num1) > 0 else 0
            n2 = ord(num2.pop())-ord('0') if len(num2) > 0 else 0
            
            temp = n1 + n2 + carry 
            res.append(temp % 10)
            carry = temp // 10
        if carry: res.append(carry)
        return ''.join([str(i) for i in res])[::-1]

'''
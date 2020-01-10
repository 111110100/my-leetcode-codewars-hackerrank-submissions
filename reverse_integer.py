class Solution:
    def reverse(self, x: int) -> int:
        g = 1 if x >= 0 else -1
        s = str(abs(x))[::-1]
        n = int(s)
        if n > 0x7fffffff or n < -0x80000000:
            return 0
        else:
            return n*g

reversal = Solution()
print(reversal.reverse(-123))

'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers 
within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose 
of this problem, assume that your function returns 0 when the reversed 
integer overflows.
'''

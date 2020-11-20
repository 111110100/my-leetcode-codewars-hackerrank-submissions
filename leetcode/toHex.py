class Solution:
    def toHex(self, num) -> str:
        if num == 0: 
            return "0" 
            
        code = "0123456789abcdef"
        res = ""
        
        if num < 0:
            num = (-num ^ 0xffffffff) + 1
        
        while num != 0:
            x = num & 0xf
            res = code[x] + res
            num = num >> 4
        
        return res

answer = Solution()
print(answer.toHex(-1), hex(-1))

'''
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.
Example 1:

Input:
26

Output:
"1a"
Example 2:

Input:
-1

Output:
"ffffffff"

    def toHex(self, num):
        if num==0: return '0'
        mp = '0123456789abcdef'  # like a map
        ans = ''
        for i in range(8):
            n = num & 15       # this means num & 1111b
            c = mp[n]          # get the hex char 
            ans = c + ans
            num = num >> 4
        return ans.lstrip('0')  #strip leading zeroes


'''
class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = list(str(n))[::-1]
        i = 0
        r = ''
        for c in s:
            i += 1
            if i % 3 == 0:
                if len(s) == i:
                    r = c + r
                else:
                    r = '.' + c + r
            else:
                r = c + r
        return r

answer = Solution()
print(answer.thousandSeparator(123456789))

'''
Given an integer n, add a dot (".") as the thousands separator and return it in string format.

Example 1:

Input: n = 987
Output: "987"
Example 2:

Input: n = 1234
Output: "1.234"
Example 3:

Input: n = 123456789
Output: "123.456.789"
Example 4:

Input: n = 0
Output: "0"

class Solution:
    def thousandSeparator(self, n: int) -> str:
        return f"{n:,}".replace(",", ".")
'''
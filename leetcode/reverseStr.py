class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        r, p = '', 0
        for i in range(0, len(s), k):
            if p == 0:
                r += s[i:i+k][::-1]
                p = 1
            else:
                r += s[i:i+k]
                p = 0
        return r

answer = Solution()
print(answer.reverseStr('abcdefg', 2))

'''
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return "".join(s)
'''
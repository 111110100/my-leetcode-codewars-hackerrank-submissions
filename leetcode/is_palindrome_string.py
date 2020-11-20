class Solution:
    def isPalindrome(self, s: str) -> bool:
        return ''.join(filter(str.isalnum, s)).lower() == ''.join(filter(str.isalnum, s)).lower()[::-1]

answer = Solution()
print(answer.isPalindrome('A man, a plan, a canal: Panama'))
print(answer.isPalindrome('race a car'))

'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

Constraints:

s consists only of printable ASCII characters.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ''.join(filter(str.isalnum, s)).lower()
        b = ''.join(filter(str.isalnum, s)).lower()[::-1]
        return  a == b #Runtime: 32 ms, faster than 98.39% of Python3 online submissions for Valid Palindrome.


'''
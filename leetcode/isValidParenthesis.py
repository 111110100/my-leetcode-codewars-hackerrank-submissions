class Solution:
    def isValid(self, s: str) -> bool:
        brackets = ['()', '{}', '[]'] 
        while any(x in s for x in brackets): 
            for br in brackets: 
                s = s.replace(br, '') 
        return not s

answer = Solution()
print(answer.isValid('{[]{()}}'))
print(answer.isValid('{}[](([]))'))

'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n == 0:
            return True
        
        if n % 2 != 0:
            return False
            
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('{}','').replace('()','').replace('[]','')
        
        return s == ''

class Solution:
    def isValid(self, s: str) -> bool:
        while '[]' in s or '()' in s or '{}' in s:
            s = s.replace('[]','').replace('()','').replace('{}','')
        return not len(s)

'''
class Solution:
    def maxPower(self, s):
        n, p = 1, 1
        for x, y in zip(s, s[1:]):
            if x == y:
                n += 1
                if p < n:
                    p = n
            else:
                n = 1
        return p 

answer = Solution() 
print(answer.maxPower('leetcode'))
print(answer.maxPower('abbcccddddeeeeedcba'))
print(answer.maxPower('hooraaaaaaaaaaay'))
print(answer.maxPower('aa'))

'''
Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.

Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
Example 3:

Input: s = "triplepillooooow"
Output: 5
Example 4:

Input: s = "hooraaaaaaaaaaay"
Output: 11
Example 5:

Input: s = "tourist"
Output: 1

Constraints:

1 <= s.length <= 500
s contains only lowercase English letters.
'''
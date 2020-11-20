class Solution:
    def maxNumberOfBalloons(self, text):
        n = text.count('b')
        while n > 0:
            if n == 0:
                break
            if text.count('a') >= n:
                if text.count('n') >= n:
                    if text.count('o') >= n * 2:
                        if text.count('l') >= n * 2:
                            break
                        else:
                            n -= 1
                    else:
                        n -= 1
                else:
                    n -= 1
            else:
                n -= 1
        return n


answer = Solution()
print(answer.maxNumberOfBalloons("nlaebolko"))
print(answer.maxNumberOfBalloons("loonbalxballpoon"))
print(answer.maxNumberOfBalloons("loboonbalxbaallpoooonbb"))
print(answer.maxNumberOfBalloons("bleetcode"))

'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:

Input: text = "nlaebolko"
Output: 1
Example 2:

Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        return min(text.count('b'), text.count('a'), text.count('l') // 2, text.count('o') // 2, text.count('n'))

class Solution:
    def maxNumberOfBalloons(self, t: str) -> int:
        return min(t.count(c) // int(cnt) for c, cnt in zip('balon', '11221'))

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        return min(text.count(c) // 'balloon'.count(c) for c in 'balon')
'''
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        t = word.isupper() or word.islower() or word.istitle()
        return t

answer = Solution()
print(answer.detectCapitalUse('GOOGLE'))
print(answer.detectCapitalUse('google'))
print(answer.detectCapitalUse('Yahoo'))

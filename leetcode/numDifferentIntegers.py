import re

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        return len(set([int(i) for i in (re.split('[a-z]', word)) if i != '']))

answer = Solution()
print(answer.numDifferentIntegers('a123bc34d8ef34'))
print(answer.numDifferentIntegers('a1b01c001'))

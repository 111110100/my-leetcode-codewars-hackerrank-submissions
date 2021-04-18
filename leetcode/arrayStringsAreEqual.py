from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2) 

answer = Solution()
input1 = ["abc", "d", "defg"]
input2 = ["abcddefgh"]
print(answer.arrayStringsAreEqual(input1, input2))

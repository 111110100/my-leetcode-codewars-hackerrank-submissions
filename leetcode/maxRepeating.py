class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        i = 1
        while word * i in sequence:
            i += 1
        return i - 1

class Solution2:
    def maxRepeating(self, sequence: str, word: str) -> int:
        return sum(word * i in sequence for i in range(1, 101))

answer = Solution()
print(answer.maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba", "aaaba"))
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if A == B:
            return False
        return sorted(A) == sorted(B)

answer = Solution()
print(answer.buddyStrings('aaaaaaabc', 'aaaaaaacb'))
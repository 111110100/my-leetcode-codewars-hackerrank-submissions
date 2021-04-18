class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(s.split()[:k])
        
answer = Solution()
print(answer.truncateSentence("Hello how are you Contestant", 4))
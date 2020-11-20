class Solution:
    def isAlmostPalindrome(self, s):
        #if s == s[::-1]:
        #    return True
        #return (100 - (sum(i != j for i, j in zip(list(s), list(s)) / float(len(s)))) * 100) 
        return ( 100 - (sum(i != j for i, j in zip(list(s), list(s)[::-1])) / float(len(s))) * 100 ) >= 60

answer = Solution()
print(answer.isAlmostPalindrome('levtt'))
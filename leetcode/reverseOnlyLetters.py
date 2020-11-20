class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letters = [ch for ch in S if ch.isalpha()]
        return ''.join([letters.pop() if S[i].isalpha() else S[i] for i in range(len(S))])

answer = Solution()
print(answer.reverseOnlyLetters('ab-cde'))
print(answer.reverseOnlyLetters('a-bC-dEf-ghIj'))
print(answer.reverseOnlyLetters('Test1ng-Leet=code-Q!'))

'''
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

Note:

S.length <= 100
33 <= S[i].ASCIIcode <= 122 
S doesn't contain \ or "

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        i, j = 0, len(S) - 1
        S = list(S)
        while i < j:
            while i < j and not S[i].isalpha(): i += 1
            while i < j and not S[j].isalpha(): j -= 1
            S[i], S[j] = S[j], S[i]
            i, j = i + 1, j - 1
        return "".join(S)

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S, i, j = list(S), 0, len(S) - 1
        while i < j:
            if not S[i].isalpha():
                i += 1
            elif not S[j].isalpha():
                j -= 1
            else:
                S[i], S[j] = S[j], S[i]
                i, j = i + 1, j - 1
        return "".join(S)
'''
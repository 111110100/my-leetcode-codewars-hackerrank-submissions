class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False
        alphabet = {chr(i) for i in range(97, 123)}
        return alphabet == set(sentence)

class Solution2:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False
        return len(set(sentence)) == 26


answer = Solution()
print(answer.checkIfPangram('thequickbrownfoxjumpsoverthelazydog'))

'''
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:

Input: sentence = "leetcode"
Output: false
 

Constraints:

1 <= sentence.length <= 1000
sentence consists of lowercase English letters.
'''
